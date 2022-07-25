# Custom safe_eval module for untrusted code execution
# Tailor-made for the survey module

"""
(custom) safe-compile module - methods intended to provide security to evaluate/compile untrusted code

Methods in this module are typically used as alternatives to eval() 
to parse simple user-defined functions in the survey module.

The idea is to create a class that wraps around the solution given by the survey candidate,
while restricting imports and some operations

IMPORTANT NOTE: This solution is not optimal. The best solution would be to sandbox Python in a VM,
But this is one way to use only Odoo's dependencies.

"""

import dis
import functools
from types import CodeType
from opcode import opname
import traceback

from odoo.loglevels import ustr
from odoo.tools import safe_eval

__all__ = ['safe_compile',]

#typical modules used for data structures training
_ALLOWED_MODULES = ['math', 'time', 'queue', 'collections']

_BLACKLIST = set(safe_eval.to_opcodes([
    #import *
    'IMPORT_STAR',
    #setting attributes
    'STORE_ATTR', 'DELETE_ATTR',
    'STORE_GLOBAL', 'DELETE_GLOBAL',
]))

_CONST_OPCODES = set(safe_eval.to_opcodes([
    # stack manipulations
    'POP_TOP', 'ROT_TWO', 'ROT_THREE', 'ROT_FOUR', 'DUP_TOP', 'DUP_TOP_TWO',
    'LOAD_CONST',
    'RETURN_VALUE', # return the result of the literal/expr evaluation
    # literal collections
    'BUILD_LIST', 'BUILD_MAP', 'BUILD_TUPLE', 'BUILD_SET',
    # 3.6: literal map with constant keys https://bugs.python.org/issue27140
    'BUILD_CONST_KEY_MAP',
    'LIST_EXTEND', 'SET_UPDATE',
])) - _BLACKLIST

_EXPR_OPCODES = _CONST_OPCODES.union(safe_eval.to_opcodes([
    'UNARY_POSITIVE', 'UNARY_NEGATIVE', 'UNARY_NOT', 'UNARY_INVERT',
    *('BINARY_' + op for op in safe_eval._operations), 'BINARY_SUBSCR',
    *('INPLACE_' + op for op in safe_eval._operations),
    'BUILD_SLICE',
    # comprehensions
    'LIST_APPEND', 'MAP_ADD', 'SET_ADD',
    'COMPARE_OP',
    # specialised comparisons
    'IS_OP', 'CONTAINS_OP',
    'DICT_MERGE', 'DICT_UPDATE',
    # Basically used in any "generator literal"
    'GEN_START',  # added in 3.10 but already removed from 3.11.
])) - _BLACKLIST

_SAFE_OPCODES = _EXPR_OPCODES.union(safe_eval.to_opcodes([
    'POP_BLOCK', 'POP_EXCEPT',

    # note: removed in 3.8
    'SETUP_LOOP', 'SETUP_EXCEPT', 'BREAK_LOOP', 'CONTINUE_LOOP',

    'EXTENDED_ARG',  # P3.6 for long jump offsets.
    'MAKE_FUNCTION', 'CALL_FUNCTION', 'CALL_FUNCTION_KW', 'CALL_FUNCTION_EX',
    # Added in P3.7 https://bugs.python.org/issue26110
    'CALL_METHOD', 'LOAD_METHOD',

    'LOAD_BUILD_CLASS', 'IMPORT_NAME', 'IMPORT_FROM'

    'GET_ITER', 'FOR_ITER', 'YIELD_VALUE',
    'JUMP_FORWARD', 'JUMP_ABSOLUTE',
    'JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE',
    'SETUP_FINALLY', 'END_FINALLY',
    # Added in 3.8 https://bugs.python.org/issue17611
    'BEGIN_FINALLY', 'CALL_FINALLY', 'POP_FINALLY',

    'RAISE_VARARGS', 'LOAD_NAME', 'STORE_NAME', 'DELETE_NAME', 'LOAD_ATTR',
    'LOAD_FAST', 'STORE_FAST', 'DELETE_FAST', 'UNPACK_SEQUENCE',
    'STORE_SUBSCR',
    'LOAD_GLOBAL',

    'RERAISE', 'JUMP_IF_NOT_EXC_MATCH',
])) - _BLACKLIST

def assert_no_unsafe_attrs(code_obj, expr):
    """ assert_no_unsafe_attrs(code_obj, expr) -> None

    Asserts that the code object does not refer to any unsafe attributes, 
    so that safe_eval prevents access to any internal-ish Python
    attribute or method (both are loaded via LOAD_ATTR which uses a name, not a
    const or a var).

    Checks that no such name exists in the provided code object (co_names).

    :param code_obj: code object to name-validate
    :type code_obj: CodeType
    :param str expr: expression corresponding to the code object, for debugging
                     purposes
    :raises NameError: in case a forbidden name
                       is found in ``code_obj``

    """
    for name in code_obj.co_names:
        if name in safe_eval._UNSAFE_ATTRIBUTES:
            raise NameError('Access to forbidden name %r (%r)' % (name, expr))

