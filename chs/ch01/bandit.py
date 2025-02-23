import numpy as np

class Bandit:
    def __init__(self,arms=10):
        self.rates = np.random.rand(arms)