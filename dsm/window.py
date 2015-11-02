from itertools import islice


class Window:
    """
    Iterator that creates a sliding window (of size n*2 + 1) over an iterable.
    """

    def __init__(self, seq, n=2):
        """
        :param seq: an iterable
        :param n: window size (on one side)
        """
        self.seq = iter(seq)
        self.n = n * 2 + 1
        self.result = None

    def __iter__(self):
        if self.result is None:
            self.result = tuple(map(str.strip, islice(self.seq, self.n)))
            yield self.word(), self.neighbours()

        for elem in self.seq:
            self.result = self.result[1:] + (elem.strip(),)
            yield self.word(), self.neighbours()

    def neighbours(self):
        return self.result[:self.n // 2] + self.result[(self.n // 2) + 1:]

    def word(self):
        return self.result[self.n // 2]