def assert_valid_codeobj(allowed_codes, code_obj, expr):
    """ Asserts that the provided code object validates against the bytecode
    and name constraints.

    Recursively validates the code objects stored in its co_consts in case
    lambdas are being created/used (lambdas generate their own separated code
    objects and don't live in the root one)

    :param allowed_codes: list of permissible bytecode instructions
    :type allowed_codes: set(int)
    :param code_obj: code object to name-validate
    :type code_obj: CodeType
    :param str expr: expression corresponding to the code object, for debugging
                     purposes
    :raises ValueError: in case of forbidden bytecode in ``code_obj``
    :raises NameError: in case a forbidden name (containing two underscores)
                       is found in ``code_obj``
    """
    assert_no_unsafe_attrs(code_obj, expr)

    # set operations are almost twice as fast as a manual iteration + condition
    # when loading /web according to line_profiler
    code_codes = {i.opcode for i in dis.get_instructions(code_obj)}
    if not allowed_codes >= code_codes:
        raise ValueError("forbidden opcode(s) in %r: %s" % (expr, ', '.join(opname[x] for x in (code_codes - allowed_codes))))

    for const in code_obj.co_consts:
        if isinstance(const, CodeType):
            assert_valid_codeobj(allowed_codes, const, 'lambda')

def test_expr(expr, allowed_codes, mode="exec"):
    try:
        code_obj = compile(expr, "<string>", mode)
    except (SyntaxError, IndentationError):
        raise
    except Exception as e:
        raise ValueError('"%s" while compiling\n%r' % (ustr(e), expr))
    assert_valid_codeobj(allowed_codes, code_obj, expr)
    return code_obj

def unsafe_eval(class_, method_name, args):
    """
    unsafe_eval(class_, method_name, args)
    Evaluation of a class method (assuming it 
    went through all the filters defined in this module)
    """
    try:
        error = ''
        code_output = getattr(class_, method_name)(*args)
    except:
        code_output = ''
        error = traceback.format_exc()
    return code_output, error

def _import(name, globals=None, locals=None, fromlist=None, level=-1):
    if globals is None:
        globals = {}
    if locals is None:
        locals = {}
    if fromlist is None:
        fromlist = []
    if name in _ALLOWED_MODULES:
        return __import__(name, globals, locals, level)
    raise ImportError(name)

_BUILTINS = {
    '__import__': _import,
    'True': True,
    'False': False,
    'None': None,
    'bytes': bytes,
    'str': str,
    'unicode': str,
    'bool': bool,
    'int': int,
    'float': float,
    'enumerate': enumerate,
    'dict': dict,
    'list': list,
    'tuple': tuple,
    'map': map,
    'abs': abs,
    'min': min,
    'max': max,
    #TODO this print stays here for debugging purposes, 
    # but the user can't really use this feature 
    # for the moment
    'print': print,
    'sum': sum,
    'reduce': functools.reduce,
    'filter': filter,
    'sorted': sorted,
    'round': round,
    'len': len,
    'repr': repr,
    'set': set,
    'all': all,
    'any': any,
    'ord': ord,
    'chr': chr,
    'divmod': divmod,
    'isinstance': isinstance,
    'range': range,
    'xrange': range,
    'zip': zip,
    'Exception': Exception,
}
def safe_compile(expr, globals_dict=None, locals_dict=None, mode="exec", nocopy=False, locals_builtins=False):
    """safe_compile(expression[, globals[, locals[, mode[, nocopy]]]]) -> code_obj

    System-restricted Python class compilation

    Evaluates a string that contains an expression that mostly
    uses class definitions (along with method definitions), 
    uses Python constants, arithmethic expressions, and typical
    data structures libraries for algorithm design and
    objects directly provided in context.

    This can be used to e.g. 
    evaluate code provided by an untrusted source
    for a code interview challenge in the survey module

    :throws TypeError: If the expression provided is a code object
    :throws SyntaxError: If the expression provided is not valid Python
    :throws NameError: If the expression provided accesses forbidden names
    :throws ValueError: If the expression provided uses forbidden bytecode
    """
    if type(expr) is CodeType:
        raise TypeError("safe_compile does not allow direct evaluation of code objects.")

    # prevent altering the globals/locals from within the sandbox
    # by taking a copy.
    if not nocopy:
        # isinstance() does not work below, we want *exactly* the dict class
        if (globals_dict is not None and type(globals_dict) is not dict) \
                or (locals_dict is not None and type(locals_dict) is not dict):
            safe_eval._logger.warning(
                "Looks like you are trying to pass a dynamic environment, "
                "you should probably pass nocopy=True to safe_eval().")
        if globals_dict is not None:
            globals_dict = dict(globals_dict)
        if locals_dict is not None:
            locals_dict = dict(locals_dict)

    safe_eval.check_values(globals_dict)
    safe_eval.check_values(locals_dict)

    if globals_dict is None:
        globals_dict = {}

    globals_dict['__builtins__'] = _BUILTINS
    if locals_builtins:
        if locals_dict is None:
            locals_dict = {}
        locals_dict.update(_BUILTINS)
    code_obj = test_expr(expr, _SAFE_OPCODES, mode=mode)
    code_obj_config = {
        'code_obj': code_obj,
        'globals_dict': globals_dict,
        # NOTE is this locals necessary??
        'locals_dict': locals_dict}
    return code_obj_config
