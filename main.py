from fmp_requests import get_company_data, get_stock_price

TICKER_LIST = ["AMZN", "AAPL", "TSLA"]

def main():
    data_list = {}
    for ticker in TICKER_LIST:
        company_data = get_company_data(ticker)
        price_data = get_stock_price(ticker)
        data_list[ticker] = {
            "company_data": company_data,
            "price_data": price_data
        }
    print(data_list)

main()