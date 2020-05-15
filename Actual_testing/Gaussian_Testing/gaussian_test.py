# Imports
import csv
import sys
import numpy as np
from skmultiflow.data import FileStream
from skmultiflow.trees import HoeffdingTree
from skmultiflow.meta import AdaptiveRandomForest
from skmultiflow.meta import LearnNSE
from skmultiflow.meta import DynamicWeightedMajority
from skmultiflow.meta import OnlineBoosting
from skmultiflow.lazy import KNNAdwin
from skmultiflow.lazy import KNN
from skmultiflow.bayes import NaiveBayes
from skmultiflow.bayes import NaiveBayes
from sklearn.metrics import cohen_kappa_score

def shuffle_in_unison(a, b):
    assert len(a) == len(b)
    shuffled_a = np.empty(a.shape, dtype=a.dtype)
    shuffled_b = np.empty(b.shape, dtype=b.dtype)
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b
	 
	
def testClassifier(clf):

    result_list = [0]
    # Setting up the traning and testing stream
    trainingS = FileStream("Gaussian/training.csv")
    trainingS.prepare_for_use()

    testingS = FileStream("Gaussian/Gaussian_testing_data1.csv")
    testingS.prepare_for_use()

    testingC = FileStream("Gaussian/Gaussian_testing_priors1.csv")
    testingC.prepare_for_use()

    # Keeping track of sample count and correct prediction count
    sample_count = 0
    corrects = 0
    training_size = 20
    testing_size = 1024

    count = 0

    #trainingS.n_remaining_samples()>=training_size
    while(trainingS.n_remaining_samples()>=training_size):
        count += 1
        print("-----------------------------------")

        X, y = trainingS.next_sample(training_size)
        print(X)
        print(y)
        X, y = shuffle_in_unison(X,y)
        print(X)
        print(y)

        print("Starting first training batch nr: " + str(count))
        clf = clf.partial_fit(X, y, classes=trainingS.target_values)
        print("Done with training batch nr: " + str(count))

        print(trainingS.get_info())

        X, y = testingS.next_sample(testing_size)

        prediction = clf.predict(X)
        prediction = [ np.sum(prediction == i+1) for i in range(4)]
        print(prediction)

        Xp, Yp = testingC.next_sample(1)
        dist = [int(i * 1024) for i in Xp[0] ]




        if prediction is not None:

            acc = dist = [min(i,j) for i,j in zip(dist, prediction) ]
            print(acc)

            corrects += sum(acc)


        sample_count += testing_size
        print('Classifier batch performance: ' + str( sum(acc) / testing_size) )
        result_list.append(sum(acc) / testing_size)
        print('Classifier total performance: ' + str( corrects / sample_count) )


    # Displaying the results


    print("-----------------------------------")
    print('Classifier total performance: ' + str(corrects / sample_count))
    result_list.append(corrects / sample_count)
    return result_list
