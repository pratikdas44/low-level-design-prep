from WriteStrategy.Strategy import Strategy

class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self):
        if self.strategy:
            self.strategy.write_strategy()
        else:
            print("No strategy set!")
