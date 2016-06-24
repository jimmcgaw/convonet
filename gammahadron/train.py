import pandas as pd
import numpy as np

import pickle
import os

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "magic04.txt")

df = pd.read_csv(filename, header=None)

record_count = df.shape[0]
attribute_count = df.shape[1]

training_set_size = int(record_count * 0.7)

# shuffle rows
df = df.reindex(np.random.permutation(df.index))

# X = df.iloc[0:record_count, [x for x in range(0, attribute_count-1)]].values
# y = df.iloc[0:record_count, attribute_count-1].values
# y = np.where(y == 'g', -1, 1)
# print sum(y)
#
#

column_range = [x for x in range(0, attribute_count-1)]

# 70% of our data goes into the training set to fit the svm
# the remaining 30% goes into the test set for verification of
# our model parameters
training_X = df.iloc[0:training_set_size, column_range].values
testing_X = df.iloc[training_set_size+1:record_count, column_range].values

training_y = df.iloc[0:training_set_size, attribute_count-1].values
training_y = np.where(training_y == 'g', -1, 1)

testing_y = df.iloc[training_set_size+1:record_count, attribute_count-1].values
testing_y = np.where(testing_y == 'g', -1, 1)


from sklearn import svm

clf = svm.SVC()
clf.fit(training_X, training_y)

# print clf.support_vectors_

correct = 0
incorrect = 0

print clf.predict(testing_X)

for index in range(0, testing_X.shape[0]):
    X = testing_X[index]
    y = testing_y[index]
    svm_prediction = clf.predict(X)
    if svm_prediction == y:
        correct += 1
    else:
        incorrect += 1

print "SVM guessed %d correctly and %d incorrectly of %d records in the test set" % (correct, incorrect, testing_X.shape[0])
# print "Accuracy is %d%" % correct * 100 / testing_X.shape[0]
