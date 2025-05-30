from flask import Flask, render_template, request, jsonify
import json
import os
import subprocess

app = Flask(__name__, template_folder='templates')

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.json')

# Load config
def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save config
def save_config(data):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    config = load_config()
    return render_template("index.html", config=config)

@app.route("/update_config", methods=["POST"])
def update_config():
    try:
        data = request.json
        save_config(data)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/run_ai")
def run_ai():
    try:
        # Get absolute path to brain.py
        brain_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core', 'brain.py'))
        venv_activate = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'venv', 'bin', 'activate'))

        # Run brain.py inside virtual environment
        subprocess.Popen(
            f"source {venv_activate} && python3 {brain_path}",
            shell=True,
            executable="/bin/bash"
        )
        return jsonify({"status": "launched"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
