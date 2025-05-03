
# Network Monitoring Toolkit

A comprehensive, open-source toolkit designed to help system administrators, cybersecurity professionals, and network engineers monitor, analyze, and visualize their networks effectively.

<p align="center">
  <img src="banner.png" alt="Network Monitoring Toolkit Banner" width="600"/>
</p>

---

## Features

- Real-time network monitoring using Prometheus and Grafana
- Host and service status tracking with Zabbix and Nagios
- Custom scripts for port scanning, ping sweeps, and bandwidth usage
- Preconfigured alerting rules and dashboards
- Modular and extensible design for custom environments

## Repository Structure

```
network-monitoring-toolkit/
├── scripts/                  # Bash and Python scripts for scanning and monitoring
├── config/                   # Configuration files (SNMP, Prometheus, etc.)
├── dashboards/               # Grafana dashboards in JSON format
├── tools/                    # Setup guides for open-source tools
├── alerts/                   # Prebuilt alert rules for Prometheus/Zabbix
├── docs/                     # Usage guide and architecture diagrams
├── LICENSE
├── README.md
└── CONTRIBUTING.md
```

## Quick Start

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/network-monitoring-toolkit.git
   cd network-monitoring-toolkit
   ```

2. **Make scripts executable**:
   ```bash
   chmod +x scripts/*.sh
   ```

3. **Run the ping sweep script**:
   ```bash
   ./scripts/ping_sweep.sh 192.168.1
   ```

4. **Set up monitoring tools**:
   - Follow `tools/setup_prometheus.md` to configure Prometheus + Grafana
   - Use `tools/setup_zabbix.md` or `tools/setup_nagios.md` for full-stack monitoring

## Live Demo (Terminal Menu)

Want to try out the toolkit in action? Run the interactive menu:

```bash
chmod +x scripts/live_demo.sh
./scripts/live_demo.sh
```

This script lets you:
- Run a ping sweep on any subnet
- Scan open ports on a target IP
- Monitor real-time bandwidth usage

## Requirements

- Linux (preferred) or macOS
- Bash and Python 3
- Docker (optional, for containerized deployments)
- Admin access to monitoring targets (SNMP, SSH, etc.)

## Tools Used

- [Prometheus](https://prometheus.io)
- [Grafana](https://grafana.com)
- [Zabbix](https://www.zabbix.com)
- [Nagios Core](https://www.nagios.org/projects/nagios-core/)
- [Wireshark](https://www.wireshark.org)

## Scripts Included

- `ping_sweep.sh` – Ping a subnet and list online hosts
- `port_scanner.py` – Scan specified ports on a host
- `bandwidth_monitor.sh` – Monitor bandwidth with ifstat (optional)
- `live_demo.sh` – Interactive menu for running demo tools

## Screenshots & Dashboards

> Add screenshots of your Grafana dashboard or terminal output here for visual appeal.

## Roadmap

- [ ] Add Docker Compose setup for Prometheus + Grafana
- [ ] Add email/SMS alerting setup guide
- [ ] Add CLI launcher for all scripts
- [ ] Add Ansible playbook for tool installation

## Contributing

Contributions are welcome! Please open an issue or pull request. See `CONTRIBUTING.md` for more.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Author

Created and maintained by Ainny1

---

## 1. `port_scanner.py` (Python TCP Port Scanner)

```python
#!/usr/bin/env python3
import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python3 port_scanner.py <target_ip> <start-end>")
    sys.exit(1)

target = sys.argv[1]
port_range = sys.argv[2]
start_port, end_port = map(int, port_range.split('-'))

print(f"Scanning {target} from port {start_port} to {end_port}...")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

print("Scan complete.")
```

**Save as:** `scripts/port_scanner.py`  
**Make it executable:**
```bash
chmod +x scripts/port_scanner.py
```

---

## 2. `bandwidth_monitor.sh` (Real-Time Interface Monitor)

```bash
#!/bin/bash

# Requires: ifstat
# Install: sudo apt install ifstat (Debian/Ubuntu) or brew install ifstat (macOS)

if ! command -v ifstat &> /dev/null; then
    echo "Error: ifstat is not installed."
    echo "Install it with: sudo apt install ifstat"
    exit 1
fi

echo "Monitoring bandwidth (eth0)... Press Ctrl+C to stop."
ifstat -i eth0 1
```

**Save as:** `scripts/bandwidth_monitor.sh`  
**Make it executable:**
```bash
chmod +x scripts/bandwidth_monitor.sh
```

 