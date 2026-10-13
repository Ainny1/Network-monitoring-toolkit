# Local Prometheus + Grafana lab

This optional Docker Compose lab runs Prometheus and Grafana on **localhost only**. It monitors **Prometheus itself**, not your entire network. The provisioned dashboard is real JSON configuration, but runtime validation and screenshots must be captured on your computer.

## Windows 11 prerequisites

Install Docker Desktop with Linux containers enabled. In PowerShell, from the repository root:

```powershell
Copy-Item .env.example .env
notepad .env
docker compose config
docker compose up -d
docker compose ps
```

Change the example password in `.env` to a unique strong password **before** starting. Never commit `.env`.

Open Grafana at **http://127.0.0.1:3000** and Prometheus at **http://127.0.0.1:9090**. Grafana username is `admin`; password is the one you chose. The dashboard is in **Dashboards → Network Toolkit → Network Toolkit | Prometheus Health**. Wait about one minute for samples.

In Prometheus, query `up{job="prometheus"}`; it should equal `1` if self-scraping works. If Grafana panels are empty, inspect `docker compose logs prometheus grafana` and confirm the data source points to `http://prometheus:9090` **inside Docker**, not localhost.

Capture a real screenshot **only after** the services run. Redact usernames, infrastructure addresses, tokens, and other private details. No screenshot or end-to-end validation is claimed in the repository yet.

Stop the lab with `docker compose down`. To remove stored data too, use `docker compose down -v` (this deletes the lab volumes).

## Scope and limits

Only Prometheus and Grafana are provisioned. Zabbix and Nagios are not installed and no screenshots for them are claimed. Grafana's dashboard monitors the Prometheus server itself; adding real host/network exporters and alert rules is future work. The published ports bind to `127.0.0.1`, not all network interfaces.
