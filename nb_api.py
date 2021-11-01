import requests
from currency import Currency
from const_for_api import *
from datetime import date
from datetime import timedelta
from currency_statistics import *
import json


class NbApi:
    @staticmethod
    def get_currencies():
        list_currencies = []
        request = requests.get(url=ALL_CURRENCIES)
        for i in range(0, len(request.json())):
            currency_object = Currency(request.json()[i])
            list_currencies.append(currency_object)
        return list_currencies

    @staticmethod
    def get_all_statistics():
        start_date = date.today() - timedelta(days=30)
        end_date = date.today()
        list_statistics = []
        currencies = NbApi.get_currencies()
        print(start_date)
        print(end_date)
        for i in range(0, len(currencies)):
            request = requests.get(url=CURRENT_DYMANICS + str(
                currencies[i].cur_id) + "?startDate=" + str(start_date) + "&endDate=" + str(end_date))
            if len (request.json())!=0:
                for i in range(0,len(request.json())):
                    currency=CurrencyStatistics(request.json()[i])
                    list_statistics.append(currency)
        return list_statistics

    @staticmethod
    def get_statistics_for_currency(cur_id):
        start_date = date.today() - timedelta(days=30)
        end_date = date.today()
        list_statistics = []
        print(start_date)
        print(end_date)
        request = requests.get(url=CURRENT_DYMANICS + str(
                cur_id) + "?startDate=" + str(start_date) + "&endDate=" + str(end_date))
        if len (request.json())!=0:
            for i in range(0,len(request.json())):
                currencys = CurrencyStatistics(request.json()[i])
                list_statistics.append(currencys)
        return list_statistics







