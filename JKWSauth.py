from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from jose import jwk, jwt
import uuid

app = Flask(__name__)

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Serialize keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Key ID (kid) and expiry timestamp
key_id = str(uuid.uuid4())
expiry_timestamp = datetime.now() + timedelta(days=30)

# JWKS endpoint
@app.route('/jwks', methods=['GET'])
def jwks():
    keys = [{
        "kty": "RSA",
        "kid": key_id,
        "use": "sig",
        "alg": "RS256",
        "n": public_key.public_numbers().n,
        "e": public_key.public_numbers().e,
        "exp": int(expiry_timestamp.timestamp())
    }]
    return jsonify(keys)

# Authentication endpoint
@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        # Generate JWT
        token = jwt.encode({'user': 'fake_user'}, private_pem, algorithm='RS256', headers={'kid': key_id})
        return jsonify({'access_token': token.decode('utf-8')})

if __name__ == '__main__':
    app.run(port=8080)
