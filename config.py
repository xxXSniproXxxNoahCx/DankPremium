import json
import os

def load_config():
    with open(config_file, 'r') as configfile:
        CONFIG = json.load(configfile)
    return CONFIG

def save_config():
    with open(config_file, 'w') as configfile:
        json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)

RUN_PATH = os.getcwd()

config_file = 'my.json'
CONFIG = load_config()
if not "bal" in CONFIG:
    CONFIG["bal"] = {}
if not "cs" in CONFIG:
    CONFIG["cs"] = {}
