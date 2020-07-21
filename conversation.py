import os
import pandas as pd
import json

class Conversation():

    def __init__(self , user_id , db_config_path = r"C:\Users\amirsaa\Documents\GitHub\AllRides\db_format.json"):
        print('Hello user: {}'.format(user_id))
        
        with open (db_config_path) as json_file:
            self.config = json.load(json_file)
        

        self.csv_path = 'user_id.csv'
        self.user_id = user_id
        self.fields = self.config['db_fields']
        self.curr_field = self.fields.pop(0)
        self.ride = {}
        if os.path.exists(self.csv_path):
            self.df = pd.read_csv(self.csv_path)
        
        else:
            self.df = pd.DataFrame()

        print(self.curr_field['request_string']) 

    def get_message(self,message):
        self.ride.update({self.curr_field['name'] : message})
        self.curr_field = self.fields.pop(0)
    
    def post_message(self):
        print(self.curr_field['request_string']) 

    
        

    def ask_question(self):
        pass
    
    def get_answer(self):
        pass


