"""
8
2017-01-03,16:18:50,AAPL,142.64
2017-01-03,16:25:22,AMD,13.86
2017-01-03,16:25:25,AAPL,141.64
2017-01-03,16:25:28,AMZN,845.61
2017-01-03,16:28:50,AAPL,140.64
2017-01-03,16:29:59,FB,140.34
2017-01-04,16:29:32,AAPL,143.64
2017-01-04,16:30:50,AAPL,141.64


Trading Day = 2017-01-03
Last Quote Time = 16:29:59
Number of valid quotes = 6
Most active hour = 16
Most active symbol = AAPL
2017-01-03 16:28:50,AAPL,142.64,140.64
2017-01-03 16:25:22,AMD,13.86,13.86
2017-01-03 16:25:28,AMZN,845.61,845.61
2017-01-03 16:29:59,FB,140.34,140.34
Trading Day = 2017-01-04
Last Quote Time = 16:29:32
Number of valid quotes = 1
Most active hour = 16
Most active symbol = AAPL
2017-01-04 16:29:32,AAPL,143.64,143.64
"""
import itertools
import statistics


class DayTrade(object):
    def __init__(self, trading_date, day_trades):
        self.trading_date = trading_date
        self.day_trades = [trade for trade in day_trades]
        self.last_quote = self.day_trades[-1][1]
        self.valid_quotes = len(self.day_trades)
        self.most_active_hour = statistics.mode([trade[1].split(':')[0] for trade in self.day_trades])
        self.most_active_symbol = statistics.mode([trade[2] for trade in self.day_trades])

    def report(self):
        day_trades = sorted(self.day_trades, key=lambda x: x[2])
        group_by_symbol = itertools.groupby(day_trades, lambda x: x[2])
        print('Trading Day = {0}'.format(self.trading_date))
        print('Last Quote Time = {0}'.format(self.last_quote))
        print('Number of valid quotes = {0}'.format(self.valid_quotes))
        print('Most active hour = {0}'.format(self.most_active_hour))
        print('Most active symbol = {0}'.format(self.most_active_symbol))
        for group in group_by_symbol:
            symbol, trades = group
            trades = [trade for trade in trades]
            last_record = trades[-1]
            zip_data = [trade for trade in zip(*trades)][3]
            print(last_record[0], last_record[1], "{0},{1},{2}".format(symbol, max(zip_data), min(zip_data)))


class TradeData(object):
    def __init__(self, trades):
        self.trades = trades
        self.exchange_start_time = tuple(int(i) for i in '09:30:00'.split(':'))
        self.exchange_end_time = tuple(int(i) for i in '16:30:00'.split(':'))

    def divide_trades_by_session(self):
        valid_trades = filter(
            lambda trade: self.exchange_start_time <= tuple(
                int(i) for i in trade[1].split(':')) <= self.exchange_end_time,
            self.trades)
        trades_by_session = itertools.groupby(valid_trades, lambda x: x[0])
        return trades_by_session

    def gen_report(self):
        trades_by_day = self.divide_trades_by_session()
        for day in trades_by_day:
            DayTrade(*day).report()


if __name__ == "__main__":
    n = int(input())
    ar = []
    for _ in range(n):
        t = input().split(',')
        ar.append(t)
    tr = TradeData(ar)
    tr.gen_report()
