from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    print('Вызван /start')

def main():
    mybot = Updater("866496947:AAFlEBYTxppRqb77BzRML3mj7faL7fN-QTw", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))

    mybot.start_polling()
    mybot.idle()

main()
