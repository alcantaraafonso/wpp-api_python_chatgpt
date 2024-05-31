from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def index():
    return "Welcome"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        accessToken = "BEGA98721NHAWHAT345SAPP"
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token is not None and challenge is not None and token == accessToken:
            return challenge
        
        return "", 400
    except:
        return "", 400


@app.route('/whatsapp', methods=['POST'])
def receivedMessage():
    return "message received"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)