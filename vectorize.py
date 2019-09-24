"""
    vectorize.py
    Matthew Reading
    September 23 2019
"""
import os
import sys
from glob import glob
from sklearn.feature_extraction.text import TfidfVectorizer

def clean(corpus):
    """ Preprocess the corpus and remove unnecessary data """
    # Ines work your magic
    # remove ascii
    # convert to lowercase
    # remove stop characters
    pass


def vectorize(essays):
    """ Tf-idf (term-frequency - inverse document frequency) term weighting """

    # initialize or open vectorizer here using PICKLE
    vectorizer = TfidfVectorizer()

    for essay in essays:
        raw_text = open(essay, 'rb')
        try:
            corpus = raw_text.read()
            corpus = clean(corpus)
            # vectorizer.fit_transform(corpus)
        except:
            print("Unable to read", raw_text.name)
        raw_text.close()

    # dump initializer using PICKLE here

    return 0


def main():
    """ Steam essay files to be vectorized """

    # open path to essay directory and load filenames into list
    try:
        essays = glob(os.path.join(sys.argv[1], "*.txt"))
    except:
        print("Invalid or no path to essay directory.")
        return -1

    return vectorize(essays)


if __name__ == "__main__":
    main()
