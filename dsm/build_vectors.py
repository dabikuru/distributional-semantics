from itertools import islice
from collections import Counter
import pickle as p
import csv


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
        self.word = None
        self.neighbours = self.result[:n // 2] + self.result[(n // 2) + 1:]

    def __iter__(self):
        return self

    def __next__(self):
        if self.result is None:
            self.result = tuple(islice(self.seq, self.n))
            self.word = self.result[self.n // 2]
            return self.word, self.neighbours

        for elem in self.seq:
            self.result = self.result[1:] + (elem,)
            self.word = self.result[self.n // 2]
            return self.word, self.neighbours


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
        self.candidates = candidates
        self.features = features
        self.corpus = corpus

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
        return  # cosine similarity of two vectors

    def populate(self):
        """
        Iterate over corpus with a sliding window:
        when the central word is in candidates, add its neighbours to the counter.
        """

        window = Window(self.corpus, 3)
        for (word, neighbours) in window:
            if word in self.candidates:
                self.m[word].update([n for n in neighbours if (n in self.features)])


def read_candidates(f_candidates):
    """
    Retrieves target words from a file
    :param f_candidates: file handle
    :return: set of target words
    """
    reader = csv.reader(f_candidates)
    candidates = set()
    for (w1, w2, _) in reader:
        candidates.add(w1)
        candidates.add(w2)
    return candidates


def read_features(f_features):
    """
    Retrieves feature words from a file
    :param f_features: file handle
    :return: set of features
    """
    features = set()
    for f in f_features:
        features.add(f.split()[0])
    return features


def main():
    with open('../res/wikicorpus.list', 'r') as f_corpus:
        with open('../res/frequent_words', 'r') as f_features:
            features = read_features(f_features)
        with open('../res/wordsim353/combined.csv', 'r') as f_candidates:
            candidates = read_candidates(f_candidates)

        model = Matrix(candidates, features, f_corpus)
        model.populate()
        with open('../tmp/model.p', 'wb') as fout:
            p.dump(model, fout)

# TODO: neighbours returns None
