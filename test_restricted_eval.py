import builtins
def safe_eval(code, globals_dict, locals_dict):
    safe_builtins = {
        name: getattr(builtins, name)
        for name in [
            "int", "str", "float", "bool", "list", "dict", "set", "tuple",
            "bytes", "bytearray", "complex", "frozenset", "memoryview",
            "type", "object", "None", "True", "False", "NotImplemented", "Ellipsis"
        ]
    }

    # We shouldn't modify the caller's globals_dict permanently, so we create a copy
    new_globals = dict(globals_dict)
    new_globals["__builtins__"] = safe_builtins

    return eval(code, new_globals, locals_dict)

try:
    print(safe_eval("__import__('os').system('echo VULNERABLE')", {}, {}))
except Exception as e:
    print("Caught:", type(e), e)

try:
    print(safe_eval("int | str", {}, {}))
except Exception as e:
    print("Caught:", type(e), e)
