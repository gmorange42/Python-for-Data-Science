class calculate:
    '''Contains calculation methods.

    Methods:
    def mean(lst: list) -> int
    def median(lst: list) -> int
    def quartile(lst: list) -> list[float]
    def variance(lst: list) -> float
    def standardDeviation(lst: list) -> float

    '''

    @staticmethod
    def mean(lst: list) -> int:
        '''return the mean of lst'''
        return sum(lst) / len(lst)

    @staticmethod
    def median(lst: list) -> int:
        '''return the median of lst'''
        return lst[len(lst) // 2] if len(lst) % 2 == 1 else \
            (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

    @staticmethod
    def quartile(lst: list) -> list[float]:
        '''return the quartile  of lst'''
        return [float(lst[len(lst) // 4]), float(lst[len(lst) // 4 * 3])]

    @staticmethod
    def variance(lst: list) -> float:
        '''return the variance of lst'''
        _mean = calculate.mean(lst)
        return (sum([(x - _mean)**2 for x in lst])) / len(lst)

    @staticmethod
    def standardDeviation(lst: list) -> float:
        '''return the standard deviation of lst'''
        return calculate.variance(lst)**(1/2)


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Applies kwargs calculations to all args values

    Parametres:
    args: values tu calculate.
    kwargs: calculations to do.
    '''
    functions = {'mean': calculate.mean,
                 'median': calculate.median,
                 'quartile': calculate.quartile,
                 'var': calculate.variance,
                 'std': calculate.standardDeviation}
    try:
        assert all([isinstance(x, (int, float)) for x in args])
        lst = list(args)
        lst.sort()
        for value in kwargs.values():
            if not (len(args)):
                print("ERROR")
            elif value in functions:
                print(f'{value} : {functions[value](lst)}')
    except AssertionError:
        print("Error: args must be integers or floats")


def main():
    '''Tests ft_statistics()'''
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == '__main__':
    main()
