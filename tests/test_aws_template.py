"""Offline structural checks; no AWS credentials or calls."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "aws/private-monitoring.yaml").read_text(encoding="utf-8")


class AwsTemplateTests(unittest.TestCase):
    def test_no_inbound_rules(self):
        self.assertNotIn("SecurityGroupIngress:", TEMPLATE)
        self.assertNotIn("0.0.0.0/0\n          FromPort: 3000", TEMPLATE)

    def test_ssm_role_and_encryption(self):
        self.assertIn("AmazonSSMManagedInstanceCore", TEMPLATE)
        self.assertIn("Encrypted: true", TEMPLATE)

    def test_no_embedded_secret(self):
        self.assertNotIn("GRAFANA_ADMIN_PASSWORD", TEMPLATE)
        self.assertNotIn("UserData:", TEMPLATE)


if __name__ == "__main__":
    unittest.main()
