import StockTrends
import Portfolio

scraper = StockTrends.StockTrends()
portfolio = Portfolio.Portfolio()
portfolios = Portfolio.Portfolio()
portfolios.load_portfolios()

for p_name in portfolios.get_portfolios():
    tickers = portfolios.get_tickers(p_name)
    print (p_name, tickers)

# def get_data (with_finance=False, with_stats=False)
data = scraper.get_data()


print(data)
