import numpy as np
import math
from sympy import * 

def interchangeEq(indexEq1, indexEq2, matrix):
    indexeq1 = indexEq1 - 1
    indexeq2 = indexEq2 - 1
    temp = matrix[indexeq2, :]
    matrix[indexeq2, :] = matrix[indexeq1, :]
    matrix[indexeq1, :] = temp


def multScalar(indexEq, k, matrix):
    matrix[indexEq - 1, :] = k * matrix[indexEq - 1, :]


def interchangeByCombination(indexEq1, indexEq2, k1, k2, matrix):
    eq1Mod = k1 * matrix[indexEq1 - 1, :]
    eq2Mod = k2 * matrix[indexEq2 - 1, :]
    matrix[indexEq1 - 1, :] = eq1Mod + eq2Mod


def printMatrix(arr):
    toPrint = ' '
    nbRows = arr.shape[0]
    nbCols = arr.shape[1]

    for i in numpy.arange(0, nbRows, 1):
        for j in numpy.arange(0, nbCols, 1):
            toPrint += str(arr[i, j]).zfill(3) + '  '
        if i < nbRows - 1:
            toPrint += '\n '
    print(toPrint)

####################################
### HOMEWORK CHAPTER 1 #############
###   SOLUTIONS        #############
####################################

##############################
###### Section 1.1 ###########
##############################



##############################
###### Section 1.2 ###########
##############################

#######################
#### Exercise 5 #######
#######################
print('Exercise 5.')
#####
# a #
#####
A = np.array([[1, 1, 2], [3, -1, 1], [-1, 3, 4]])
b = np.array([8, 0, -4])
X = np.linalg.solve(A, b) 
print('a)', X)
x, y ,z = symbols(['x', 'y', 'z'])
system = [Eq(x + y + 2*z, 8), Eq(3*x - y + z, 0), Eq(-x + 3*y + 4*z, -4)]
solution = solve(system, [x, y, z])
print(solution)

#####
# b # Nope
#####
A = np.array([[-2,3,3], [3,-4,1], [-5,7,2]])
b = np.array([-9,5,-14])
X = np.linalg.solve(A, b) 
print('b)', X)

#####
# c #
#####
# Order of Matrix(n)
x, y, z = symbols(['x', 'y', 'z'])
system = [Eq(x + y - z , 10), Eq(-x + 4*y + 5*z , -5), Eq(x + 6*y + 3*z , 15)]
soln = solve(system, [x, y ,z])
print('c)', soln)

#####
# d #
#####
system = [Eq(x + 2*y - z , 2), Eq(2*x + 5*y - 3*z, 1), Eq(x + 4*y - 3*z, 3)]
soln = solve(system, [x, y, z])
print('d)', soln)

#########################
#### Exercise 7 #########
#########################
print('Exercise 7.')
#####
# b #
#####
x, y , z, w = symbols(['x', 'y', 'z', 'w'])
Eq1 = Eq(x - y + z - w, 0)
Eq2 = Eq(-x + y+z+w, 0)
Eq3 = Eq(x + y - z + w, 0)
Eq4 = Eq(x + y + z + w, 0)
system = [Eq1, Eq2, Eq3, Eq4]
soln = solve(system, [x, y, z, w]) 
print('b)', soln)

##########################
#### Exercise 11 #########
##########################
print('Exercise 11.')
#####
# a #
#####
A = np.array([[1, 1, 2], [3, -1, 1], [-1, 3, 4]])
r = np.linalg.matrix_rank(A)
print('a) r = ', r)
#####
# c #
#####
A = np.array([[1, 1, -1, 3], [-1, 4, 5, -2], [1, 6, 3, 4]])
r = np.linalg.matrix_rank(A)
print('c) r = ', r)
#####
# d # Nope
#####
A = np.array([[3, -2, 1, -2], [1, -1, 3, 5], [-1, 1, 1, -1]])
r = np.linalg.matrix_rank(A)
print('d) r = ', r)


