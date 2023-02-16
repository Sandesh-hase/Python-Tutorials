

def topten():

    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

values =topten()


print(values.__next__())
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

def top10square():
    n=1

    while n <= 10:
        sq = n*n
        yield sq            # Return terminates the fun, but yield iterates the fun
        n += 1
sq = top10square()

print("Top ten squares are:- ")
for i in sq:
    print(i)