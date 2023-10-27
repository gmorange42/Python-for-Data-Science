import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    '''loads a file.csv, displays its shape and returns it'''
    try:
        assert path.endswith(".csv")
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except AssertionError:
        print("AssertionError: the format is not .csv")
    except IsADirectoryError as e:
        print("IsADirectory:", e)
    except pd.errors.EmptyDataError as e:
        print("pandas.errors.EmptyDataError:", e)
    except pd.errors.ParserError as e:
        print("pandas.errors.ParserError", e)
    else:
        return None


def main():
    '''tests load() with the file life_expectancy_years.csv'''
    print(load("../ressources/eparse_life_expectancy_years.csv"))


if __name__ == '__main__':
    main()
