import pandas as pd
import requests
import dotenv
import os
import json
from pathlib import Path
import numpy
from datetime import datetime
import dateutil.parser


def get_data(symbols, asset_type):
    dotenv.load_dotenv()
    ms_api_key = os.getenv("MARKETSTACK_API_KEY")
    ms_api_options = {'symbols': symbols, 'access_key': ms_api_key, 'limit': '3000'}

    ms_request_url = "https://api.marketstack.com/v1/eod"

    # Execute get request
    ms_response_data = requests.get(ms_request_url, ms_api_options)
    ms_data = ms_response_data.json()
    #print(json.dumps(data, indent=4))
    ms_list = ms_data["data"]

    column_list = ['date', 'adj_closing', 'asset_type']
    ms_df = pd.DataFrame(columns=column_list)

    for dict in ms_list: 
        for list in dict: 
            if list == "date":
                temp_date = str(dateutil.parser.parse(dict[list]).date())
                temp_date = datetime.strptime(temp_date, '%Y-%m-%d')
            elif list == "adj_close":
                temp_close = dict[list] 
            
        new_row = {'date':temp_date, 'adj_closing':temp_close, 'asset_type':asset_type}
        ms_df = ms_df.append(new_row, ignore_index=True)                 
    
    ms_df = ms_df.set_index(['date'])  
    return ms_df



symbols = 'GSPC.INDX'
asset_type = "S&P 500 Index"

#symbols = 'SCHH'
#asset_type = "Bond Index"

ms_df = get_data(symbols, asset_type)
print(ms_df)