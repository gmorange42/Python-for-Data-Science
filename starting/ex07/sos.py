from sys import argv


def checkstr(s: str) -> bool:
    '''check if the string contain only alphanum and space'''
    nospace = s.replace(' ', '')
    return nospace.isalnum()


def main():
    '''convert string in morse code'''
    NESTED_MORSE = {
            ' ': '/',
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.'
        }

    try:
        assert len(argv) == 2
        assert checkstr(argv[1])
        morse_string = str()
        for i in argv[1]:
            morse_string += (NESTED_MORSE[i.upper()] + ' ')
        morse_string = morse_string[:-1]
        print(morse_string)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == '__main__':
    main()
