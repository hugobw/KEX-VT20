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
classifiers = [DynamicWeightedMajority(n_estimators=3),
               DynamicWeightedMajority(n_estimators=5),
               DynamicWeightedMajority(n_estimators=10),
               DynamicWeightedMajority(n_estimators=20),
               DynamicWeightedMajority(n_estimators=50)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsDWM/DWM_n_estimators.csv', mode='w')
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
classifiers = [DynamicWeightedMajority(period=10),
               DynamicWeightedMajority(period=25),
               DynamicWeightedMajority(period=50),
               DynamicWeightedMajority(period=75),
               DynamicWeightedMajority(period=100)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsDWM/DWM_period.csv', mode='w')
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
classifiers = [DynamicWeightedMajority(beta=0.1),
               DynamicWeightedMajority(beta=0.25),
               DynamicWeightedMajority(beta=0.5),
               DynamicWeightedMajority(beta=0.75),
               DynamicWeightedMajority(beta=0.9)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsDWM/DWM_beta.csv', mode='w')
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
classifiers = [DynamicWeightedMajority(theta=0.01),
               DynamicWeightedMajority(theta=0.001),
               DynamicWeightedMajority(theta=0.0001),
               DynamicWeightedMajority(theta=0.05),
               DynamicWeightedMajority(theta=0.1)
               ]


classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('ResultsDWM/DWM_theta.csv', mode='w')
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
