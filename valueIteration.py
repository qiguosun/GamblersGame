import numpy as np
import matplotlib.pyplot as plt

STATESPACE = 100
ACTIONSPACE = 100
PROB_HEAD = 0.4
TOR = 0.0001
GAMMA = 0.99


class GamblersSolver(object):
    def __init__(self, STATESPACE=STATESPACE, ACTIONSPACE=ACTIONSPACE, PROB_HEAD=PROB_HEAD, TOR=TOR, GAMMA=GAMMA):
        self.values = np.zeros(shape=ACTIONSPACE+1, dtype=np.float32)
        self.policy = np.zeros(shape=ACTIONSPACE+1, dtype=np.float32)
        self.reward = np.zeros(shape=ACTIONSPACE+1, dtype=np.float32)
        self.reward[100] = 1
        self.prob_head = PROB_HEAD
        self.stateSpace = STATESPACE
        self.tor = TOR
        self.gamma = GAMMA

    def valueIteration(self):
        while True:
            delta = 0

            for capital in range(self.stateSpace):
                v = self.values[capital]
                optimal_value = 0
                for stack in range(capital+1):
                    capital_if_win = min(self.stateSpace, capital+stack)
                    capital_if_loss = capital - stack
                    expect_capital = self.prob_head*(self.reward[capital_if_win] +
                                                     self.gamma * self.values[capital_if_win]) +\
                        (1-self.prob_head)*(self.reward[capital_if_loss] +
                                            self.gamma * self.values[capital_if_loss])
                    if expect_capital > optimal_value:
                        self.policy[capital] = stack
                        optimal_value = expect_capital
                        self.values[capital] = expect_capital
                delta = max(delta, np.abs(v - self.values[capital]))
            if delta < self.tor:
                break
        return self.policy


if __name__ == "__main__":
    solver = GamblersSolver()
    opt_policy = solver.valueIteration()
    plt.figure(figsize=(10, 8))
    plt.title("Gamblers Game")
    plt.xlabel("Capital")
    plt.ylabel("Optimal-Stack")
    plt.scatter(np.array(range(ACTIONSPACE+1)), opt_policy)
    plt.savefig("./opt_policy.png")
