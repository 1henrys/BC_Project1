import pandas as pd
import requests
import dotenv
import os
import json
from pathlib import Path
import numpy
from datetime import datetime
import dateutil.parser


def get_data(symbols):
    symbols_dict = {'GSPC.INDX':'S&P500 Index', 'SCHH':'SCHH REIT POD Price',}
    
    dotenv.load_dotenv()
    ms_api_key = os.getenv("MARKETSTACK_API_KEY")
    ms_api_options = {'symbols': symbols, 'access_key': ms_api_key, 'limit': '3000'}

    ms_request_url = "https://api.marketstack.com/v1/eod"

    # Execute get request
    ms_response_data = requests.get(ms_request_url, ms_api_options)
    ms_data = ms_response_data.json()
    #print(json.dumps(data, indent=4))
    ms_list = ms_data["data"]

    column_list = ['Date', 'Asset', 'AdjClosePrice']
    ms_df = pd.DataFrame(columns=column_list)

    for dict in ms_list: 
        for list in dict: 
            if list == "date":
                temp_date = str(dateutil.parser.parse(dict[list]).date())
                temp_date = datetime.strptime(temp_date, '%Y-%m-%d')
            elif list == "adj_close":
                temp_close = dict[list] 
                
        new_row = {'Date':temp_date, 'Asset':symbols_dict[symbols], 'AdjClosePrice':temp_close}
        ms_df = ms_df.append(new_row, ignore_index=True)                 
    
    ms_df = ms_df.set_index(['Date']) 
    ms_df = ms_df.sort_index()
    return ms_df


#symbols = 'GSPC.INDX'

#symbols = 'SCHH'

#ms_df = get_data(symbols)
#print(ms_df)