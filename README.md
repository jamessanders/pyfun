About
-----

PyFun provides a few useful functions for composing functions quickly.

Example
-------

    from pyfun import *
    from operator import *

    add = Fn(lambda a,b: a + b)

    # Curry a function
    add2 = add % 2

    # Compose a function
    add4 = add2 | add2

    # Compose a function
    add6 = add2 | add2 | add2

    # factorial example
    fac = Fn(reduce) % mul | Fn(range) % 1 | Fn(add) % 1
       
    # > fac(5)
    # 120

    # the above example is the same as:
    #  def fac(x): 
    #     return reduce(mul,range(1,x+1),1)

