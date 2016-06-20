import pandas as pd
import numpy as np

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# shuffle rows
df = df.reindex(np.random.permutation(df.index))

from mlp import MultiLayerPerceptron


X = df.iloc[0:150, [0, 1, 2, 3]].values
y = df.iloc[0:150, 4].values


training_X = df.iloc[0:100, [0, 1, 2, 3]].values
testing_X = df.iloc[101:150, [0, 1, 2, 3]].values

training_y = df.iloc[0:100, 4].values
training_y = np.where(training_y == 'Iris-setosa', -1, 1)

testing_y = df.iloc[101:150, 4].values
testing_y = np.where(testing_y == 'Iris-setosa', -1, 1)

perceptron = MultiLayerPerceptron(iteration_count=100)
perceptron.fit(training_X, training_y)

print perceptron.w_  # final parameters
print ""

print "Predicted"
print perceptron.predict(testing_X)
print ""

print "Actual"
print testing_y
