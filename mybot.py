import settings
# import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Пользователь нажал START')
    update.message.reply_text('Привет! Я — бот-попугай. Почему попугай? А сейчас узнаешь. '
                               'Напиши что-нибудь)')

def talk_to_me(update, context):
    user_text = update.message.text
    print(f'Пользователь: {user_text}')
    if user_text == 'Время':
        current_time = datetime.now()
        update.message.reply_text(current_time.strftime('Сейчас %H:%M'))
    else:
        update.message.reply_text(user_text)


def main():
    
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # logging.info('** БОТ СТАРТОВАЛ **')

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()