#a porgram to find the factiorial using generator


def product(a,b):
    return a*b

def fact():
    i = 1
    n = i
    while True:
        output= product(n,i)
        yield output
        i+=1
        n=output

my_gen =fact()
num=5
for i in range(num):
    print(next(my_gen))
