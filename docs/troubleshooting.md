# Troubleshooting the local diagnostic tools

This guide covers common issues when running the **bounded, authorized** diagnostics described in [quick start](quickstart.md). Examples use only loopback (127.0.0.1) or the machine's own Linux interface; do not test third-party hosts without explicit permission.

## First verify the basics

From the repository root, run:

```bash
python3 --version
python3 -m unittest discover -s tests -v
bash -n scripts/*.sh
```

These checks test Python logic and shell syntax, **not** a deployed monitoring stack. If `python3` is missing, install Python 3 using your operating system's standard package manager.

## TCP port check reports closed/filtered

Try the documented loopback example:

```bash
python3 scripts/port_scanner.py 127.0.0.1 --ports 22,80,443
```

- No service may be listening on the selected port. A failed connection is not evidence of compromise.
- A timeout can be caused by filtering, networking conditions, or another environmental issue; the script cannot prove which cause applies.
- For a meaningful **open** result, use a TCP service that you intentionally started on your own computer, and ensure its port is within the tool's limits. Stop the test service when finished.
- Use numeric IP addresses and no more than 20 ports, as described in the quick start.

## Ping gets no reply

```bash
bash scripts/ping_sweep.sh 127.0.0.1
```

- A missing ICMP response does not necessarily mean a system is offline.
- Verify that `ping` is installed and accessible in your shell.
- Provide 1–16 individual numeric addresses, not a CIDR subnet.

## Bandwidth monitor cannot find an interface

On Linux, list available network interface names with:

```bash
ls /sys/class/net
```

Then supply a name that exists, for example:

```bash
bash scripts/bandwidth_monitor.sh lo
```

This script samples Linux interface RX/TX byte counters for one second. The interface name `lo` is a common loopback example; the script is not a macOS bandwidth monitor. Little or no observed traffic is expected if the chosen interface is idle.

## Interactive demo fails

```bash
bash scripts/live_demo.sh
```

Run this command from the repository root and ensure Bash, Python 3, and any utilities needed by the selected menu option are installed. On macOS, use menu options 1–2; the Linux interface counter option requires Linux.

## Prometheus/Grafana screenshot missing

The Docker Compose configuration is a **local lab configuration**, not evidence of a running or verified monitoring deployment. Follow [monitoring lab setup](monitoring-lab.md) and validate the actual services before capturing screenshots. Do not post placeholder dashboards as real test results.

## Before sharing a screen recording

- Show only your own lab targets, such as `127.0.0.1`, or systems for which you have explicit written authorization.
- Hide authentication tokens, credentials, personal paths, and sensitive information in terminal history and browser tabs.
- Describe the scripts as basic diagnostic tools; avoid claiming intrusion detection or production monitoring that has not been validated.
