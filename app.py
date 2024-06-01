from flask import Flask, request
import util
import whatsapp_service

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
        entry = body["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]
        message = value["messages"][0]
        number = message["from"]
        message_type = message['type']

        message_user = util.get_user_message(message)
        generate_message(message_type, message_user, number)
        print(f'{message_user=}')

        # deve SEMPRE retornar EVENT_RECEIVED
        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"

# TODO alterar o IF pra usar o type
def generate_message(message_type, text, number):
    if message_type == 'text':
        data = util.text_message(number, text)

    whatsapp_service.send_message_whatsapp(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)