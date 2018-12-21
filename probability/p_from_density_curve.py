import random
#whatever............
PERCENT_OF_VALUES_1_SD_AWAY_FROM_MEAN  = 0.68  # 68%

def makeRandomData(mu, sigma, population_size):
    data = []
    for x in range(population_size):
        height = round(random.gauss(mu, sigma), 2)
        data.append(height)
    return data

def main():
    population_size = 10000

    mu    = 59
    sigma = 8
    h5f7i = mu + sigma
    data = makeRandomData(mu, sigma, population_size)

    # get all values one standard deviation above mean:
    above_st_div = [value for value in data if value > h5f7i]
    print(len(above_st_div))

    probablity_of_h5f7i = round(len(above_st_div)/population_size, 4)
    theoretical         = round(1 - (0.5 + PERCENT_OF_VALUES_1_SD_AWAY_FROM_MEAN / 2), 4)

    print(probablity_of_h5f7i)
    print(theoretical)

if __name__ == "__main__":
    main()
