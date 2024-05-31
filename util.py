def get_text_user(message):
    text = ''
    type_message = message['type']

    if type_message == 'text':
        return (message['text'])['body']

    return 'sem mensagem'