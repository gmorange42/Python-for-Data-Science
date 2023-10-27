class calculator:
    '''A class that can do basic operations between a vector and an object

    Attribute:
    vector (object): a vector with the values to calculate.

    Methods:
    __init__(self, vector)
    __add__(self, object) -> None
    __mul__(self, object) -> None
    __sub__(self, object) -> None
    __truediv__(self, object) -> None

        '''

    def __init__(self, vector):
        '''set a vector with the values to calculate.'''
        self.vector = vector

    def __add__(self, object) -> None:
        '''adds object to all the values of self.vector and print it'''
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        '''multiplies the object to all the values of self.vector
            and print it'''
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        '''substracts the object to all the values of self.vector
            and print it'''
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        '''divides the object to all the values of self.vector and print it'''
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print("ZeroDivisionError", e)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == '__main__':
    main()
