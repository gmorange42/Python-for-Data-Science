from numpy import shape


def check_list(lst: list) -> bool:
    '''check if lst is a list that only contains lists of the same lenght'''
    return (isinstance(lst, list) and
            all(isinstance(i, list) for i in lst) and
            all([len(i) == len(lst[0]) for i in lst]))


def slice_me(family: list, start: int, end: int) -> list:
    '''print the shape of the list, \
 slice it with start and end, print the shape of the new list'''
    try:
        assert check_list(family)
        assert isinstance(start, int)
        assert isinstance(end, int)
        print("My shape is:", shape(family))
        family_sliced = family[start:end]
        print("My new shape is:", shape(family_sliced))
        return (family_sliced)
    except AssertionError:
        print("AssertionError: not a list or nor same lenght")


def main():
    '''main function to test slice_me()'''
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == '__main__':
    main()
