import os
import configparser

class Portfolio:
    def __init__(self):
        self.config = None
        self.config_path = "./config/portfolios.ini" # default value ?

    def load_portfolios(self, config_path:str='./config/portfolios.ini'): # another default value lol
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 
            config_path)
        self.config.read(self.config_path)
    
    def add_portfolio(self, name:str, ticker_symbols:str = ""):
        if not self.portfolio_exists(name):
            #print ("Adding portfolio [" + name + "]!")
            self.config["Portfolios"][name] = ticker_symbols
            self.write_portfolio()
        else:
            pass
            #print ("portfolio " + name + " already exists")

    def portfolio_exists(self, name: str):
        return name in self.config["Portfolios"]
        
    def get_portfolios(self):
        return self.config["Portfolios"]
    
    def get_tickers(self, portfolio_name:str):
        if self.portfolio_exists(portfolio_name):
            return self.get_portfolios()[portfolio_name].split(",")
        else:
            print ("Could not retrieve tickers. Portfolio [" + portfolio_name + "] did not exist.")
        
    def write_portfolio(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
    
    def print_portfolio_names(self):
        print("------------------------------.")
        print("portfolios:".ljust( 30, ' ') + ":")
        for f in self.get_portfolios():
            print((" " + f).ljust( 30, ' ') + ":")
        print("------------------------------'")

    def crupdate_portfolio_from_scraper_frames(self, portfolio_name:str, scraper_data):
            tickers = self.do_stuff_with_scraper_data(scraper_data)
            self.update_portfolio(portfolio_name, tickers, force_update=True)
    
    def update_portfolio(self, portfolio_name:str, tickers:str, force_update:bool=False):
        
        self.compare_portfolio (portfolio_name, tickers)
        
        if self.portfolio_exists(portfolio_name) or force_update == True:
            self.config["Portfolios"][portfolio_name] = tickers
            self.write_portfolio()

    def add_ticker(self, portfolio_name:str, ticker:str):
        if self.portfolio_exists(portfolio_name):
            tickers = self.get_tickers(portfolio_name)

            if ticker in tickers:
                print("Ticker already Existed")
            else:
                tickers.push(ticker)
                self.update_portfolio(portfolio_name,",".join(tickers))
        else:
            print ("Could not add ticker - Portfolio [" + portfolio_name + "] does not exist.")

    def do_stuff_with_scraper_data (self, scraper_data):
        print("Doing stuff to scraper data...")
        return "THIS,IS,A,TEST"

    def compare_portfolio(self, portfolio_name, tickers):
        print ("Comparing portfolio before updating...")


# def main():
#     portfolios = Portfolio()
#     portfolios.load_portfolios()
#     #for port in portfolios.get_portfolios():
#         #tickers = portfolios.get_tickers(port)
#         #print (port, tickers)

# if __name__ == "__main__":
#     main()