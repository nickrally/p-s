import itertools
import math


def getPermutations(s, len=None):
    permutations = list(itertools.permutations(s, len))
    permutations = [''.join(permutation) for permutation in permutations]
    return permutations

def getCombinations(s, i):
    combinations = list(itertools.combinations_with_replacement(s, i))

s = "ABC"
l = ['a','b','c']
gashek = ["Svejk","Baloun","Dub","Lukash","Vodichka"]

def test_str_getPermutations():
    permutations = getPermutations(s)
    assert math.factorial(len(s)) == len(permutations)
    print(len(permutations))
    print("\n".join(permutations))


def test_list_getPermutations():
    permutations = getPermutations(l)
    assert math.factorial(len(s)) == len(permutations)
    print(len(permutations))
    print("\n".join(permutations))

    permutations = getPermutations(l,2)
    assert math.factorial(len(s)) == len(permutations)
    print(len(permutations))
    print("\n".join(permutations))

def test_getCombinations():
    combinations = getCombinations(l, 2)
    print (combinations)
