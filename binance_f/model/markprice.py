import pandas as pd
from binance_f.impl.utils.timeservice import maybe_convert_timestamp_to_datetime

class MarkPrice:

    def __init__(self):
        self.symbol = ""
        self.markPrice = 0.0
        self.lastFundingRate = 0.0
        self.nextFundingTime = 0
        self.time = 0
    
    @staticmethod
    def json_parse(json_data):
        result = MarkPrice()
        result.symbol = json_data.get_string("symbol")
        result.markPrice = json_data.get_float("markPrice")
        result.lastFundingRate = json_data.get_float("lastFundingRate")
        result.nextFundingTime = json_data.get_int("nextFundingTime")
        result.time = json_data.get_int("time")

        return result

    def to_pandas(self, as_datetime=False):
        res = pd.Series({
            'symbol': self.symbol,
            'markPrice': self.markPrice,
            'lastFundingRate': self.lastFundingRate,
            'nextFundingTime': maybe_convert_timestamp_to_datetime(self.nextFundingTime, as_datetime),
            'time': maybe_convert_timestamp_to_datetime(self.time, as_datetime)
        })
        return res
