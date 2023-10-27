from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''display a graph of life expectancy in France'''
    try:
        data = load('../ressources/life_expectancy_years.csv')
        data.set_index("country", inplace=True)
        years = list(data.columns)
        years = [int(x) for x in years]
        france = list(data.loc['France'])
        france = [float(x) for x in france]
        plt.plot(years, france)
        plt.title("France Life expectancy projections")
        plt.xlabel("Years")
        plt.ylabel("Life expectancy")
        plt.xticks(ticks=range(1800, 2100, 40),
                   labels=range(1800, 2100, 40))
        plt.xlim(1790, 2110)
        plt.show()
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except AssertionError:
        print("AssertionError: opening file failed")
    except AttributeError:
        print("AttributeError: opening file failed")


if __name__ == '__main__':
    main()
