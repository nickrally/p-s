import statistics
import numpy as np
import pytest


def odd(l):
    if len(l) % 2 == 0:
        return False
    else:
        return True

def breakInTwo(sorted_data):
    left = []
    right = []
    if odd(sorted_data):
        median = statistics.median(sorted_data)
        idx1 = int((len(sorted_data)) / 2)
        for idx, x in enumerate(sorted_data):
            if idx < idx1:
                left.append(x)
            elif idx > idx1:
                right.append(x)
    else:
        idx1 = int((len(sorted_data))/2 -1)
        idx2 = int((len(sorted_data))/2)
        append_to_left   = sorted_data[idx1]
        prepend_to_right = sorted_data[idx2]
        for idx, x in enumerate(sorted_data):
            if idx < idx1:
                left.append(x)
            elif idx > idx2:
                right.append(x)

        left.append(append_to_left)
        right.insert(0,prepend_to_right)

    return left, right

def calcInterquartileRange(data):
    sorted_data = sorted(data)
    left, right = breakInTwo(sorted_data)
    mean_left = statistics.median(left)
    mean_right = statistics.median(right)
    return mean_right - mean_left


@pytest.mark.skip(reason="fails assertion 6==8")
def test_bad_irq():
    odd_data = [4, 4, 10, 11, 15, 7, 14, 12, 6]
    d = sorted(odd_data)
    q75, q25 = np.percentile(odd_data, [75,25])
    iqr = q75 - q25
    assert iqr == 8
    iqr = np.percentile(d, 75, interpolation='higher') - np.percentile(d, 25, interpolation='lower')
    assert iqr == 8


def test_practice():
    l = [4, 4, 10, 11, 15, 7, 14, 12, 6]
    iqr = calcInterquartileRange(l)
    assert iqr == 8

    l = [7, 9, 9, 10, 10, 10, 11, 12, 12, 14]
    iqr = calcInterquartileRange(l)
    assert iqr == 3

    l = [1,5,3,1,5,5,9,4,7,6,4]
    iqr = calcInterquartileRange(l)
    assert iqr == 3

    l = [5, 6, 8.2, 2.6, 6, 4.9, 5, 8, 7.9, 3]
    iqr = calcInterquartileRange(l)
    assert iqr == 3.0

    l = [0,0,0,1,1,3,3,4,7,7]
    iqr = calcInterquartileRange(l)
    assert iqr == 4

    l = [7,12,14,15,11,4,4,6,10]
    iqr = calcInterquartileRange(l)
    assert iqr == 8
