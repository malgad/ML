#! /usr/bin/env python3
 # how to run:
#    pytest-3 matrixmult.py
import numpy as np

def multiply(a, b):
    matrix = [[0 for y in range(len(b[0]))] for x in range(len(a))]

    if len(a[0]) != len(b):
        Exception
    else:
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    matrix[i][j]+= a[i][k]*b[k][j]
    return matrix
    pass

#print(multiply([[1, 2, 3], [4, 5, -7]],  [[3, 0, 4], [2, 5, 1], [-1, -1, 0]]))

def multiplyWithNumpy(a, b):
    return np.matmul(a,b)
    pass

testdata = [
    ([[3]], [[6]], [[18]]),
    ([[1, 2]],   [[3], [4]], [[11]]),
    ([[1, 2, 3], [4, 5, -7]],  [[3, 0, 4], [2, 5, 1], [-1, -1, 0]],  [[4, 7, 6], [29, 32, 21]])
]
multiplicationFunc = [multiply, multiplyWithNumpy]
def test_multiply(multiplicationFunc, a, b, expected):
    assert np.array_equal(multiplicationFunc(a, b), expected)
testdataImpossibleProducts = [
    ([[3, 4]], [[6, 7]]),
    ([[1, 2]], [[3, 4], [4, 5], [5, 6]])
]
def test_multiplyIncompatibleMatrices(multiplicationFunc, a, b):
    with pytest.raises(Exception) as e:
        multiplicationFunc(a, b)
for func in multiplicationFunc:
    for a, b, expected in testdata:
        test_multiply(func, a, b, expected)
for func in multiplicationFunc:
    for a, b in testdataImpossibleProducts:
        try:
            test_multiply(func, a, b)
            assert False
        except:
            pass