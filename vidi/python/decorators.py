# pyright: basic
# In basic mode, pyright will still allow Unknowns within types.
# when pyright: strict is specified instead, Unknowns will be disallowed.

# Objective of exercise:
# Learn about the different kinds of decorators and how to declare them.

from typing import Callable, Generic, TypeVar
from functools import wraps

T = TypeVar('T')

# In Python, decorators are callables that wrap an object.
# Other languages call this pattern higher-order functions (HOFs).
# Classes can also be implemented as decorators.

# Mark the parameter to clarify that this annotation can only receive callables
# (functions, methods, etc.)
# Without a return type, annotations are expected to return a transparent wrapper over "fun".


def hello(fun):
    @wraps(fun)  # Copies the runtime attributes of "fun" over to "_fun"
    def _fun(*args, **kw):
        # Delegate all arguments to "fun"
        print(f'Hello from {fun.__name__}!')
        return fun(*args, **kw)
    return _fun


@hello
def foo():
    print("It's foo.")


@hello
def complex(named_arg=True):
    print(f'{named_arg=}')

# Replicate Rust's conditional attribute.
# One difference of this approach is that even if cond is falsy,
# the item will still be in scope.


def cfg(cond):
    if cond:
        # Type parameters are required to maintain the original type.
        def _identity(i: T) -> T: return i
        return _identity
    else:
        def _void(_): return None
        return _void


@cfg(True)
def bar(who='Stranger'):
    print(f'Hello from bar, {who}')


@cfg(False)
class NoneClassButStillInScope:
    pass


class greet:
    def __init__(self, value=None):
        self.value = value

    def __call__(self, fun: Callable):
        @wraps(fun)
        def _fun(*args, **kw):
            print(f'Hi there, my value is {self.value}')
            return fun(*args, **kw)
        return _fun

# In a similar vein, we can conditionally attach decorators.


def cfg_attr(cond, *decos: Callable):
    """ If "cond" is true, apply "decos" onto the target."""
    if cond:
        def _collapse(fun):
            for deco in reversed(decos):  # in order of declaration
                fun = deco(fun)
            return fun
        return _collapse
    else:
        def _identity(fun): return fun
        return _identity


@greet('Unconditionally')
@cfg_attr(
    True,
    hello,
    greet(),
    greet(1),
    greet(False)
)
def baz():
    print('baz is away...')
    return 123


if __name__ == '__main__':
    foo()
    complex()
    if bar:
        bar()
    if NoneClassButStillInScope:
        print('this line is never printed')
    ret = baz()
