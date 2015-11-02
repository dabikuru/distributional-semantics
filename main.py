import pickle
from dsm.preprocessing import read_candidates, read_features
from dsm.matrix import Matrix
import json


def main(f_candidates, f_features, f_corpus):
    # Open corpus file
    with    open(f_corpus, 'r') as h_corpus,\
            open(f_candidates, 'r') as h_candidates,\
            open(f_features, 'r') as h_features,\
            open('../tmp/model.p', 'wb') as fout:

        candidates = read_candidates(h_candidates)
        features = read_features(h_features)

        model = Matrix(candidates, features, h_corpus)
        model.populate()

        # json.dump(model.m, fout1)
        pickle.dump(model.m, fout)


if __name__ == '__main__':
    main('../data/wordsim353/combined.csv', '../data/frequent_words', '../data/wikicorpus.list')
    # main('../data/test/candidates.csv', '../data/test/features', '../data/test/corpus')
