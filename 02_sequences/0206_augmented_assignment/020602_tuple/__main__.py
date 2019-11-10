t = (1, 2, 3)
id1 = id(t)
print(f"id1: {id1}")

t *= 2
id2 = id(t)
print(f"id2: {id2}")

assert id1 != id2

print(f"id1 != id2: {id1 != id2}")
