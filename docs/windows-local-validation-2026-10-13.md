# Windows 11 local validation — 13 October 2026

## Scope

A local, authorized check of the Network Monitoring Toolkit on Windows 11 using the Python port scanner and offline unit tests. This is **not** evidence of a Prometheus, Grafana, Zabbix, or Nagios deployment.

## Commands

From the repository root in PowerShell:

```powershell
py -3 -m unittest discover -s tests -v
py -3 scripts\port_scanner.py 127.0.0.1 --ports 22,80,443
```

## Reported outcome

The project maintainer confirmed:

- All **five Python unit tests passed** with `OK`.
- The TCP port scanner returned results for **127.0.0.1** on ports **22, 80, and 443**.

The exact open/closed results, command output, Python version, and screenshots were **not supplied**, so they are not reproduced or inferred here.

## Interpretation

These results support that the Python tests and loopback TCP checks ran successfully in the maintainer's Windows environment. They do **not** validate the Bash scripts, Linux interface monitoring, alerting, dashboard integrations, or any non-local network scan.

## Follow-up evidence

- [ ] Capture a redacted terminal screenshot or sanitized command output.
- [ ] Verify the GitHub Actions workflow completed successfully.
- [ ] Run Bash checks in a Linux lab or Kali VM and record results.
- [ ] Implement and validate a monitoring dashboard separately.

## Safety

The target `127.0.0.1` is loopback and does not expose or scan a public IP address.
