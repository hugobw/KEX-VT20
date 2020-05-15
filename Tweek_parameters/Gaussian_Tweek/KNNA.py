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
from sklearn.metrics import cohen_kappa_score
from gaussian_test import testClassifier


#clf =NaiveBayes()
#clf = DynamicWeightedMajority()
#clf = AdaptiveRandomForest(n_estimators=30)
#clf = KNNAdwin(max_window_size = sample_size)

#insert instances of the classifier that you wanna test here and try diffrent parameters
classifiers = [KNNAdwin(n_neighbors=1),
               KNNAdwin(n_neighbors=3),
               KNNAdwin(n_neighbors=5),
               KNNAdwin(n_neighbors=10),
               KNNAdwin(n_neighbors=20)
               ]

classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsKNN/KNNA_n_neighbors.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6),
                         round(classifier_performance[5][j],6)
                         ])


for j in classifier_performance:
    print(j)

classifiers = [KNNAdwin(max_window_size=50),
               KNNAdwin(max_window_size=100),
               KNNAdwin(max_window_size=300),
               KNNAdwin(max_window_size=500),
               KNNAdwin(max_window_size=1000),
               KNNAdwin(max_window_size=2000)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsKNN/KNNA_max_window_size.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6),
                         round(classifier_performance[5][j],6),
                         round(classifier_performance[6][j],6)
                         ])


for j in classifier_performance:
    print(j)
classifiers = [KNNAdwin(leaf_size=10),
               KNNAdwin(leaf_size=20),
               KNNAdwin(leaf_size=30),
               KNNAdwin(leaf_size=40),
               KNNAdwin(leaf_size=50)
               ]


classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsKNN/KNNA_leaf_size.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6),
                         round(classifier_performance[5][j],6)
                         ])


for j in classifier_performance:
    print(j)
