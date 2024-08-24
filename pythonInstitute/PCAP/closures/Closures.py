
def outer(par):
    loc = par

    def inner():
        return loc
    return inner

fun_obj = outer(5)
print(fun_obj())
