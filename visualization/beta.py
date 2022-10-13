from copy import deepcopy


class InteractiveBetaCollector:
    def __init__(self, init_alphas, init_betas, real_probabilities):
        self.alphas = []
        self.betas = []
        self.real_probabilities = real_probabilities

        self.update(init_alphas, init_betas)

    def update(self, a, b):
        self.alphas.append(deepcopy(a))
        self.betas.append(deepcopy(b))

    def get(self):
        return self.alphas, self.betas, self.real_probabilities
