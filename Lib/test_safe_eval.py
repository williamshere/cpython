import ast

def safe_eval_type(node, globals_dict, locals_dict):
    if isinstance(node, ast.Expression):
        return safe_eval_type(node.body, globals_dict, locals_dict)
    elif isinstance(node, ast.Name):
        if node.id in locals_dict: return locals_dict[node.id]
        if node.id in globals_dict: return globals_dict[node.id]
        import builtins
        if hasattr(builtins, node.id): return getattr(builtins, node.id)
        raise NameError(f"name '{node.id}' is not defined")
    elif isinstance(node, ast.Attribute):
        value = safe_eval_type(node.value, globals_dict, locals_dict)
        return getattr(value, node.attr)
    elif isinstance(node, ast.Subscript):
        value = safe_eval_type(node.value, globals_dict, locals_dict)
        slice_val = safe_eval_type(node.slice, globals_dict, locals_dict)
        return value[slice_val]
    elif isinstance(node, ast.Tuple):
        return tuple(safe_eval_type(elt, globals_dict, locals_dict) for elt in node.elts)
    elif isinstance(node, ast.List):
        return list(safe_eval_type(elt, globals_dict, locals_dict) for elt in node.elts)
    elif isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = safe_eval_type(node.left, globals_dict, locals_dict)
        right = safe_eval_type(node.right, globals_dict, locals_dict)
        if isinstance(node.op, ast.BitOr):
            return left | right
        raise ValueError(f"Unsupported BinOp: {type(node.op)}")
    elif isinstance(node, ast.UnaryOp):
        operand = safe_eval_type(node.operand, globals_dict, locals_dict)
        if isinstance(node.op, ast.Invert):
            return ~operand
        raise ValueError(f"Unsupported UnaryOp: {type(node.op)}")
    else:
        raise ValueError(f"Unsupported AST node: {type(node)}")

print("Defined.")
