def div(a,b):
    print(a/b)

# div(6,2)
# Fun that act as a decorator to swap values if num is greater than denom
def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div=smart_div(div)
div(3,6)