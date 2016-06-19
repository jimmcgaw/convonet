import numpy as np

a = np.arange(9).reshape(3, 3)

print "A"
print a
print a.shape
print a.itemsize # 9

# 3 X 3 multiplicative identity matrix
i = np.identity(3)

print "Identity"
print i
print i.shape

print "A * Indentity"
print np.dot(a, i)


complicated = np.array( [ [1,2], [3,4] ], dtype=complex )
print "Complex matrix"
print complicated


print np.array([[1,2], [3,4]]) + np.array([[4,3], [2,1]])

print "3-D Array"
print np.arange(24).reshape(2,3,4)
