def square(x: int | float) -> int | float:
    '''Return the square of x'''
    try:
        return x**2
    except TypeError as e:
        print("Error:", e)


def pow(x: int | float) -> int | float:
    '''Return the exponentiation of x by itself '''
    try:
        return x**x
    except TypeError as e:
        print("Error:", e)


def outer(x: int | float, function) -> object:
    '''return the function inner()'''
    try:
        assert isinstance(x, (int, float))
        assert callable(function)
        count = 0

        def inner() -> float:
            '''Count is incremented each time inner() is called.
The operation given to outer() is performed count times.
The result is returned'''
            nonlocal count
            count += 1
            result = x
            for i in range(count):
                result = function(result)
            return result
        return inner
    except AssertionError:
        print("Error, x must be an int or a float and function a function")


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == '__main__':
    main()
