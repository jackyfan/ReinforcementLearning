import numpy as np


# 老虎机
class Bandit:
    def __init__(self, arms=10):
        self.rates = np.random.rand(arms)

    def play(self, arm):
        rate = self.rates[arm]
        if rate >= np.random.rand():
            return 1
        else:
            return 0


# 智能代理
class Agent:
    def __init__(self, epsilon, action_size=10):
        self.epsilon = epsilon
        self.action_size = action_size
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    def update(self, action, reward):
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))
        else:
            return np.argmax(self.Qs)


bandit = Bandit()
Qs = np.zeros(10)
ns = np.zeros(10)
for n in range(1, 11):
    action = np.random.randint(0, 10)
    reward = bandit.play(action)
    ns += 1
    Qs[action] += (reward - Qs[action]) / ns[action]
    print(Qs)
