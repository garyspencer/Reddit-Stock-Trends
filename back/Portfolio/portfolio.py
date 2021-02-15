import os
import configparser

class Portfolio:
    config = None
    config_path = "./config/portfolios.ini" # default value ?

    def load_portfolios(self, config_path:str='./config/portfolios.ini'): # another default value lol
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 
            config_path)
        self.config.read(self.config_path)
    
    def add_portfolio(self, name:str, ticker_symbols:str = ""):
        if not self.portfolio_exists(name):
            print ("Adding fund [" + name + "]!")
            self.config["Portfolios"][name] = ticker_symbols
            self.write_portfolio()
        else:
            print ("fund " + name + " already exists")

    def portfolio_exists(self, name: str):
        return name in self.config["Portfolios"]
        
    def get_portfolios(self):
        return self.config["Portfolios"]
    
    def get_tickers(self, portfolio_name:str):
        if self.portfolio_exists(portfolio_name):
            return self.get_portfolios()[portfolio_name].split(",")
        else:
            print ("Fund " + portfolio_name + " did not exist.")
        
    def write_portfolio(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
    
    def print_portfolio_names(self):
        print("------------------------------.")
        print("FUNDS:".ljust( 30, ' ') + ":")
        for f in self.get_portfolios():
            print((" " + f).ljust( 30, ' ') + ":")
        print("------------------------------'")

def main():
    portfolios = Portfolio()
    portfolios.load_portfolios()
    for port in portfolios.get_portfolios():
        tickers = portfolios.get_tickers(port)
        print (port, tickers)

if __name__ == "__main__":
    main()