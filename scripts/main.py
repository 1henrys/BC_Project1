from crypto import *
start_date = '2012-01-01'
end_date = '2020-11-10'

bpi_df = get_bpi(start_date, end_date)
print(bpi_df)