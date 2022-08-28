import random

c = 1
v = random.sample(range(999), 10)
print(f"{v}\n")
for a in range(10):
    for b in range(9):
        if v[b] > v[b+1]:
            t = v[b]
            v[b] = v[b+1]
            v[b+1] = t
    print(f"Passo {c} - {v}")
    c = c+1
