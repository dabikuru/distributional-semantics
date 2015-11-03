from collections import Counter
from dsm.window import Window
import pickle

class Matrix:
    def __init__(self, candidates=None, features=None, corpus=None, model=None):
        """
        Create a (empty) sparse matrix indexed by candidate and feature words
        :param candidates: list of words for which vectors will be built
        :param features: list of words to be used as features
        :param corpus: file handle to the training corpus
        :return:
        """

        self.candidates = candidates
        if candidates is not None:
            for c in candidates:
                # Counter defaults to 0 for missing keys – no need to instantiate features in all of them
                self.m[c] = Counter()

        self.features = features
        self.corpus = corpus

        self.m = dict() if model is None else self.load(model)

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

    def load(self, serialized):
        """
        Load a serialized matrix into the object instance
        :param serialized: file handle to a serialized matrix of type (Dict of Counters)
        """
        self.m = pickle.load(serialized)

    def save(self, fout):
        """
        Serialize the matrix to a pickled file.
        :param fout: file handle to output file
        """
        pickle.dump(self.m, fout)
