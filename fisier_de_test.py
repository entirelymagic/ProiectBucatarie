n1 = [1, 2, 3]
n2 = [2, 3, 4]


n = []

for e in n1:
    n.append(str(e))

# acelasi lucru ca mai sus , folosind list comprehension
n = [str(e) for e in n1]

print(n)