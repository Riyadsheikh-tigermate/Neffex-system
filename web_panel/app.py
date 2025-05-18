from flask import Flask, render_template, request, jsonify
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core import brain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    lang = request.json.get('lang', 'en')
    response = brain.process(user_input, lang)
    return jsonify({'response': response})

@app.route('/status')
def status():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return jsonify(config)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
