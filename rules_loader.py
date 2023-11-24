import json

def load_rules(file_path='rules.json') -> dict:
    with open(file_path, 'r') as file: #open rules.json with read operation and stores rules object in variable file
        return json.load(file) #with ensures that the file is closed completely after read operation is complete