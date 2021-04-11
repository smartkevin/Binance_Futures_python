import pandas as pd
from binance_f.impl.utils.timeservice import maybe_convert_timestamp_to_datetime

DATA_COLUMNS = [
    'openTime', 'open', 'high', 'low', 'close', 'ignore1', 
    'closeTime', 'ignore2', 'count', 'ignore3', 'ignore4', 'ignore5'
]

class MarkPriceKlines:
    # GET /fapi/v1/indexPriceKlines
    def __init__(self):
        for c in DATA_COLUMNS:
            setattr(self, c, 0)

    @staticmethod
    def json_parse(json_data):
        result = MarkPriceKlines()
        val = json_data.convert_2_list()
        for i, c in enumerate(DATA_COLUMNS):
            setattr(result, c, val[i])  
        return result

    def to_pandas(self, as_datetime):
        res = pd.Series({
            'openTime': maybe_convert_timestamp_to_datetime(self.openTime, as_datetime),            
            'closeTime': maybe_convert_timestamp_to_datetime(self.closeTime, as_datetime),
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'count': self.count,
        })
        return res