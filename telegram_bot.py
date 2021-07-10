import telegram


telegram_token = '1633525793:AAHCo8pV9dDFBA8hsbM1gEHL96vgGe2E8PM'
chat_id = '-1001450410896'


def send_message_list(msg_list):
    bot = telegram.Bot(token=telegram_token)
    for msg in msg_list:
        bot.sendMessage(chat_id=chat_id, text=msg)
