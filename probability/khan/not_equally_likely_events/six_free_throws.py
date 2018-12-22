import math

def caclulateScoreProbability(throws, scores, single_score_probability):
    misses = throws - scores
    compound_probability = (single_score_probability ** scores) * ((1 - single_score_probability) ** misses)
    combinations = math.factorial(throws) / (math.factorial(scores) * math.factorial(throws - scores))
    return combinations * compound_probability


throws = 6
scores = 2
single_score_probability = 0.7

p = caclulateScoreProbability(throws, scores, single_score_probability)
print (p)
assert round(p, 6) == 0.059535

import sympy
# from scipy.stats.distributions import binom
# p2 = binom.cdf(scores, throws, single_score_probability)
# print (p2) # 0.07047
#assert p == p2