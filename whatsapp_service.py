import requests
import json

def send_message_whatsapp(data):
    try:
        token = "EAAGdQac3cVEBO8DdN9n8a6fYorXjAMybVgC5Vf5WC6fXkyvxsq2R6xhCc7M4fb0QmfzybZCXWvXNsPjpNqsTOuS7ggJLUHdqHo3wba18SKzZC5REdriKROsGpiZAaibsUOy0ZCyq0YZBuCetFCh1vks6k8ZCZAJmJQrJKVdqRhVfxkvPBIoXNdbj0UOOZAxesrJm"
        api_url = "https://graph.facebook.com/v19.0/272679455939616/messages"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        response = requests.post(api_url, data = json.dumps(data), headers= headers)

        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False