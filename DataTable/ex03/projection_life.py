from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''display a graph of life expectancy and gross \
national product par person in each country'''
    try:
        life = load('../ressources/life_expectancy_years.csv')
        gnppp = load('../ressources/income_per_person_\
gdppercapita_ppp_inflation_adjusted.csv')
        data = life.copy()
        data['life_1900'] = life['1900'].tolist()
        data['gnppp_1900'] = gnppp['1900'].tolist()
        data = data[data.columns[-2:]]
        data.dropna(inplace=True)
        plt.scatter(data['gnppp_1900'].tolist(), data['life_1900'].tolist())
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.show()
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except AssertionError:
        print("AssertionError: opening file failed")
    except AttributeError:
        print("AttributeError: opening file failed")


if __name__ == '__main__':
    main()
