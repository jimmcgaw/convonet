import theano

a = theano.tensor.vector('a')
b = a + a ** 10
f = theano.function([a], b)

print f([0,1,2])
