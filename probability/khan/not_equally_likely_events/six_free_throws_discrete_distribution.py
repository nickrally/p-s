import math


def nChooseK(n, k):
    num_of_ways = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    print ("There are %s ways to score %s out of %s throws" %(num_of_ways, k, n))
    return num_of_ways

def calculateScoreProbability(throws, scores, single_score_probability):
    misses = throws - scores
    compound_probability = (single_score_probability ** scores) * ((1 - single_score_probability) ** misses)
    combinations = nChooseK(throws, scores)
    return combinations * compound_probability

throws = 6
single_score_probability = 0.7

# what is the probability of our random variable p be 0, 1, 2, 3 ,4 ,5 , or 6
for scores in range(0, 7):       # may score 0, 1, 2, 3 ,4 ,5 ,6 out of 6 throws
    p = calculateScoreProbability(throws, scores, single_score_probability)
    print ("Probability of scoring %s out of %s throws: %s " %(scores, throws, round(p,3)))