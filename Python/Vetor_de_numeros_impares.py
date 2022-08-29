import random

def numRand():
    return random.randrange(1,100,2)
v =[]

for i in range(30):
    c = numRand()
    v.insert(i, c)
print(v)