"""
Utility Library for functions that make requests to Financial Modeling Prep (FMP) API.
"""
import os
import requests
import json

# Global Variables
API_ENDPOINT = "https://financialmodelingprep.com/stable"
API_KEY =  os.getenv("FMP_API_KEY")
TICKER_LIST = ["AMZN"] #["AMZN", "AAPL", "TSLA"]


def get_company_data(ticker):
    """
    Gets company data from FMP API for a given ticker symbol.

    EndPoint Documentation:
    https://site.financialmodelingprep.com/developer/docs/stable/profile-cik
    """
    # Begin Request
    url = f"{API_ENDPOINT}/profile?symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # grabbing needed fields only
    if "companyName" or "exchange" or "ipoDate" in data[0]:
        return {
            "companyName": data[0]["companyName"],
            "exchange": data[0]["exchange"],
            "ipoDate": data[0]["ipoDate"]
        }
    return []


def get_stock_price(ticker):
    """
    Gets stock price data from FMP API for a given ticker symbol.
    
    EndPoint Documentation:
    https://site.financialmodelingprep.com/developer/docs/stable/quote
    """

    url = f"{API_ENDPOINT}/quote?symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # grabbing needed fields only
    if "price" or "dayLow" or "dayHigh" or "open" or "previousClose" in data[0]:
        return {
            "Open Price": data[0]["open"],
            "Close Price": data[0]["price"],
            "Price Change Since Open": data[0]["price"] - data[0]["open"],
            "Price Change Since Previous Close": data[0]["price"] - data[0]["previousClose"],
            "Previous Day Close": data[0]["previousClose"]
        }