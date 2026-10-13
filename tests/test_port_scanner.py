"""Offline unit tests; no external network traffic."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import argparse

SPEC = importlib.util.spec_from_file_location("port_scanner", Path(__file__).resolve().parents[1] / "scripts" / "port_scanner.py")
scanner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scanner)


class PortScannerTests(unittest.TestCase):
    def test_valid_ports(self):
        self.assertEqual(scanner.parse_ports("443,80,443"), [80, 443])

    def test_reject_invalid_port(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            scanner.parse_ports("0")

    def test_reject_too_many_ports(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            scanner.parse_ports(",".join(map(str, range(1, 22))))

    def test_open_socket(self):
        with patch.object(scanner.socket, "create_connection") as connect:
            self.assertTrue(scanner.check_port("127.0.0.1", 80))
            connect.assert_called_once_with(("127.0.0.1", 80), timeout=0.5)

    def test_closed_socket(self):
        with patch.object(scanner.socket, "create_connection", side_effect=OSError):
            self.assertFalse(scanner.check_port("127.0.0.1", 80))


if __name__ == "__main__":
    unittest.main()
