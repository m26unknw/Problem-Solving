#Largest In the List:

def LargestInList(list):

    large = list[0]

    for N in list:
        if N > large:
            large= N
    return large
print(LargestInList([1,2,3,3,4]))