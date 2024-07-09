from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    message = f"Hello {name}, I am your server Trixy."
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
