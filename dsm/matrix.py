from collections import Counter
from dsm.window import Window


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
            # Counter defaults to 0 for missing keys – no need to instantiate features in all of them
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
        when the central word is in candidates.csv, add its neighbours to the counter.
        """

        window = Window(self.corpus, 3)
        for (word, neighbours) in window:
            if word in self.candidates:
                self.m[word].update([n for n in neighbours if (n in self.features)])
