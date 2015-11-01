from collections import Counter
import string
import glob


def strip_punctuation(file):
    exclude = str.maketrans('', '', string.punctuation)

    with open(file, 'r') as fin:
        with open (file + '.stripped', 'w') as fout:
            for line in fin:
                s = str.translate(line, exclude)
                fout.write(s)


def load_stopwords():
    with open('../res/stopwords', 'r') as fin:
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


n_most_frequent('../res/wikicorpus.list', 2000)
