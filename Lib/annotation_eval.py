import ast

def _is_safe_type_node(node):
    """
    Recursively verify if an AST node is safe for type hint evaluation.
    Allowed operations: names, attributes, subscripts, lists, tuples, operators used in types (|, ~).
    Function calls are generally blocked unless we want to allow specifically safe ones.
    For type annotations, we'll allow Constant, Name, Attribute, Tuple, List, Subscript,
    BinOp (BitOr), UnaryOp (Invert), Set, Dict.
    We also allow Calls, but we should make sure they don't do RCE.
    Actually, preventing RCE with `eval` usually means removing `__builtins__` or limiting it,
    but `ForwardRef` explicitly merges `builtins.__dict__`.
    """
    pass
