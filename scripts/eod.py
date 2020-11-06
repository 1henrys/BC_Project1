import pandas as pd
import requests
import dotenv
import os
import json
from pathlib import Path
import numpy
from datetime import datetime
import dateutil.parser


def get_data(symbols, start_date):
    symbols_dict = {'SP500BDT.INDX':'S&P500 Bond Index', 
                    'GSPC.INDX':'S&P500 Index', 
                    'BCOMGCTR.INDX':'Gold Total Return Index', 
                    'BTC-USD.CC':'Bitcoin EOD Price', 
                    'GC.COMM':'Gold EOD Price',}
    
    dotenv.load_dotenv()
    eod_api_key = os.getenv("EOD_API_KEY")
    eod_option = {'api_token': eod_api_key, 'order': 'd', 'fmt': 'json', 'from': start_date}

    eod_request_url = "https://eodhistoricaldata.com/api/eod/" + symbols

    # Execute get request
    eod_response_data = requests.get(eod_request_url, eod_option)
    eod_data = eod_response_data.json()
    #print(json.dumps(data, indent=4))

    column_list = ['Date', 'Asset', 'AdjClosePrice']
    eod_df = pd.DataFrame(columns=column_list)

    for dict in eod_data: 
        for list in dict: 
            if list == "date":
                temp_date = datetime.strptime(dict[list], '%Y-%m-%d')
            elif list == "adjusted_close":
                temp_close = dict[list] 
            
        new_row = {'Date':temp_date, 'Asset':symbols_dict[symbols], 'AdjClosePrice':temp_close}
        eod_df = eod_df.append(new_row, ignore_index=True)                 
    
    eod_df = eod_df.set_index(['Date']) 
    eod_df = eod_df.sort_index()
    return eod_df

#start_date = '2010-01-01'

#symbols = "SP500BDT.INDX"

#symbols = "GSPC.INDX"

#symbols = "BCOMGCTR.INDX"

#symbols = "BTC-USD.CC"

#symbols = "GC.COMM"


#eod_df = get_data(symbols, start_date)
#print(eod_df)