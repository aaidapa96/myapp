import ssl
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

CORS(app, resources={r"/submit": {"origins": "*"}})
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    # Process the data (e.g., store it in a database)
    # In this example, we'll just print it
    print("Received data:", data)

    # Send a response back to the frontend
    return jsonify({"message": "Data received successfully"})

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(host='0.0.0.0',debug=True, port=3000,ssl_context=context)