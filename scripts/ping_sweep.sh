#!/usr/bin/env bash
# Reachability checks for a bounded set of explicitly authorized hosts.
set -euo pipefail
if [[ "$#" -lt 1 || "$#" -gt 16 ]]; then
  echo "Usage: $0 HOST [HOST ...] (1-16 authorized IP addresses)" >&2
  exit 2
fi
for host in "$@"; do
  if [[ ! "$host" =~ ^[0-9a-fA-F:.]+$ ]]; then
    echo "Only numeric IP addresses are accepted: $host" >&2
    exit 2
  fi
done
for host in "$@"; do
  if ping -c 1 -W 1 -- "$host" >/dev/null 2>&1; then
    printf '%s reachable\n' "$host"
  else
    printf '%s no ping reply (may be filtered)\n' "$host"
  fi
done
