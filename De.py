import requests
import time

# Your bot token and chat ID
TOKEN = '6747670042:AAHlP2CSkhFzSs_ahjIuGIKD_8qAPXh1VoA'
CHAT_ID = '5755160640'
MESSAGE = 'This is an hourly message from your bot!'

def send_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == '__main__':
    while True:
        response = send_message(TOKEN, CHAT_ID, MESSAGE)
        print(f'Message sent: {response}')
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)
