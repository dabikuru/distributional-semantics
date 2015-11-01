from itertools import islice
from collections import Counter


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
        self.n = n*2 + 1

        self.result = None
        self.word = None
        self.neighbours = self.result[:n//2] + self.result[(n//2)+1:]

    def __iter__(self):
        return self

    def __next__(self):
        if self.result is None:
            self.result = tuple(islice(self.seq, self.n))
            self.word = self.result[self.n//2]
            return self.result

        for elem in self.seq:
            self.result = self.result[1:] + (elem,)
            self.word = self.result[self.n//2]
            return self.result


class Matrix:
    def __init__(self, candidates, features, corpus):
        """
        Create a (empty) sparse matrix indexed by candidate and feature words
        :param candidates: list of words for which vectors will be built
        :param features: list of words to be used as features
        :param corpus: file handle to the training corpus
        :return:
        """

        self.m = dict()
        self.candiates = candidates
        self.features = features

        for c in candidates:
            # Counter defaults to 0 for missing keys – no need to instantiate all of them
            self.m[c] = Counter()
        return

    def __getitem__(self, item):
        if type(item) == str:
            return self.m[item]
        elif type(item) == tuple:
            return self.m[item[0]][item[1]]

    def similarity(self, w1, w2):
        # return self.m[w1] * self.m[w2]

    def populate(self):
        """
        Iterate over corpus with a sliding window:
        when the central word is in candidates, add its neighbours to the counter.
        :return:
        """
        # return self.corpus

