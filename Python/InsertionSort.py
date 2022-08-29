import random

def numRand():
    return random.randrange(1,1000,2)

def insertionSort(array):
    for i in range(1, len(array)):
        c = array[i]
        j = i-1
        while (j >= 0) and (c < array[j]):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = c

v =[]

for i in range(30):
    c = numRand()
    v.insert(i, c)

print(f"Vetor inicial: \n{v}\n")
insertionSort(v)
print(f"Vetor final: \n{v}\n")