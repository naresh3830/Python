import argparse
import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def parse_config(file_path):
    try:
        config = configparser.ConfigParser()
        config.read(file_path)
        return {section: dict(config.items(section)) for section in config.sections()}
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None

def save_to_json(data, json_file_path):
    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Configuration data saved to {json_file_path}")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")

@app.route('/get_config', methods=['GET'])
def get_config():
    return jsonify({"Configuration": parse_config(app.config['CONFIG_PATH'])})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Configuration Management Program')
    parser.add_argument('--config', type=str, help='Path to the configuration file', default='sample_config.ini')
    args = parser.parse_args()

    app.config['CONFIG_PATH'] = args.config
    configuration_data = parse_config(args.config)

    if configuration_data:
        save_to_json(configuration_data, 'output.json')

    app.run(debug=True)
