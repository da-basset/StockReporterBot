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

    # Append needed data to company_data_list
    return data