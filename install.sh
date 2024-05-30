#!/bin/bash

python -m venv rbac-webapp-env
source rbac-webapp-env/bin/activate
pip install flask kubernetes
