import nltk
# Corpus which consists of male and female names dataset
from nltk.corpus import names
# For shuffling
import random

import sexmachine.detector as gender
def gender_features(word):
    """ feature extractor for the name classifier
    The feature evaluated here is the last letter of a name
    feature name - "last_letter"
    """

    return {"last_letter": word[-1]}  # feature set
def get_gender(nam):

    labeled_names = ([(name, "male") for name in names.words("/Users/dipit/Desktop/male.txt")] +
                     [(name, "female") for name in names.words("/Users/dipit/Desktop/female.txt")])

    print len(labeled_names)  # 7944 names

    # Shuffle the names in the list
    random.shuffle(labeled_names)

    # Process the names through feature extractor
    feature_sets = [(gender_features(n), gender)
                    for (n, gender) in labeled_names]

    # Divide the feature sets into training and test sets
    train_set, test_set = feature_sets[500:], feature_sets[:500]

    # Train the naiveBayes classifier
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return  classifier.classify(gender_features(nam)) , nltk.classify.accuracy(classifier, test_set)  # returns 0.78 for now


#
# f=["Adam", "Mike", "X"]
# for i in f:
#   print i,get_gender(i)


# if __name__ == "__main__":
#   print get_gender("Adam")
    


