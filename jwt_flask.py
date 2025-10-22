from flask import Flask, jsonify
import jwt, datetime

app = Flask(__name__)
SECRET_KEY = "mi_secreto"

@app.route('/login/<usuario>')
def login(usuario):
    payload = {
        "user": usuario,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

@app.route('/verificar/<token>')
def verificar(token):
    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"estado": "válido", "datos": datos})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"})

if __name__ == '__main__':
    app.run(port=5001)
