import theano
import theano.tensor as T

x = T.dmatrix('x')
s = 1 / ( 1 + T.exp(-x))

logistic = theano.function([x], s)
print logistic([[0, 1], [-1, -2]])

# "keyword argument" - default value for missing argument
from theano import In
from theano import function

x, y = T.dscalars('x', 'y')
z = x + y

f = function([x, In(y, value = 5)], z)

print f(33)  # 38.0
print f(33, 7)  # 40.0

# shared variables
from theano import shared

state = shared(0)
inc = T.iscalar('inc')
accumulator = function([inc], state, updates=[(state, state+inc)])

print state.get_value() # 0
accumulator(30)
print state.get_value() # 30
accumulator(-2)
print state.get_value() # 28

state.set_value(-2)
accumulator(5)
print state.get_value() # 3

new_state = theano.shared(0)
new_accumulator = accumulator.copy(swap={state: new_state })
new_accumulator(100)
print new_state.get_value()  # 100
