from bothandler import BotHandler
from database_API import allRidesDB
from conversation import Conversation


def main():
    bot = BotHandler(token = '991813369:AAFvJEvI46yf28LwXfGIirsJTCOXfHmqw_4')
    new_offset = 0
    
    print('hi, now launching...')
    conversations = dict()

    while True:
        bot.get_updates(new_offset)

        for update in bot.new_updates:
            user_id  = update['message']['from']['id']
            if user_id not in conversations.keys():
                conversations.update({user_id : Conversation(user_id)})
            else:
                conversations[user_id].get_message(update['message'])
                conversations[user_id].post_message()
            
        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()