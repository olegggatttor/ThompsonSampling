import numpy as np
from scipy.stats import beta


class BernoulliBandit:
    def __init__(self, n: int):
        self.alphas = np.ones(n)
        self.betas = np.ones(n)

    def sample(self):
        probabilities_of_click = []
        for a, b in zip(self.alphas, self.betas):
            probabilities_of_click.append(beta.rvs(a, b))
        return np.argmax(probabilities_of_click)

    def update(self, i: int, result: int):
        assert result == 0 or result == 1

        self.alphas[i] += result
        self.betas[i] += (1 - result)

    def get_beta_params(self):
        return self.alphas, self.betas
