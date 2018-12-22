import statistics
import math


def calcVariance(data, population):
    mean = statistics.mean(data)
    numerator = 0
    for e in data:
        numerator += (e - mean) ** 2
    denominator = len(data) if population else len(data) - 1
    variance = numerator / denominator
    return variance

def calcStandardDeviation(data, population=True):
    variance = calcVariance(data, population)
    std_deviation = round(math.sqrt(variance), 2)
    return std_deviation


def test_calcVariance():
    import numpy as np

    p_data = [1, 3, 5, 7, 14]
    assert np.var(p_data) == calcVariance(p_data, True)

    p_data = [4, 4.2, 5, 4.3, 5.5]
    assert calcStandardDeviation(p_data) == 0.56

    s_data = [4,3,5,7,2,9,11,7]
    assert calcStandardDeviation(s_data, False) == 3.07

    p_data = [8,4,14,16,8]
    assert calcStandardDeviation(p_data) == 4.38

    s_data = [5,4,6,39]
    assert calcStandardDeviation(s_data, False) == 17.02

    p_data = [22,13,18,16]
    assert calcStandardDeviation(p_data) == 3.27

    s_data = [8,4,14,16,8]
    assert calcStandardDeviation(s_data, False) == 4.9

    import interquartile_range
    p_data = [35,50,50,50,56,60,60,75,250]
    # the data is skewed by an outlier (250) , and measurements based on the mean are not representative:
    assert round(statistics.mean(p_data), 2) == 76.22
    assert calcStandardDeviation(p_data, True) == 62.27
    # when the data is skewed, measures based on the median are more representative:
    assert round(statistics.median(p_data), 2) == 56
    assert interquartile_range.calcInterquartileRange(p_data) == 17.5