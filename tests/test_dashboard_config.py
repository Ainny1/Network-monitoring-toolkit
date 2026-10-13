"""Offline checks for the checked-in dashboard definition."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DashboardConfigTests(unittest.TestCase):
    def test_dashboard_json_and_panels(self):
        path = ROOT / "monitoring/grafana/dashboards/prometheus-health.json"
        dashboard = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(dashboard["uid"], "network-toolkit-health")
        self.assertGreaterEqual(len(dashboard["panels"]), 2)
        for panel in dashboard["panels"]:
            self.assertTrue(panel["targets"])
            self.assertEqual(panel["datasource"]["uid"], "prometheus")

    def test_no_broken_screenshot_markdown(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("screenshots/grafana_dashboard.png", readme)
        self.assertNotIn("screenshots/zabbix_interface.png", readme)
        self.assertNotIn("screenshots/nagios_dashboard.png", readme)


if __name__ == "__main__":
    unittest.main()
