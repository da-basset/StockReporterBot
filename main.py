from fmp_requests import get_company_data, get_stock_price
from portfolio_report import gen_portfolio_report

#Global Ticker Count
AMZN_COUNT = 10
AAPL_COUNT = 15
TSLA_COUNT = 1

TICKER_DICT = {
    "AMZN": AMZN_COUNT,
    "AAPL": AAPL_COUNT,
    "TSLA": TSLA_COUNT
}


def main():
    data_list = {}
    for ticker in TICKER_DICT:
        company_data = get_company_data(ticker)
        portfolio_data = gen_portfolio_report(ticker, TICKER_DICT[ticker])
        combined_data = company_data + portfolio_data
        
        data_list[ticker] = combined_data
    print(data_list)

main()
