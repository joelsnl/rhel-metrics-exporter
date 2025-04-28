# RHEL Metrics Exporter

Exposes CPU, Memory, and Disk usage metrics for Prometheus/Grafana monitoring.

## Features
- Lightweight.
- Exposes `/metrics` endpoint on port 8000.
- Compatible with Prometheus scrape targets.

## Requirements
- Python 3
- Flask
- psutil

Install dependencies:
```bash
pip install flask psutil
