#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-7860}"
pkill -f "backend_files/app.py" || true
pkill -f "gunicorn.*:${PORT}" || true
