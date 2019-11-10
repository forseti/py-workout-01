l = [1, 2, 3]
id1 = id(l)
print(f"id1: {id1}")

l *= 2
id2 = id(l)
print(f"id2: {id2}")

assert id1 == id2

print(f"id1 == id2: {id1 == id2}")
