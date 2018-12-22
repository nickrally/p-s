import math

def allFairCoinPossibleOutcomes(flips, outcomes_per_flip):
    return outcomes_per_flip ** flips

def calculateFairCoinHeadProbability(flips, event, outcomes):
    combinations = math.factorial(flips) / (math.factorial(event) * math.factorial(flips - event))
    p = combinations / allFairCoinPossibleOutcomes(flips, outcomes)
    return p

def calculateFairOrUnfairCoinHeadProbability(flips, heads, single_outcome_probability):
    '''
    see Generalizing k scores in n attempts
    https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/v/generalizing-k-scores-in-n-attempts
    '''
    combinations = math.factorial(flips) / (math.factorial(heads) * math.factorial(flips - heads))
    tails = flips - heads
    compound_probability = (single_outcome_probability ** heads) * (1 - single_outcome_probability) ** tails
    p = combinations * compound_probability
    return p

flips = 5    # choose 5 over x(where x can be 0, 1 ,2 ,3 ,4, or 5 - Finite Descrete Values)
outcomes = 2 # two outcomes: H or T

for heads in range(0, 6):
    p = calculateFairCoinHeadProbability(flips, heads, outcomes)
    print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4)))

print ("===============")

for heads in range(0, 6):
    p = calculateFairOrUnfairCoinHeadProbability(flips, heads, 0.5)
    print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4)))


print ("===============")

for heads in range(0, 6):
    p = calculateFairOrUnfairCoinHeadProbability(flips, heads, 1.0)
    print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4)))

print ("===============")

for heads in range(0, 6):
    p = calculateFairOrUnfairCoinHeadProbability(flips, heads, 0.0)
    print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4)))

print ("===============")

for heads in range(0, 6):
    p = calculateFairOrUnfairCoinHeadProbability(flips, heads, 0.7)
    print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4)))



