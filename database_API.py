import pandas as pd
from datetime import date
import os
import json

class allRidesDB():
    
    def __init__(self , db_config_path = 'db_format.json'):
        
        with open (db_config_path) as json_file:
            self.config = json.load(json_file)

        self.db_fields = {field['name'] for field in self.config['db_fields']}
        self.mandatory_fields = {field['name'] for field in self.config['db_fields'] if field['mandatory']}
        print(self.db_fields)
        self.csv_path = 'allRidesDB_' + date.today().strftime("%Y_%m_%d") + '.csv'
        
        if os.path.exists(self.csv_path):
            self.df = pd.read_csv(self.csv_path)
        
        else:
            self.df = pd.DataFrame(columns = self.db_fields)
            
        print(self.df)

    def add_Ride(self , record):
        assert self.mandatory_fields.issubset(record.keys())
        self.df = pd.concat([self.df,record])
        

    def remove_Ride(self):
        pass

if __name__ == "__main__":
    print(allRidesDB().mandatory_fields)