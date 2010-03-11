About
-----

PyFun provides a few useful functions for composing functions quickly.

Example
-------

    from pyfun import *

    add = Fn(lambda a,b: a + b)

    # Curry a function
    add2 = add % 2

    # Compose a function
    add4 = add2 | add2

    # Compose a function
    add6 = add2 | add2 | add2



