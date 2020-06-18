from bothandler import BotHandler
from database_API import allRidesDB

token = '991813369:AAFvJEvI46yf28LwXfGIirsJTCOXfHmqw_4' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name
def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']

                if 'message' not in current_update.keys():
                    continue

                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'Hi':
                    magnito_bot.send_message(first_chat_id, 'Morning ' + first_chat_name)
                    new_offset = first_update_id + 1
                else:
                    magnito_bot.send_message(first_chat_id, 'How are you doing '+first_chat_name)
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()