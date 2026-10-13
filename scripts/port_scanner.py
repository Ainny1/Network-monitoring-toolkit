#!/usr/bin/env python3
"""Bounded TCP connect checks for hosts you own or are authorized to test."""
import argparse
import ipaddress
import socket


def parse_ports(value):
    ports = []
    for item in value.split(","):
        item = item.strip()
        if not item.isdecimal() or not 1 <= int(item) <= 65535:
            raise argparse.ArgumentTypeError("ports must be comma-separated integers from 1 to 65535")
        ports.append(int(item))
    if not ports or len(ports) > 20:
        raise argparse.ArgumentTypeError("provide between 1 and 20 ports")
    return sorted(set(ports))


def check_port(host, port, timeout=0.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (OSError, TimeoutError):
        return False


def main():
    parser = argparse.ArgumentParser(description="Check up to 20 TCP ports on one authorized IP address.")
    parser.add_argument("host", help="single IPv4/IPv6 address (no CIDR or hostnames)")
    parser.add_argument("--ports", type=parse_ports, default=[22, 80, 443])
    parser.add_argument("--timeout", type=float, default=0.5)
    args = parser.parse_args()
    try:
        ipaddress.ip_address(args.host)
    except ValueError:
        parser.error("host must be a single numeric IP address")
    if not 0.1 <= args.timeout <= 3:
        parser.error("--timeout must be between 0.1 and 3 seconds")
    for port in args.ports:
        print(f"{args.host}:{port} {'open' if check_port(args.host, port, args.timeout) else 'closed/filtered'}")


if __name__ == "__main__":
    main()
