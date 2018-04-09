import time

class UtilityManager:

    def __init__(self):
        self.e = ""

    def wait_until(self, predicate, timeout, period=3, *arg, **kwargs):
        mustend = time.time() + timeout
        while time.time() < mustend:
            if predicate(*arg, **kwargs): return True
            time.sleep(period)
        return False
