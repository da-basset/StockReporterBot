"""
Utility Library for functions that make requests to Financial Modeling Prep (FMP) API.
"""
import os
import requests
import json

# Global Variables
API_ENDPOINT = "https://financialmodelingprep.com/stable"
API_KEY =  os.getenv("FMP_API_KEY")

def get_company_data(ticker):
    """
    Gets company data from FMP API for a given ticker symbol.

    EndPoint Documentation:
    https://site.financialmodelingprep.com/developer/docs/stable/profile-cik
    """
    company_data_list = []

    # Begin Request
    url = f"{API_ENDPOINT}/profile?symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Append needed data to company_data_list
    company_data_list.append(f"Exchange: {data[0]['exchange']}")
    company_data_list.append(f"IPO Date: {data[0]['ipoDate']}")

    return company_data_list


def get_stock_price(ticker):
    """
    Gets stock price data from FMP API for a given ticker symbol.
    
    EndPoint Documentation:
    https://site.financialmodelingprep.com/developer/docs/stable/quote
    """
    price_data_list = []

    url = f"{API_ENDPOINT}/quote?symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Math calculations
    price_change_since_open = data[0]['price'] - data[0]['open']
    price_change_since_prev_close = data[0]['price'] - data[0]['previousClose']

    # Append needed data to company_data_list
    price_data_list.append(f"Open Price: {data[0]['open']}")
    price_data_list.append(f"Close Price: {data[0]['price']}")
    price_data_list.append(f"Price Change Since Open: {price_change_since_open}")
    price_data_list.append(f"Price Change Since Previous Close: {price_change_since_prev_close}")
    price_data_list.append(f"Previous Day Close: {data[0]['previousClose']}")

    return price_data_list