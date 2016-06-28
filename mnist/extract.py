import cPickle, gzip, numpy

# Load the dataset
with gzip.open('mnist.pkl.gz', 'rb') as f:
    train_set, valid_set, test_set = cPickle.load(f)

vectors = train_set[0]
labels = train_set[1]

test_vectors = test_set[0]
test_labels = test_set[1]


first_digit = vectors[0]
print first_digit
print "is a "
print labels[0]


# CNN preprocessing
# first_digit_matrix = first_digit.reshape(28, 28)
# print first_digit_matrix
