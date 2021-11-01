class CurrencyStatistics:
    def __init__(self, kwargs):
        self.cur_id = kwargs.get('Cur_ID')
        self.date = kwargs.get('Date')
        self.cur_official_rate = kwargs.get('Cur_OfficialRate')
