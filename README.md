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
  
  
  ### Data Cleaning and Initial Analysis
  
  art_analysis.ipynb
  crypto.ipynb
  edo.ipynb
  market.ipynb
  real_estate_cleaning.ipynb
  real_estate_analysis.ipynb
  schh.ipynb
  
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