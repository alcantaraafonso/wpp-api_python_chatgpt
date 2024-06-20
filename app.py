from flask import Flask, request
import util
import whatsapp_service
from util_log import get_logger

app = Flask(__name__)



@app.route('/welcome', methods=['GET'])
def index():
    get_logger().info('testing log message1')
    return "Welcome"

@app.route('/whatsapp', methods=['GET'])
def verify_token():
    try:
        accessToken = "BEGA98721NHAWHAT345SAPP"
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token != None and challenge != None and token == accessToken:
            return challenge
        
        return "", 400
    except Exception as exception:
        get_logger().error("app.verify_token")
        get_logger().error(exception)
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def received_message():
    try: 
        # get_logger().info('entreik no received_nessage')

        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        messages = (value["messages"])[0]
        number = messages["from"]
        message_type = messages["type"]
        message_user = util.get_user_message(message_type, messages)
        # get_logger().info(f'{message_user=}')

        process_messages(message_user, number)

        # deve SEMPRE retornar EVENT_RECEIVED
        return "EVENT_RECEIVED"
    except Exception as e:
        get_logger().error("Exception - app.received_message")
        if hasattr(e, 'message'):
            get_logger().error(e.message)
        else:
            get_logger().error(e)

        return "EVENT_RECEIVED"
@app.route('/healthcheck', methods=['GET'])
def health_check():
    try:
        return "", 204
    
    except:
        return "", 500

def process_messages(text, number):
    try: 
        greeting = ['olá', 'oi', 'opa', 'oie']
        thanking = ['obrigado', 'agradecido', 'brigado', 'valeu']

        if text.lower() in greeting:
            get_logger().info('entre no process_messages')

            data = util.text_message("Olá, como você está?", number)

        elif text.lower() in thanking:
            data = util.text_message("Obrigado por entrar em contato conosco!", number)
        
        else:
            data = util.text_message("Desculpe, não te entendi!", number)    

        whatsapp_service.send_message_whatsapp(data)
    except Exception as e:
        get_logger().error("Exception - app.received_message")
        if hasattr(e, 'message'):
            get_logger().error(e.message)
        else:
            get_logger().error(e)     

# def generate_message(text, number):
#     try:
#         data = util.text_message(number, text)

#         whatsapp_service.send_message_whatsapp(data)
#     except Exception as exception:
#         get_logger().error("app.generate_message")
#         get_logger().error(exception)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)