import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

#Class for IB Connection
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    #listen for real-time bars
    def realtimeBar(self, reqId, time, open_, high, low, close,
                        volume, wap, count):
        bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)


#Class for Bot
class Bot:
    ib = None
    def __init__(self):
        #Connection to IB
        self.ib = IBapi()
        self.ib.connect("127.0.0.1", 7497, 1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        #input symbol info
        symbol = input("Enter the symbol you want to trade: ")
        #contract object initialization
        contract = Contract()
        contract.symbol = symbol.upper()
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        #market data
        self.ib.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])
    #seperate thread to listen to socket
    def run_loop(self):
        self.ib.run()
    #pass real-time bar data to bot object
    def on_bar_update(reqId, time, open_, high, low, close,
                        volume, wap, count):
        print(reqId)

bot = Bot()