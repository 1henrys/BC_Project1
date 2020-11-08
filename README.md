### *UCB FinTech Project 1, Team 2: On The Money Alpha Managers*
### *Kris Kish, Henry Schrader, Lawson Deng*
---

# **ON THE MONEY** 
## A Platform for Diversifed Asset Investments and Currency Adjusted Returns


Full Presentation on [Google Slides](https://docs.google.com/presentation/d/1aJsdNW4mfC-DXb_fuXbBhri-1n7bpccKGcNhqPgErqc/edit?usp=sharing).


## Challenge

Retail investors are not offered performance metrics/dashboards that institutional investors have.  They don’t have one place to go to measure or compare asset performance or their portfolio against others.

# The Solution

A one-stop shop dashboard that allows retail investors to input investment ideas and existing holdings and visualize their cumulative return across all assets comparing to their local currency, and against other currency.

# How
 
 We evaluate a user provided list of assets, indexes, or algo portfolios in traditional fashion for daily returns, cumulative returns, 200-day moving avg, 200day standard deviation. 
 
Then to account for fiat currencies devaluation, we evaluate the same user provided list against both London Gold Spot price and Bitcoin to determine a (Asset price in USD / (BTC or USD) ratio). 

Finally, we calculate a Currency Adjusted Return to empower the retail investor to truly evaluate their asset performance versus both a long standing store of value, and versus a modern digital store of value.

 ---
 
Download the Project Repo at [GitHub](https://github.com/1henrys/BC_Project1.git).
 
 
# Main Notebook
 
To run the project, download and run the data_analysis.ipynb Jupyter notebook.
 
 You will also need:
     
   > • eod.py
   
   > • PyViz / Bokeh library
     
Once you run the entire notebook and initiate the .servable connection, open your terminal, navigate to the /notebooks directory on this repo and type:
 
 ```
 panel serve --show data_analysis.ipynb
 ```
 
## Directory Breakdown
 
notebooks : contains all core project notebooks, data analysis and cleaning, and scratch pads.
data_imports : all imported / downloaded static csv data files.
 
## Notebooks Breakdown

There are several types of python and notebook files in the directory.

The first is a list of API connector python and notebook pair files for connecting to the third-party data providers and fetching the required data to be used by the application.

The notebook file is used to test the connection of the API. It can fetch the required data and processes it to the desired format. The corresponding python script will wrap the defined process into a python function, so it can be called by an outside program and return the desired result as a data frame to the caller. Furthermore, it shows some examples of how the function can be called within the python script.

The eod.py python script and its notebook file are used to demonstrate the routine of getting the data from EODhistroicdata.com, a France-based international financial data service provider. It can provide equity/bond index data, bond index data, real estate data, as well as cryptocurrency trading data across multiple markets in the world.

The ms.py script and market.ipynb are used to demonstrate the routine of getting the data from marketstack.com, a US financial data service provider. It can provide equity/bond index and trading data across multiple US exchanges.

The crypto.py script and crypto.ipynb are used to demonstrate the routine of getting the bpi index data from coindesk.com, a Bitcoin information aggregator. It provides a syndicated bitcoin price index to track its EOD trading data across multiple international cryptocurrency exchanges.

The main.py python script is to demonstrate the routine of calling a python function resided in a separate file and obtain the return result.

The second type of python and notebook files, the send_sms files,  are used to connect to a third-party service provider Twilio and provide the SMS service. It can send out SMS messages to pre-verified cellphone numbers with the user-defined content.
  
  
  ### Data Cleaning and Initial Analysis
  
  art_analysis.ipynb
  crypto.ipynb
  edo.ipynb
  gold_analysis.ipynb
  market.ipynb
  real_estate_cleaning.ipynb
  real_estate_analysis.ipynb
  schh.ipynb
  yahoo_analysis.ipynb
  
  ### Data Viz and Panel Scratchpads
  
  data_analysis_viz_scratch.ipynb
  data_analysis_viz.ipynb
  panel_template
  
  ### Scripts
  
  crypto.py
  eod.py
  main.py
  ms.py
  send_sms.py
  
  ### Twilio 
  
  send_sms.ipynb