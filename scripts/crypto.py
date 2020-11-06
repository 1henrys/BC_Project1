import pandas as pd
import requests
import dotenv
import os
import json
from pathlib import Path
import numpy
import datetime
from datetime import datetime
import dateutil.parser
import urllib.request


def get_bpi(start_date, end_date):
    date_range = {'start': start_date, 'end': end_date}

    request_url = "https://api.coindesk.com/v1/bpi/historical/close.json"

    response_data = requests.get(request_url, date_range)
    data = response_data.json()
    bpi_list = data["bpi"]

    bpi_df = pd.DataFrame.from_dict(bpi_list, orient='index', columns=['BPI_Closing'])
    bpi_df.index.name = 'Date'

    bpi_df = bpi_df.reset_index()
    bpi_df['Date'] = pd.to_datetime(bpi_df['Date'], format='%Y-%m-%d')
    bpi_df['Asset'] = "Crypto Index"

    bpi_df = bpi_df.set_index(['Date'])
    bpi_df = bpi_df[['Asset', 'BPI_Closing']]
    bpi_df = bpi_df.sort_index()

    return bpi_df


start_date = '2012-01-01'
end_date = '2020-11-10'

bpi_df = get_bpi(start_date, end_date)
print(bpi_df)