import json
import yfinance as yf


class FinancialModel:
    
    def __init__(self, ticker):
        self.tick = yf.Ticker(ticker)
        
    def historyData(self,start, end):
        history = self.tick.history(start=start,end=end)
        return history.to_json() 
    def info(self):
        info = self.tick.info
        return json.dumps(self.tick.info)
    def financials(self):
        financials = self.tick.financials
        return financials.to_json()     

22