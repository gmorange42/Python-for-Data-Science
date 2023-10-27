def count_in_list(lst: list, s: str):
    try:
        return lst.count(s)
    except TypeError as e:
        print("TypeError:", e)


def main():
    print(count_in_list(["Roger", "Bill", "Jill",
                        "Jenny", "Roger"], "Roger"))


if __name__ == '__main__':
    main()
