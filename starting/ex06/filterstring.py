from sys import argv


def toInt(s: str) -> int: return int(s)


def main():
    '''return a list of words in a string that have a lenght \
greater than a given integer'''
    try:
        assert len(argv) == 3
        splited = argv[1].split()
        new_list = [i for i in splited if len(i) > toInt(argv[2])]
        print(new_list)
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except ValueError:
        print("ValueError: the second argument is not an integer")


if __name__ == '__main__':
    main()
