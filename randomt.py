from theano.tensor.shared_randomstreams import RandomStreams
from theano import function

srng = RandomStreams(seed=456)
rv_u = srng.uniform((2,2))
rv_n = srng.normal((2,2))

f = function([], rv_u)
g = function([], rv_n, no_default_updates=True)
nearly_zeros = function([], rv_u + rv_u - 2 * rv_u)

f_val0 = f()
print f_val0
f_val1 = f()
print f_val1

g_val0 = g()
print g_val0
g_val1 = g()
print g_val1
