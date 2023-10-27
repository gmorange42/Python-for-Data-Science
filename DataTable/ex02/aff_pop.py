from load_csv import load
import matplotlib.pyplot as plt


def value_to_float(x):
    '''converts abbreviated string in float'''
    if isinstance(x, float) or isinstance(x, int):
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


def main():
    '''display a graph of population in France and Belgium'''
    try:
        data = load('../ressources/population_total.csv')
        data.set_index("country", inplace=True)
        data = data[data.columns[:-50]]
        years = list(data.columns)
        years = [int(x) for x in years]
        france = list(data.loc['France'])
        france = [value_to_float(x) for x in france]
        belgium = list(data.loc['Belgium'])
        belgium = [value_to_float(x) for x in belgium]
        plt.plot(years, belgium)
        plt.plot(years, france)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(['Belgium', 'France'], loc=4)
        plt.xticks(range(1800, 2050, 40), range(1800, 2050, 40))
        plt.xlim(1790, 2060)
        plt.yticks(range(0, int(max(france)), int(2 * 1e7)),
                   ['0', '20M', '40M', '60M'])
        plt.ylim(0, 7 * 1e7)
        plt.show()
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except AssertionError:
        print("AssertionError: opening file failed")
    except AttributeError:
        print("AttributeError: opening file failed")


if __name__ == '__main__':
    main()
