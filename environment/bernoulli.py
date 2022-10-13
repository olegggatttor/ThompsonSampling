from scipy.stats import bernoulli


class BernoulliAgent:
    def __init__(self, ps):
        self.ps = ps

    def react(self, i):
        assert 0 <= i < len(self.ps)
        return bernoulli.rvs(p=self.ps[i])
