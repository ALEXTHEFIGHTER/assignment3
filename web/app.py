from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/set', methods=['POST'])
def set_value():
    data = request.json
    r.set(data['key'], data['value'])
    return jsonify({'status': 'ok'})

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = r.get(key)
    return jsonify({'key': key, 'value': value.decode() if value else None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
