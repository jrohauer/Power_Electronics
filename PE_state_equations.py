#Program to calculate state equations for power convertors

import sympy
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
import numpy as np

L, R, C, d, s, iL, Vc, Vg, w = sympy.symbols('L,R ,C,d,s, iL, Vc,Vg,w')

I = eye(2)
x = Matrix([iL,Vc])
u = Matrix([Vg])

# Buck Converter
a1 = Matrix(([0,-1/L ],[ 1/C, -1/(R*C)]))
a2 = Matrix(([0,-1/L ],[ 1/C, -1/(R*C)]))
A = sympy.simplify(d*a1 + (1-d)*a2)

b1 = Matrix(([1/L],[0]))
b2 = Matrix(([0],[0]))
B = sympy.simplify(d*b1 + (1-d)*b2)

c1 = Matrix([[0, 1]])
c2 = Matrix([[0, 1]])
CM = sympy.simplify(d*c1 + (1-d)*c2)

#Buck calcs
X = -A.inv()*B*u
Ainv = (s*I-A).inv()
x_u = Ainv*B
y_u = CM*Ainv*B
y_d = CM*Ainv* ((a1-a2)*X+(b1-b2 )*u)+(c1-c2 )*X
x_d = Ainv* ((a1-a2)*X+(b1-b2 )*u)


#Boost Converter
a1 = Matrix(([0, 0], [0 ,-1/(R*C)]))
a2 = Matrix(([0, -1/L], [1/C ,-1/(R*C)]))
A = sympy.simplify(d*a1 + (1-d)*a2)

b1 = Matrix(([1/L],[0]))
b2 = Matrix(([1/L],[0]))
B = sympy.simplify(d*b1 + (1-d)*b2)

c1 = Matrix([[0, 1]])
c2 = Matrix([[0, 1]])
CM = sympy.simplify(d*c1 + (1-d)*c2)

#Boost calcs
X = -A.inv()*B*u
Ainv = (s*I-A).inv()
x_u = Ainv*B
y_u = CM*Ainv*B
y_d = CM*Ainv* ((a1-a2)*X+(b1-b2 )*u)+(c1-c2 )*X
x_d = Ainv* ((a1-a2)*X+(b1-b2 )*u)



# BuckBoost Converter
a1 = Matrix(([0, 0], [0 ,-1/(R*C)]))
a2 = Matrix(([0, -1/L], [1/C ,-1/(R*C)]))
A = sympy.simplify(d*a1 + (1-d)*a2)

b1 = Matrix(([1/L],[0]))
b2 = Matrix(([0],[0]))
B = sympy.simplify(d*b1 + (1-d)*b2)

c1 = Matrix([[0, 1]])
c2 = Matrix([[0, 1]])
CM = sympy.simplify(d*c1 + (1-d)*c2)

# BuckBoost calcs
X = -A.inv()*B*u
Ainv = (s*I-A).inv()
x_u = Ainv*B
y_u = CM*Ainv*B
y_d = CM*Ainv* ((a1-a2)*X+(b1-b2 )*u)+(c1-c2 )*X
x_d = Ainv* ((a1-a2)*X+(b1-b2 )*u)