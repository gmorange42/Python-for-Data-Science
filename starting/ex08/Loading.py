def calculate_values(i, lst):
    '''calculate the values to print'''
    percent_int = int(round((i + 1) / len(lst) * 100))
    percent_str = str(percent_int) + "%"
    journey = str(i + 1) + '/' + str(len(lst))
    bar = str(("=") * ((int(percent_int / 2) - 1))) + ">"
    return str("\r" + percent_str.ljust(4) + "[|" + bar.ljust(50) + "]| "
                                                                    + journey)


def ft_tqdm(lst: range):
    '''print a loading bar'''
    try:
        print(calculate_values(-1, lst), end="", flush=True)
        for i, elem in enumerate(lst):
            yield elem
            print(calculate_values(i, lst), end="", flush=True)
    except TypeError as e:
        print("TyperError:", e)
    except ZeroDivisionError:
        print("ZeroDivistionError: Empty list")
