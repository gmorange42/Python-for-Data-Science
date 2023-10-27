import sys as sys


def count(string: str):
    '''Print the number of characters, upper case, lower case, \
punctuation characters, digits and spaces in string'''
    upper = lower = punctuation = space = digit = 0
    all_punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in string:
        if i in all_punctuation:
            punctuation += 1
            continue
        upper += i.isupper()
        lower += i.islower()
        digit += i.isdigit()
        space += i.isspace()
    print("The text contain", len(string), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation mark")
    print(space, "spaces")
    print(digit, "digits")


def noText():
    '''Ask to the user a text and give him a prompt.\
If the user write a text it call count(), \
else it ask again to the user to write a text '''
    print("What is the text to count?")
    for i in sys.stdin:
        if len(i) > 1:
            count(i)
            break


def main():
    '''Check if there is a argument. If there is one it call count(), \
else it call noText()'''
    try:
        assert len(sys.argv) < 3
        if len(sys.argv) == 2:
            if sys.argv[1] == 'None':
                noText()
            else:
                count(sys.argv[1])
        else:
            noText()
    except KeyboardInterrupt:
        sys.exit()
    except AssertionError:
        print("AssertionError: More than one argument")


if __name__ == '__main__':
    main()
