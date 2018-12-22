# I have a 0.35 probability of making a free throw
# What is the probability of making less than 5 out of 7 free throws

import math

def calculateScoreProbability(throws, scores, single_score_probability):
    misses = throws - scores
    compound_probability = (single_score_probability ** scores) * ((1 - single_score_probability) ** misses)
    combinations = math.factorial(throws) / (math.factorial(scores) * math.factorial(throws - scores))
    return combinations * compound_probability


def binomialCumulativeDistribution(throws, max_score, single_score_probability):
    cumulative_probability = 0
    for scores in range(0, max_score + 1):
        cumulative_probability += calculateScoreProbability(throws, scores, single_score_probability)
    return cumulative_probability



throws    = 7
max_score = 4
single_score_probability = 0.35

p = binomialCumulativeDistribution(throws, max_score, single_score_probability)
print("Cumulative binomial function returned: %s" % round(p, 3))


