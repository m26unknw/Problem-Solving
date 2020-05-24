#Smallest No in list

def smallestNo(list):
    small = list [0]

    for s in list:
        if s < small:
            small = s
    return small

print(smallestNo([1,-2,4,-5]))