echo ["HL Engine 3 Setup"]
python3 -m venv .venv
source venv/bin/activate
pip install -r requirements.txt

git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd unitree_sdk2_python
pip install -e .
cd ..