from fmp_requests import get_stock_price

def gen_portfolio_report(ticker, share_count):
    portfolio_data_list = []

    stock_price_data = get_stock_price(ticker)

    portfolio_data_list.append(f"Open Price: {stock_price_data[0]['open']}")
    portfolio_data_list.append(f"Current Price: {stock_price_data[0]['price']}")
    portfolio_data_list.append(f"Total Share Price : {stock_price_data[0]['price'] * share_count}")
    portfolio_data_list.append(f"Daily Share Price Fluctuation: {(stock_price_data[0]['price'] - stock_price_data[0]['open']) * share_count}")

    return portfolio_data_list
