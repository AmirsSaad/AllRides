# -*- coding: UTF8 -*-
import requests
import datetime


class BotHandler:
    def __init__(self, token):
            self.token = token
            # self.api_url = "https://api.telegram.org/bot{}/".format(token)
            self.api_url = 'https://api.telegram.org/bot991813369:AAFvJEvI46yf28LwXfGIirsJTCOXfHmqw_4/getUpdates'

            self.updates = list()
            self.new_updates = list()

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        # method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url, params)
        result_json = resp.json()['result']
        
        # updates is a list of unique (by "update_id") Telegram updates: concat and remove duplicates
        self.new_updates = [v for v in result_json if v['update_id'] not in [upd["update_id"] for upd in self.updates]]
        self.updates.append(result_json)
        self.updates = list({v['update_id']:v for v in self.updates}.values())


        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post('https://api.telegram.org/bot991813369:AAFvJEvI46yf28LwXfGIirsJTCOXfHmqw_4/sendMessage', params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update





