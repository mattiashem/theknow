#!/bin/bash
#
#
# Startup script for the app

python -u getlinks.py & gunicorn -b 0.0.0.0:8080 api_endpoint:api --reload
