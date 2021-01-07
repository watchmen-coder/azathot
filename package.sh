apt upgrade && apt update -u
apt install python -y
apt install w3m -y
pip install -r tools/doc/requirements.txt
mv tools/azathot/azathot.py .
chmod +x azathot.py
rm -rf package.sh