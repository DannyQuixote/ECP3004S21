# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:19:35 2021

@author: danny
"""

def quad_roots_1(a:float, b: float, c: float)->float: 
    """Give the roots to a quadratic equation
    >>>quad_roots_1 (3,3,3)
    
    >>>quad_roots_1 (1,1,1)
    
    >>>quad_roots_1 (2,2,2)
    
    """
    x1 = -b + (b**2-4*a*c)**(1/2)
    x1 = x1 / (2*a)
    x2 = -b - (b**2-4*a*c)**(1/2)
    x2 = x2 / (2*a)
    return [x1, x2]

print(quad_roots_1(3,3,3))
print(quad_roots_1(1,1,1))
print(quad_roots_1(2,2,2))





def quad_roots_real(a: float, b: float, c: float)->float:
    """ Returns the real roots of a quad. equation and tells you if its negative.
    >>>quad_roots_real(1,1,1)
    
    >>>quad_roots_real(2,2,2)
    
    >>>quad_roots_real(3,3,3)
    """
    if b**2-4*a*c < 0: 
        print("NO!!! THE DISCRIMINANT IS NEGATIVE!!!")
        return None
    x1= -b + (b**2-4*a*c)**(1/2)
    x1= x1 / (2*a)
    x2 = -b - (b**2-4*a*c)**(1/2)
    x2= x2 / (2**a)
    return [x1,x2]

print(quad_roots_real(1,1,1))
print(quad_roots_real(2,2,2))
print(quad_roots_real(3,3,3))



def utility_positive(x: float, y: float, a: float)->float:
    if x < 0 or a < 0 :
        print("ERROR: x is negative!")
    if y < 0:
        print("ERROR: y is negative!")
    if a < 0: 
        print("ERROR: a is negative!")
        return None 
    return (x**a)*y**(1-a)

""" 
 Returning the answer a positive utility 
 
>>>utility_positive(2,2,-2)
ERROR: a is negative!
 None

>>>utility_positive(2,-2,-2)

ERROR: y is negative!
ERROR: a is negative! 
 None

>>> utility_positive(-2,-2,-2)
ERROR: x is negative!
ERROR: y is negative!
ERROR: a is negative! 
 None
"""

print(utility_positive(2,2-2))
print(utility_positive(2,2,-2))
print(utility_positive(-2,-2,-2))



import math

def logit_like(y: int, x: float, B0: float, B1: float)->float:
    """Return value of log likelihood and logit function with values 
    y,x,B0.B1
    
    >>>logit_like(1,1,1,1)
    
    >>>logit_like(2,2,2,2)
    
    >>>logit_like(3,3,3,3)"""
    val = pow(2.71828,B0 +x * B1)
    val = math.log(val / (1+val))
    if y==0: 
        return 1-val
    if y== 1: 
        return val 
    

print(logit_like(1, 1, 1, 1))
print(logit_like(2, 2, 2, 2))
print(logit_like(3, 3, 3, 3))




print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1(3, 3, 3)")
print("Expected: " + str([-.5, -.87]))
print("Got: " + str(quad_roots_1(3,3,3)))


print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
 
print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(1, 1, 1)")
print("Expected: " + str("NO!!! THE DISCRIMINANT IS NEGATIVE!!!"))
print("Got: " + str(quad_roots_real(1, 1, 1)))


print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(2, 2, -2)")
print("Expected: " + str("ERROR: a is negative!"))
print("Got: " + str(utility_positive(2, 2, -2)))



print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")
   
print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1, 1, 1, 1)")
print("Expected: " + str(1.0485874472772614))
print("Got: " + str(logit_like(1, 1, 1, 1)))



