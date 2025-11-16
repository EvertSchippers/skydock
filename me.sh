
git pull origin main || { echo "Git pull failed..."; exit 1; }
pip install -r ./me/requirements.txt || { echo "Pip install failed..."; exit 1; }

echo "Running python me.py..."
python -c 'from me.main import *; wake_up()' || { echo "Python script failed..."; exit 1; }
