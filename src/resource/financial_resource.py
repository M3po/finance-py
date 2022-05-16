import falcon
from src.model.financial_model import FinancialModel

class FinancialResource:
    
    def __handleTicker(self, req):
        ticker = req.get_param('ticker')
        if(ticker is None):
            raise falcon.HTTPBadRequest("Missing query parameter 'ticker'")
        return ticker

    def on_get_history(self, req, resp):
        print("history")
        ticker = self.__handleTicker(req)
        financialModel = FinancialModel(ticker)
        fromDate = req.get_param('startDate')
        toDate = req.get_param('endDate')
        resp.body = financialModel.historyData(fromDate, toDate)
        resp.status = falcon.HTTP_200

    def on_get_info(self, req, resp):
        print("info")
        ticker = self.__handleTicker(req)
        print(ticker)
        financialModel = FinancialModel(ticker)
        resp.body = financialModel.info()
        resp.status = falcon.HTTP_200

    def on_get_financials(self, req, resp):
        print("info")
        ticker = self.__handleTicker(req)
        print(ticker)
        financialModel = FinancialModel(ticker)
        resp.body = financialModel.financials()
        resp.status = falcon.HTTP_200    