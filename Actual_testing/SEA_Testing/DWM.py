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
from sea_test import testClassifier


#clf =NaiveBayes()
#clf = DynamicWeightedMajority()
#clf = AdaptiveRandomForest(n_estimators=30)
#clf = KNNAdwin(max_window_size = sample_size)

#insert instances of the classifier that you wanna test here and try diffrent parameters
classifiers = [DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75),
               DynamicWeightedMajority(n_estimators=10, beta = 0.5, period = 75)
               ]
classifier_performance = [[]]
for i in classifiers:
    a = testClassifier(i)
    classifier_performance.append(a)

output_file = open('Results/DWM.csv', mode='w')
output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for j in range(len(classifier_performance[1])):
	output_file.writerow([
                         round(classifier_performance[1][j],6),
                         round(classifier_performance[2][j],6),
                         round(classifier_performance[3][j],6),
                         round(classifier_performance[4][j],6),
                         round(classifier_performance[5][j],6),
                         round(classifier_performance[6][j],6),
                         round(classifier_performance[7][j],6),
                         round(classifier_performance[8][j],6),
                         round(classifier_performance[9][j],6),
                         round(classifier_performance[10][j],6),
                         round(classifier_performance[11][j],6),
                         round(classifier_performance[12][j],6),
                         round(classifier_performance[13][j],6),
                         round(classifier_performance[14][j],6),
                         round(classifier_performance[15][j],6),
                         round(classifier_performance[16][j],6),
                         round(classifier_performance[17][j],6),
                         round(classifier_performance[18][j],6),
                         round(classifier_performance[19][j],6),
                         round(classifier_performance[20][j],6)
                         ])


for j in classifier_performance:
    print(j)

