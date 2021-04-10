import pandas as pd
from binance_f.impl.utils.timeservice import maybe_convert_timestamp_to_datetime

class FundingRate:

    def __init__(self):
        self.symbol = ""
        self.fundingRate = 0.0
        self.fundingTime = 0
    
    @staticmethod
    def json_parse(json_data):
        result = FundingRate()
        result.symbol = json_data.get_string("symbol")
        result.fundingRate = json_data.get_float("fundingRate")
        result.fundingTime = json_data.get_int("fundingTime")

        return result

    def to_pandas(self, to_datetime):
        res = pd.Series({
            'symbol': self.symbol,
            'fundingRate': self.fundingRate,
            'fundingTime': maybe_convert_timestamp_to_datetime(self.fundingTime, to_datetime)
        })
        return res
