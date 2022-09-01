#!/bin/sh
python3 -m venv .venv_marcus
source .venv_marcus/bin/activate
pip install -r requirements.txt
deactivate