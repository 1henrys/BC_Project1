from eod import *
start_date = '2010-01-01'

#symbols = 'SP500BDT.INDX'  #S&P500 Bond Index
#symbols = 'GSPC.INDX'       #S&P500 Index
#symbols = 'BCOMGCTR.INDX'   #Gold Total Return Index
#symbols = 'BTC-USD.CC'     #Bitcoin EOD Price
symbols = 'GC.COMM'         #Gold EOD Price

eod_df = get_data(symbols, start_date)
print(eod_df)