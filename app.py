from flask import Flask, request
import util

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
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.get_text_user(message)
        print(f'{text=}')
        # deve SEMPRE retornar EVENT_RECEIVED
        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)