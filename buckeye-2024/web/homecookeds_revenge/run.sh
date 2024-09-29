#!/bin/bash
export PYTHONUNBUFFERED=1
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8001 -t 5
