from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/vehicle', methods=['GET'])
def vehicle():
    key = request.args.get('key')
    query = request.args.get('query')
    
    if key != 'beast':
        return jsonify({'success': False, 'message': 'Invalid API key', 'api_dev': '@BeastAccuser'}), 401
    if not query:
        return jsonify({'success': False, 'message': 'Missing vehicle number', 'api_dev': '@BeastAccuser'}), 400
    
    clean = re.sub(r'[^A-Z0-9]', '', query.upper())
    real = f'https://usersxinfo-admin.onrender.com/api?key=freevehnum&type=vnumadv&term={clean}'
    
    try:
        resp = requests.get(real, timeout=30)
        data = resp.json()
        return jsonify({'result': data.get('result'), 'success': True, 'api_dev': '@BeastAccuser'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e), 'api_dev': '@BeastAccuser'}), 502

@app.route('/')
def home():
    return jsonify({'status': 'alive', 'api_dev': '@BeastAccuser'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
