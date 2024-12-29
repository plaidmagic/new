import logging
from src.utils import setup_wallet, fetch_market_data, execute_trade

class TradingBot:
    def __init__(self):
        self.wallet = setup_wallet()
        self.market_data = None

    def fetch_data(self):
        self.market_data = fetch_market_data()

    def execute_strategy(self):
        if self.market_data:
            execute_trade(self.wallet, self.market_data)

    def run(self):
        logging.info("Starting trading bot...")
        self.fetch_data()
        self.execute_strategy()