import numpy as np
import math
from sympy import * 

################################# 
##### Example with sympy ########
#################################

##################################
# We want to solve the following #
# system of linear equations     #
#                                #
#     -2x + 3y + 3z = -9         #
#      3x - 4y +  z =  5         #
#     -5x + 7y + 2z = -14        #
#                                #
##################################

# Step 1: Create the symbols for
# the variables
x, y , z = symbols(['x', 'y', 'z'])

# Step 2: Create the equations with
# the method Eq(left_Side,right_Side)
Eq1 = Eq(-2*x + 3*y + 3*z, -9)
Eq2 = Eq(3*x - 4*y + z, 5)
Eq3 = Eq(-5*x + 7*y + 2*z, -14)
print(Eq1)

# Step 3: Create the system
system = [Eq1, Eq2, Eq3]
print(system)

# Step 4: Use the method solve to
# solve the system
solution = solve(system, [x, y, z])

# Print the solution
print(solution)