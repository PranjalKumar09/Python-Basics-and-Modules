#doc string are the string literals that appear right after the defination of funciton , method , class of module
"""dir function in phthon to get all function available in module in list
it must have import math not like from math ... """
from math import pi, sqrt as s
import math

result = s(9) * pi
print(result) #9.42477796076938

print(dir(math)) #['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
print(type(math.ceil)) #<class 'builtin_function_or_method'>


def squares(n):
    '''takes number n , returns the
    square of n'''
    print(n ** 2)
squares(5)
print(squares.__doc__)


def squares2(n):
    print(n ** 2)
    '''takes number n , returns the
    square of n'''
    
print(squares2.__doc__) #none
    


#index works both in list and tuple ... .index(value , startindex(optional), endindex(optional))

list1 = [1,2,4,5,6,7,2,8,11,23,1,23,42,3,54,5,4]
print(list1.index(1,6))

tuple1 = (4,5,6,7,2,8,11,23,1,23,42,3,54,5,4)
print(tuple1.index(1,6))


letter = "Hey my name is {1} and I am from {0}"
count = "India"
name = "Kumar"

print(letter.format(count,name))

print(f"Hey my name is {name} and I am from {count}" )
print(f"Hey my name is {{name}} and I am from {count}" )

