from collections import Counter
import string
import csv


def strip_punctuation(file):
    exclude = str.maketrans('', '', string.punctuation)

    with open(file, 'r') as fin:
        with open (file + '.stripped', 'w') as fout:
            for line in fin:
                s = str.translate(line, exclude)
                fout.write(s)


def load_stopwords():
    with open('../data/stopwords', 'r') as fin:
        return frozenset(map(str.strip, fin.readlines()))


def n_most_frequent(corpus, n=100):
    stopwords = load_stopwords()
    freqs = Counter()

    with open(corpus, 'r') as fin:
        counter = 0
        for line in fin:
            word = line.strip()
            if word not in stopwords and len(word) >= 3:
                freqs.update([line.strip()])
                counter += 1
                if counter % 100000 == 0:
                    print(counter)
    with open('frequent_words', 'w') as fout:
        for (word, count) in freqs.most_common(n):
            fout.write("{} {}\n".format(word, count))


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
