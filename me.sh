
git pull origin main || { echo "Git pull failed..."; exit 1; }
pip install -r ./me/requirements.txt || { echo "Pip install failed..."; exit 1; }

echo "Running python me.py..."
python -c 'from me.main import *; wake_up()' || { echo "Python script failed..."; exit 1; }

# commit all and if any changes, push:
git add . || { echo "Git add failed..."; exit 1; }

if ! git diff --cached --quiet; then
    git commit -m "Automated commit from me.sh" || { echo "Git commit failed..."; exit 1; }
    git push origin main || { echo "Git push failed..."; exit 1; }
else
    echo "No changes to commit."
fi
