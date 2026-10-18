import telebot

BOT_TOKEN = '8497304663:AAEnY3iB7COdfMgB6N0bQ0UIWCrdeFMtgIU'
CHANNEL_ID = -1004463915590

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "пользователь"
    
    try:
        invite_link_object = bot.create_chat_invite_link(
            chat_id=CHANNEL_ID, 
            creates_join_request=True
        )
        channel_link = invite_link_object.invite_link
    except Exception:
        channel_link = "https://t.me..."

    first_text = f"Привет, {user_name}, чтобы войти на канал отправьте заявку: {channel_link}"
    second_text = "Важно: если владелец канала долго не принимает заявку, то он просто занят и не может найти время чтобы принять вашу заявку, ожидайте."
    
    bot.send_message(message.chat.id, first_text)
    bot.send_message(message.chat.id, second_text)

bot.infinity_polling()
