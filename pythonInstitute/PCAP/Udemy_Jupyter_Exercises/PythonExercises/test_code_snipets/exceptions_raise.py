try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(e)
    print(e.args)
    print(len(e.args))
