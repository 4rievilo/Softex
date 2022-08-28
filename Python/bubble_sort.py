import random

v = random.sample(range(9999), 10)
print(f"{v}")
for a in range(10):
    for b in range(9):
        if v[b] > v[b+1]:
            t = v[b]
            v[b] = v[b+1]
            v[b+1] = t
for a in range(10):
    print(f"{a+1} - {v[a]}")
