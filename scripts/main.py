from eod import *
start_date = '2010-01-01'

#symbols = 'SP500BDT.INDX'  #S&P500 Bond Index
#symbols = 'GSPC.INDX'       #S&P500 Index
#symbols = 'BCOMGCTR.INDX'   #Gold Total Return Index
#symbols = 'BTC-USD.CC'     #Bitcoin EOD Price
#ymbols = 'GC.COMM'         #Gold EOD Price
#symbols = 'SCHH.US'        #Charles Schwab ETF EOD Price
#symbols = 'VNQ.US'        #Vanguard Real Estate ETF EOD Price
symbols = 'FDN.US'          #First Trust Dow Jones Internet Index ETF EOD Price

eod_df = get_data(symbols, start_date)
print(eod_df)