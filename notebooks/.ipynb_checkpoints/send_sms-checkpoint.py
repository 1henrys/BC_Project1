{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Under Lock and Key"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You and Harold have developed a Python application that will extract historical stock data from **Quandl** for a given ticker and calculate the Sharpe ratio for that stock. So far, only you two have been using the program, but your manager now wants you to open the application up to the entire team. You know that Quandl allows API calls to be submitted without an API key, but the limit is 50 calls a day. Quandl is diligent in their rate-limiting and keeps services under lock and key.\n",
    "\n",
    "## Instructions\n",
    "\n",
    "### Import the Python `requests`, `os`, and `dotenv` libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "import dotenv\n",
    "import os\n",
    "import json\n",
    "from pathlib import Path\n",
    "import numpy\n",
    "%matplotlib inline\n",
    "from datetime import datetime\n",
    "import dateutil.parser\n",
    "import yfinance\n",
    "from twilio.rest import Client"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use the `load_dotenv()` method from the `dotenv` package to load and export the environment variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dotenv.load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "account_sid = os.environ['TWILIO_ACCOUNT_SID']\n",
    "auth_token = os.environ['TWILIO_AUTH_TOKEN']\n",
    "client = Client(account_sid, auth_token)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use the `os.getenv` function to retrieve the environment variable named `QUANDL_API_KEY`. Store as a Python variable named `api_key`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Concatenate `request_url` with the `api_key` variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dotenv.load_dotenv(dotenv.find_dotenv())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SMe1dd101ece294b98987f9843f4292398\n"
     ]
    }
   ],
   "source": [
    "message = client.messages.create(\n",
    "    to=\"+15512088818\",    # This number has to be a verified number\n",
    "    from_=\"+14084405432\", # Don't change this number.\n",
    "    body=\"Hello from Python!\")\n",
    "\n",
    "print(message.sid)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
