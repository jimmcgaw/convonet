import numpy
import theano.tensor as T
from theano import function

# x and y are statically typed zero-dimensional scalars
# that are double; type is TensorVariable
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y

f = function([x, y], z)

print f(2, 3)  # 5.0

# a and b are matrices of doubles.
a = T.dmatrix('a')
b = T.dmatrix('b')
c = a + b

f = function([a, b], c)

print f([[1, 2], [3, 4]], [[10, 20], [30, 40]])
