import json

def load_rules(file_path='rules.json'):
    with open(file_path, 'r') as file:
        return json.load(file)
