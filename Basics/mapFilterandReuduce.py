"""
map,filter not needed to import
reduce needed to import ->  from functools import reduce



"""
from functools import reduce


def cube(x):
    return x*x*x
def filter_function(a):
    return a>2


l = [1,2,4,6,4,3]
#now to do cube of each element 
nl = [x*x*x for x in l]
nm = list(map(cube,l))
print (nl) #[1, 8, 64, 216, 64, 27] 
print (nm) #[1, 8, 64, 216, 64, 27] 

newl = list(filter(filter_function,l)) #[4, 6, 4, 3]
print(newl)


print(reduce(lambda x,y : x+ y , l))#20



