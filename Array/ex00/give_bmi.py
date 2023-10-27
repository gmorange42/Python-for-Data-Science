def check_list(lst: list[int | float]) -> bool:
    '''check if a list is a list that contains only integers or floats'''
    return (isinstance(lst, list) and
            all(isinstance(i, (int, float)) for i in lst))


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''return a list of BMI calculated with \
a list of height and another of weight'''
    try:
        assert check_list(height)
        assert check_list(weight)
        assert len(height) == len(weight)
        return [w / h**2 for w, h in zip(weight, height)]
    except AssertionError:
        print("AssertionError: bad lenght or types")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''return a Boolean list that indicates if \
the values of a list are above a limit'''
    try:
        assert check_list(bmi)
        assert isinstance(limit, (int, float))
        return [b > limit for b in bmi]
    except AssertionError:
        print("AssertionError: bad lenght or types")


def main():
    '''Test give_bmi() and apply_limit()'''
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == '__main__':
    main()
