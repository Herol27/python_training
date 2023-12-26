#!/bin/bash

cd src

uvicorn todolist_api:app --host 0.0.0.0 --port 8000 --reload