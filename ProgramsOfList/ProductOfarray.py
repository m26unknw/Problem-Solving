#Product of an Array within list

def ProductOfArray(list):
    product = 1

    for N in list:
        product*=N
    return product

print(ProductOfArray([1,2,3]))