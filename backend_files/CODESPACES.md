# SuperKart backend in GitHub Codespaces

This repository contains the SuperKart Flask prediction API and the serialized
Random Forest pipeline. It is intended to run in a GitHub Codespace owned by
`vijaygurav24-png`.

## Start the API

From the repository root:

```bash
bash backend_files/start_backend.sh
```

The API listens on `0.0.0.0:7860`. Open the forwarded port in the Codespaces
**PORTS** panel.

## Test the API

```bash
curl http://localhost:7860/health
```

Send all fields listed in `backend_files/app.py` to `POST /v1/predict` as JSON.
