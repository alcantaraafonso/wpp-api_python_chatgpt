
def get_text_message(message):
    return message['text']['body']

def get_interactive_object(message):
    interactive_object = message['interactive']
    type_interactive = interactive_object['type']

    if type_interactive == 'button_reply':
        return interactive_object['button_reply']['title']
    elif type_interactive == 'list_reply':
        return interactive_object['list_reply']['title']

def get_user_message(message_type, message):

    if message_type == 'text':
        return get_text_message(message)
    elif message_type == 'interactive':
        return get_interactive_object(message)

    return 'sem mensagem'

def text_message(text, number):
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

def buttons_message(number):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Escolha"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "001",
                                "title": "Sim"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "002",
                                "title": "Não"
                            }
                        }
                    ]
                }
            }
        }

def list_message(number):
    return {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "✅ I have these options"
                },
                "footer": {
                    "text": "Select an option"
                },
                "action": {
                    "button": "See options",
                    "sections": [
                        {
                            "title": "Buy and sell products",
                            "rows": [
                                {
                                    "id": "main-buy",
                                    "title": "Buy",
                                    "description": "Buy the best product your home"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Sell",
                                    "description": "Sell your products"
                                }
                            ]
                        },
                        {
                            "title": "📍center of attention",
                            "rows": [
                                {
                                    "id": "main-agency",
                                    "title": "Agency",
                                    "description": "Your can visit our agency"
                                },
                                {
                                    "id": "main-contact",
                                    "title": "Contact center",
                                    "description": "One of our agents will assist you"
                                }
                            ]
                        }
                    ]
                }
            }
        }