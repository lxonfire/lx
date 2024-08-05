import requests
import time
from colorama import Fore, Style, init

# Initialize colorama
init(convert=True)

# Your bot token and chat ID
TOKEN = '6747670042:AAHlP2CSkhFzSs_ahjIuGIKD_8qAPXh1VoA'  # Replace with your actual bot token
CHAT_ID = 5755160640    # Replace with your actual chat ID
MESSAGE = 'This is an hourly message from your bot!'

def send_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error sending message: {e}{Style.RESET_ALL}")
        return None

if __name__ == '__main__':
    while True:
        response = send_message(TOKEN, CHAT_ID, MESSAGE)
        
        if response and response.get("ok"):
            print(f'{Fore.GREEN}Message sent successfully!{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Failed to send message.{Style.RESET_ALL}')
        
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)
