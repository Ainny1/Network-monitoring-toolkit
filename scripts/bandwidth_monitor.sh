#!/usr/bin/env bash
# Linux-only interface byte counters; does not capture packets.
set -euo pipefail
iface="${1:-lo}"
if [[ ! "$iface" =~ ^[a-zA-Z0-9_.:-]+$ ]]; then
  echo "Invalid interface name" >&2; exit 2
fi
rx="/sys/class/net/$iface/statistics/rx_bytes"
tx="/sys/class/net/$iface/statistics/tx_bytes"
if [[ ! -r "$rx" || ! -r "$tx" ]]; then
  echo "Interface not found or /sys unavailable: $iface" >&2; exit 2
fi
read -r before_rx < "$rx"; read -r before_tx < "$tx"
sleep 1
read -r after_rx < "$rx"; read -r after_tx < "$tx"
printf '%s RX: %d B/s | TX: %d B/s (approx.)\n' "$iface" "$((after_rx-before_rx))" "$((after_tx-before_tx))"
