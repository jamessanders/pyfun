from pyfun import *
from operator import *

# Lets pre wrap some standard functions
mul    = Fn(mul)
add    = Fn(add)
reduce = Fn(reduce)
range  = Fn(range)

# Curry a function
add2 = add % 2

# Compose a function
add4 = add2 | add2

# Compose a function
add6 = add2 | add2 | add2

# factorial example
fac = reduce % mul | range % 1 | add % 1
       
# > fac(5)
# 120

# the above example is the same as:
#  def fac(x): 
#     return reduce(mul,range(1,x+1),1)


def part(ls):
    return (ls[0],ls[1:])

# Quicksort example using Fn as a decorator.
@Fn
def qsort(ls):   
    if ls == []: return []
    else: 
        (x,xs) = part(ls)
        return qsort (filter(Fn(lt) % x, xs)) + [x] + qsort (filter (Fn(ge) % x, xs))
