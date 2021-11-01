import cx_Oracle
from const_for_api import *
import requests
from currency import Currency
from currency_statistics import *
from nb_api import NbApi
import random
''' colnames = curs.description
        for i in range(0, len(colnames)):
            print(colnames[i][0])
'''


class DbTools:
    @staticmethod
    def add_currency_to_db(currency):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = (
                'INSERT INTO CURRENCY (CUR_ID,CUR_PARENT_ID,CUR_CODE,CUR_ABBREVIATION,CUR_NAME,CUR_NAME_BEL,CUR_NAME_ENG,CUR_QUOT_NAME,CUR_QUOT_NAME_BEL,CUR_QUOT_NAME_ENG,CUR_NAME_MULTI,CUR_NAME_BEL_MULTI,CUR_NAME_ENG_MULTI,CUR_SCALE,CUR_PERIODICITY,CUR_DATE_START,CUR_DATE_END) VALUES (\'' + str(
            currency.cur_id) + '\',\'' + str(currency.cur_parent_id) + '\',\'' + str(
            currency.cur_code) + '\',\'' + str(currency.cur_abbreviation) + '\',\'' + str(
            currency.cur_name) + '\',\'' + str(currency.cur_name_bel).replace("'", "") + '\',\'' + str(
            currency.cur_name_eng) + '\',\'' + str(currency.cur_quot_name) + '\',\'' + str(
            currency.cur_quot_name_bel).replace("'", "") + '\',\'' + str(
            currency.cur_quot_name_eng) + '\',\'' + str(currency.cur_name_multi) + '\',\'' + str(
            currency.cur_name_bel_multi).replace("'", "") + '\',\'' + str(
            currency.cur_name_eng_multi) + '\',\'' + str(currency.cur_scale) + '\',\'' + str(
            currency.cur_periodicity) + '\',\'' + str(currency.cur_date_start) + '\',\'' + str(
            currency.cur_date_end) + '\')')
        curs.execute(sql_req)
        conn.commit()
        conn.close()

    @staticmethod
    def add_all_currencies(request):
        for i in range(0, len(request.json())):
            currencys = Currency(request.json()[i])
            DbTools.add_currency_to_db(currencys)

    @staticmethod
    def add_statistics_to_db(currency_statistics):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('INSERT INTO CURRENCY_STATISTICS (CUR_ID,CUR_DATE,CUR_OFFICIAL_RATE) VALUES (\'' + str(
            currency_statistics.cur_id) + '\',\'' + str(currency_statistics.date) + '\',\'' + str(
            currency_statistics.cur_official_rate) + '\')')
        curs.execute(sql_req)
        conn.commit()
        conn.close()

    @staticmethod
    def add_all_statistics_to_db(list_statistics=NbApi.get_all_statistics()):
        for i in range(0, len(list_statistics)):
            DbTools.add_statistics_to_db(list_statistics[i])
    @staticmethod
    def get_currency_from_db():
        result_list=[]
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY_STATISTICS')
        for row in  curs.execute(sql_req):
            print(row[0],row[1],row[3])
        conn.close()
        return result_list

    @staticmethod
    def get_random_currency_statistics():
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY_STATISTICS')
        for row in curs.execute(sql_req):
            result_list.append(row[0])
        conn.close()
        return random.choice(result_list)

