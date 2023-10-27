from sys import argv

try:
    assert len(argv) < 3, "more than one argument is provided"
    if len(argv) == 2:
        assert (argv[1].lstrip('-')).isnumeric(), "argument is not an integer"
        if int(argv[1].lstrip('-')) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

except AssertionError as e:
    print("AssertionError:", e)
