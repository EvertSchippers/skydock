#!/bin/bash

git clone "$REPO" . || { echo "Git clone failed..."; sleep 60; continue; }
pip install -e ./me || { echo "Pip install failed..."; sleep 60; continue; }

echo "Running python me.py..."
python -c 'from me.main import *; wake_up()' || { echo "Python script failed..."; sleep 60; continue; }

