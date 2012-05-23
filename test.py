import numpy as np
import ctypes

# Load C functions into Python
# Make sure to compile test.c into a .so file first
# gcc -shared -fPIC test.c -o test.so
lib = ctypes.cdll['./test.so']
fib = lib['fib']
doubleme = lib['doubleme']

# We use a C library function from Python
print "fib(5) = ", fib(5)

# Allocate an array of double in Python using NumPy
A = np.array([1, 1.5, 2, 5])

print "A before doubling", A
print "A's location in memory: %d"%A.ctypes.data
doubleme(A.ctypes.data, len(A))
print "A after doubling", A
