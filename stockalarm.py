# Used as an imported class 
# e.g from stockalarm import StockAlarm

class StockAlarm:
    """
    Creates an alarm object.

    Plays a semi-customisable sound(?) based on stockname input for alarm?
    """

    def __init__(self, stockname):
        self._stockname = stockname

    def riseToValue(self, value):
        # Play sound
        pass

    def fallToValue(self, value):
        # Play sound
        pass

    def recoveringTrend(self, value):
        # Play sound
        pass

    def peakingTrend(self, value):
        # Play sound
        pass

    def rocketTrend(self):
        # Play sound
        pass

    def crashingTrend(self):
        # Play sound
        pass