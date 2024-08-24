
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x, end='')



# By using yield, fun() becomes a generator object.
def fun(n):
    for i in range(n):
        yield i


for i in fun(5):
    print(i)


