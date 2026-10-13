# Verified scope and quick start

This repository contains **bounded diagnostic scripts** and offline unit tests. It does **not** include a working Prometheus/Grafana/Zabbix/Nagios deployment.

## Linux/macOS examples

From the repository root:

```bash
bash scripts/ping_sweep.sh 127.0.0.1
python3 scripts/port_scanner.py 127.0.0.1 --ports 22,80,443
bash scripts/live_demo.sh
```

Linux only, for a present interface:

```bash
bash scripts/bandwidth_monitor.sh lo
```

The ping tool accepts **1–16 numeric addresses**; it is not a subnet enumerator. A missing ping response does not prove a host is offline. The TCP tool accepts one numeric IP and up to 20 ports, with 0.1–3 second timeouts. A failed TCP connection is shown as closed/filtered, not proof of a firewall or compromise.

## Offline checks

```bash
python3 -m unittest discover -s tests -v
bash -n scripts/*.sh
```

These checks validate Python behavior and shell syntax; they do not validate network monitoring deployments. Capture real, redacted lab results separately before claiming end-to-end validation.

## Safety

Run against your own systems or explicit authorized targets only. No public-IP scanning is required; use loopback addresses for initial experiments.
