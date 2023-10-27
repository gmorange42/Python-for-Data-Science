import sys
sys.tracebacklimit = 0


class ft_filter:
    '''ft_filter(function or None, iterable) --> filter object\n\nReturn an \
iterator yielding those items of iterable for which function(item)\nis true. \
If function is None, return the items that are true.'''
    def __init__(self, function, sequence):
        '''fill attribute'''
        try:
            self.function = function
            self.sequence = sequence
            self.iterator = iter(sequence)
        except TypeError as e:
            print("TypeError:", e)

    def __iter__(self):
        '''return a iterator'''
        return self

    def __next__(self):
        '''return the next filtred value in sequence'''
        while True:
            item = next(self.iterator)
            if not self.function or self.function(item):
                return item
