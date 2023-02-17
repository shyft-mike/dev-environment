#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 8081 --root-path /api/v1 --app-dir=src