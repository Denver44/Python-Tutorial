# ----------------------------------------------- FUNCTIONS -------------------------------------------------
# NOTE: docstring help us to know more about your functions

def func(a, b):
    """This is a function which takes to two values and give average of it."""  # docstring it should be written at the top
    c = (a + b) / 2
    return c


res = func(500, 600)
print(res)
print(func.__doc__)  # This gives the doctsring of the function (varname.__doc__)
