cython_usage = 1
af = None
try:
    import cython
    from add_function_cython import add_function_cython
    af = add_function_cython
except:
    cython_usage = 0
    from add_function import add_function
    af = add_function

print("Cython:", cython_usage)
print("Add Function:", af(1, 2))
