import math

def nCk(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def calcFairOrUnfairCoinHeadProbability(flips, heads, p_single_outcome):
    '''
    see Generalizing k scores in n attempts
    https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/v/generalizing-k-scores-in-n-attempts

    this computs the probability distribution for a random variable
    that's defined by the number of scores in your n attempts
    '''
    combos = nCk(flips, heads)
    tails = flips - heads
    compound_p = (p_single_outcome ** heads) * ((1 - p_single_outcome) ** tails)
    p = combos * compound_p
    return p

flips = 6
heads = 4

p = calcFairOrUnfairCoinHeadProbability(flips, heads, 0.5)
print ("Probability of getting %s Heads in %s coin flips: %s" %(heads, flips, round(p,4))) # 0.2344


p = calcFairOrUnfairCoinHeadProbability(flips, heads, 0.8)
print("Probability of getting %s Heads in %s coin flips: %s" % (heads, flips, round(p, 4))) # 0.2458

p = calcFairOrUnfairCoinHeadProbability(flips, heads, 1)
print("Probability of getting %s Heads in %s coin flips: %s" % (heads, flips, round(p, 4))) # 0.0

heads = 6

p = calcFairOrUnfairCoinHeadProbability(flips, heads, 1)
print("Probability of getting %s Heads in %s coin flips: %s" % (heads, flips, round(p, 4))) # 1.0