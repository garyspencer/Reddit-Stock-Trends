import StockTrends
import Portfolio

scraper = StockTrends.StockTrends()

portfolio = Portfolio.Portfolio()
portfolio.load_portfolios()

for p_name in portfolio.get_portfolios():
    tickers = portfolio.get_tickers(p_name)
    print (p_name, tickers)

# def get_data (with_finance=False, with_stats=False)
data = scraper.get_data()
portfolio.crupdate_portfolio_from_scraper_frames("scrape_latest", data)

print(data)
