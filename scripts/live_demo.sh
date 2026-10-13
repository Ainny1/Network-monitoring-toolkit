#!/usr/bin/env bash
# Interactive menu for authorized local diagnostics.
set -euo pipefail
cd "$(dirname "$0")"
while true; do
  printf '\nNetwork Toolkit\n1) Ping loopback\n2) Check loopback TCP ports\n3) Linux loopback byte counters\n4) Exit\n'
  read -r -p 'Choose [1-4]: ' choice || exit 0
  case "$choice" in
    1) bash ./ping_sweep.sh 127.0.0.1 ;;
    2) python3 ./port_scanner.py 127.0.0.1 --ports 22,80,443 ;;
    3) bash ./bandwidth_monitor.sh lo ;;
    4) exit 0 ;;
    *) echo 'Choose 1-4' ;;
  esac
done
