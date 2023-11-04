import telebot
import requests
import io
from telebot import types


bot = telebot.TeleBot('6309248314:AAFXkFSlPHl8ynW00LLoDNnJBxwGoctCBeY')


CHANNEL_USERNAME = 'lxbadboy'


welcome_message = "🌟 Welcome to the Image to URL bot! 🌟 Send an image, and I'll provide you with a URL for it. 😄"


def is_user_member_of_channel(user_id, channel_username):
    try:
        chat_member = bot.get_chat_member(chat_id='@' + channel_username, user_id=user_id)
        return chat_member.status in ('member', 'administrator', 'creator')
    except Exception as e:
        return False

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_user_member_of_channel(user_id, CHANNEL_USERNAME):
        bot.send_message(message.chat.id, welcome_message)
    else:
        bot.send_message(message.chat.id, "To use this bot, you must join our channel first. 📢")
        bot.send_message(message.chat.id, f"Join @{CHANNEL_USERNAME} and then come back! 👥")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
       
        photo = message.photo[-1]

 
        file_info = bot.get_file(photo.file_id)
        image_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'


        image_response = requests.get(image_url)
        image_data = image_response.content

     
        image_file = io.BytesIO(image_data)

 
        formData = {'file': ('image.jpg', image_file)}

    
        telegraph_response = requests.post('https://telegra.ph/upload', files=formData)

    
        photo_url = telegraph_response.json()[0]['src']


        bot.send_message(message.chat.id, f'🔗 Image URL: https://telegra.ph{photo_url}')
    except Exception as e:
        bot.send_message(message.chat.id, f'❌ Error: {e}')


if __name__ == '__main__':
    bot.polling()
