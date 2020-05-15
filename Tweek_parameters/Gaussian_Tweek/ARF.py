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
classifiers = [AdaptiveRandomForest(n_estimators=3),
               AdaptiveRandomForest(n_estimators=5),
               AdaptiveRandomForest(n_estimators=10),
               AdaptiveRandomForest(n_estimators=20),
               AdaptiveRandomForest(n_estimators=40)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsARF/ARF_n_estimators.csv', mode='w')
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

classifiers = [AdaptiveRandomForest(),
               AdaptiveRandomForest(drift_detection_method=None),
               AdaptiveRandomForest(warning_detection_method=None),
               AdaptiveRandomForest(warning_detection_method=None, drift_detection_method=None)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsARF/ARF_driftandwarning.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6)
                         ])


for j in classifier_performance:
    print(j)
classifiers = [AdaptiveRandomForest(grace_period=50),
               AdaptiveRandomForest(grace_period=25),
               AdaptiveRandomForest(grace_period=10),
               AdaptiveRandomForest(grace_period=75),
               AdaptiveRandomForest(grace_period=100)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsARF/ARF_grace_period.csv', mode='w')
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
classifiers = [AdaptiveRandomForest(split_confidence=0.01),
               AdaptiveRandomForest(split_confidence=0.005),
               AdaptiveRandomForest(split_confidence=0.1),
               AdaptiveRandomForest(split_confidence=0.05)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsARF/ARF_split_confidence.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6)
                         ])


for j in classifier_performance:
    print(j)
classifiers = [AdaptiveRandomForest(leaf_prediction='nba'),
               AdaptiveRandomForest(leaf_prediction='nb'),
               AdaptiveRandomForest(leaf_prediction='mc')
               ]


classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsARF/ARF_leaf_prediction.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6)
                         ])


for j in classifier_performance:
    print(j)
