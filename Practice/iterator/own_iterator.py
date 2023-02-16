class CustomTopTenIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = CustomTopTenIterator()

print(values.__next__())
print(next(values))

for i in values:  # iterator is values, so it will pick the values from 3 in the for loop without repeating
    print(i)