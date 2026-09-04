builtins_dict = {"__import__": __import__}
try:
    print(eval("__import__('os')", {"__builtins__": {}}, builtins_dict))
except Exception as e:
    print("Error:", e)
