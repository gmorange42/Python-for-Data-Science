class calculator:
    '''A class that can do dot product, addition or substraction
        between two vectors.

    Methods:
    dotproduct(V1: list[float], V2: list[float]) -> None:
        prints the sum of all dot product of two vectors

    add_vec(V1: list[float], V2: list[float]) -> None:
        prints a list of the sum of two vectors

    sous_vec(V1: list[float], V2: list[float]) -> None:
        prints a list of the substrction of two vectors

        '''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''prints the sum of all dot product of two vectors'''
        print(sum(a * b for a, b in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''prints a list of the sum of two vectors'''
        print([float(a + b) for a, b in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''prints a list of the substrction of two vectors'''
        print([float(a - b) for a, b in zip(V1, V2)])


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == '__main__':
    main()
