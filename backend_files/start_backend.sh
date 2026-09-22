#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-7860}"
export PORT
python -m pip install -r backend_files/requirements.txt
exec python backend_files/app.py
