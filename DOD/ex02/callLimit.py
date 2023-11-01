def callLimit(limit: int):
    '''Return the decorator callLimiter'''
    count = 0

    def callLimiter(function):
        '''Return limit_function'''

        def limit_function(*args: any, **kwds: any):
            '''Return the function given to callLimiter
if count is lower than limit.'''
            try:
                nonlocal count
                assert count < limit
                count += 1
                return function(*args, **kwds)
            except AssertionError:
                print("Error:", function, "call to many times")
            except TypeError:
                print("Errror: limit must be an integer")

        return limit_function

    return callLimiter


def main():
    '''tests callLimit'''
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == '__main__':
    main()
