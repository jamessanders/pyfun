from functional import *

__all__ = ["Fn","curry","combine","call","flip"]

def can_call(obj):
    if callable(obj): return obj
    else: raise TypeError("%s is not callable."%obj)

class Fn:
    """Wrapper class for functional helpers"""
    def __init__(self,fn):
        self._fn = can_call(fn)

    def __call__(self,*argv,**kwargs):
        return self._fn(*argv,**kwargs)

    def __or__(self,f2):
        return self.combine(f2)

    def __lshift__(self,*argv,**kwargs):
        try:
            return self._fn.__call__(*argv,**kwargs)
        except TypeError:
            return self.curry(*argv,**kwargs)

    def __mod__(self,*argv,**kwargs):
        return self.curry(*argv,**kwargs)

    def curry(self,*args,**keywords):
        """partially apply arguments to a function"""
        def aux(*fargs,**kwargs):
            nkw = keywords.copy()
            nkw.update(kwargs)
            return self._fn(*(args+fargs),**nkw)
        return Fn(aux)

    def combine(self,fn):
        """combine two functions into one"""
        f = can_call(fn)
        def aux(*args,**kwargs):
            return self._fn(f(*args,**kwargs))
        return Fn(aux)
    
def curry(fn,*args,**kwargs):
    return Fn(fn).curry(*args,**kwargs)

def combine(f1,f2):
    return Fn(f1).combine(can_call(f2))

def wrapFn(f): return Fn(f)

def call(fn): return can_call(fn)()


try:
    reversed
except NameError:
    def reversed(seq):
        rev = list(seq)
        rev.reverse()
        return iter(rev)

def flip(fn):
    func = can_call(fn)
    def flipped_func(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return Fn(flipped_func)
