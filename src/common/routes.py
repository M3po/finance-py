from src.resource.financial_resource import FinancialResource
import src.common.constants as constants


class Router:
    apiVer = '/' + constants.API_VERSION

    def __generateFinancialRoute(self, path, app):
        route = self.apiVer + '/' + constants.FINANCE_ROUTE + '/' + path
        app.add_route(route , FinancialResource(), suffix=path)


    def __init__(self, app):
        self.__generateFinancialRoute('history', app)
        self.__generateFinancialRoute('info', app)
        self.__generateFinancialRoute('financials', app)