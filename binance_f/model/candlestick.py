import pandas as pd
from binance_f.impl.utils.timeservice import maybe_convert_timestamp_to_datetime

class Candlestick:

    def __init__(self):
        self.openTime = 0
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = 0.0
        self.closeTime = 0
        self.quoteAssetVolume = 0.0
        self.numTrades = 0
        self.takerBuyBaseAssetVolume = 0.0
        self.takerBuyQuoteAssetVolume = 0.0
        self.ignore = 0.0

    @staticmethod
    def json_parse(json_data):
        result = Candlestick()
        val = json_data.convert_2_list()
        result.openTime = val[0]
        result.open = val[1]
        result.high = val[2]
        result.low = val[3]
        result.close = val[4]
        result.volume = val[5]
        result.closeTime = val[6]
        result.quoteAssetVolume = val[7]
        result.numTrades = val[8]
        result.takerBuyBaseAssetVolume = val[9]
        result.takerBuyQuoteAssetVolume = val[10]
        result.ignore = val[11]
  
        return result

    def to_pandas(self, as_datetime):
        res = pd.Series({
            'openTime': maybe_convert_timestamp_to_datetime(self.openTime, as_datetime),
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume,
            'closeTime': maybe_convert_timestamp_to_datetime(self.closeTime, as_datetime),
            'quoteAssetVolume': self.quoteAssetVolume,
            'numTrades': self.numTrades,
            'takerBuyBaseAssetVolume': self.takerBuyBaseAssetVolume,
            'takerBuyQuoteAssetVolume': self.takerBuyQuoteAssetVolume,
            'ignore': self.ignore,
        })
        return res