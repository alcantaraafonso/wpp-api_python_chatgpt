def get_text_message(message):
    return message['text']['body']

def get_interactive_object(message):
    interactive_object = message['interactive']
    type_interactive = interactive_object['type']

    if type_interactive == 'button_reply':
        return interactive_object['button_reply']['title']
    elif type_interactive == 'list_reply':
        return interactive_object['list_reply']['title']

def get_user_message(message):
    type_message = message['type']

    if type_message == 'text':
        return get_text_message(message)
    elif type_message == 'interactive':
        return get_interactive_object(message)

    return 'sem mensagem'

def text_message(number, text):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": text
            }
        }   

def text_format_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": "*msg texto de teste* \n _oi usuário_ - ~ola usuário~ \n ```até usuário```"
            }
        }  

def text_format_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": "*msg texto de teste* \n _oi usuário_ - ~ola usuário~ \n ```até usuário```"
            }
        }  

def image_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "image",
            "image": {
                "link": ""
            }
        }

def audio_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "audio",
            "audio": {
                "link": ""
            }
        }

def video_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "video",
            "video": {
                "link": ""
            }
        }

def document_message(number):
    return {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "document",
            "document": {
                "link": ""
            }
        }

def location_message(number):
    return {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "location",
            "location": {
                "latitude": "-33.44315362206545",
                "longitude": "-70.65355722839423",
                "name": "Centro Cultural La Moneda",
                "address": "Citizenship Square 26, Santiago de Chile. Metro La Moneda, Santiago, Región Metropolitana, Chile"
            }
        }