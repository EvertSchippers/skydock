#!/bin/bash

# Clone to begin with...
git clone "$REPO" repo || { echo "Git clone failed..."; exit 1; }

# Move into repo directory
cd repo || { echo "Changing directory failed..."; exit 1; }
chmod +x ./me.sh || { echo "Setting execute permission on me.sh failed..."; exit 1; }

# Create an environment and activate it
python -m venv .venv || { echo "Creating virtual environment failed..."; exit 1; }
source .venv/bin/activate || { echo "Activating virtual environment failed..."; exit 1; }

# Upgrade pip to the latest version
pip install --upgrade pip

# Get me going!
while true; do
    ./me.sh || { echo "Execution of me.sh failed with exit code $?"; }
    echo "Restarting in 60 seconds..."
    sleep 60
done
