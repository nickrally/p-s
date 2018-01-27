import random
import statistics
import standard_deviation


pop_size       = 1000
high           = 100
low            = 50
sample_size    = 10
num_of_samples = 10

def makePopulation(pop_size, high, low):
    data = []
    for i in range(pop_size):
        data.append(random.randrange(low, high))
    return data

def pickUniqueIndices(size, limit):
    indices = []
    count = 0
    while count < size:
        idx = random.randrange(0, limit)
        if idx not in indices:
            indices.append(idx)
            count += 1
    return indices

def makeSamples(population, sample_size, num_of_samples):
    samples = []
    for i in range(num_of_samples):
        for i in range(num_of_samples):
            indices = pickUniqueIndices(sample_size, len(population) - 1)
        sample = [x for idx, x in enumerate(population) if idx in indices]
        samples.append(sample)
    return samples

def getDeviations():
    population = makePopulation(pop_size, high, low)
    population_std_dev = standard_deviation.calcStandardDeviation(population)
    print("Population Standard Deviation: %s" % population_std_dev)
    samples = makeSamples(population, sample_size, num_of_samples)
    samples_std_div = []
    for sample in samples:
        sample_std_dev = standard_deviation.calcStandardDeviation(sample, False)
        samples_std_div.append(sample_std_dev)

    samples_std_div_mean = round(statistics.mean(samples_std_div),2)
    print ("Mean of Sample Deviations:     %s" % samples_std_div_mean)
    print("==============")
    print("Sample Standard Deviations: %s" % samples_std_div)

getDeviations()

################## tests

def test_pickUniqueIndices():
    size    = 10
    limit   = 99
    indices = pickUniqueIndices(size, limit)
    assert len(indices) == 10
    assert not [i for i in indices if i > limit]
    assert len(indices) == len(set(indices))

def test_makeSamples():
    population = makePopulation(pop_size, high, low)
    samples = makeSamples(population, sample_size, num_of_samples)
    assert len(samples) == 10





