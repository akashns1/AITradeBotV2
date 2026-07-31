

class ReplayEngine:
    def __init__(
        self,
        signal_generator,
        trade_engine,
    ):
        self.signal_generator = signal_generator
        self.trade_engine = trade_engine

    def replay(self, candles):
        pass