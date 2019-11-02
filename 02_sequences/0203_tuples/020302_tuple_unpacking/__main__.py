import os

lax_coords = (33.9425, -118.408056)
latitude, longitude = lax_coords

print(f"lax_coords: {lax_coords}")
print(f"latitude: {latitude}")
print(f"longitude: {longitude}")
print()

result = divmod(20, 8)
print(f"divmod(20, 8): {result}")

t = (20, 8)
result = divmod(*t)
print(f"if t: {t}, then divmod(*t): {result}")

quotient, remainder = result
print(f"quotient, remainder: {quotient}, {remainder}")

print()

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(f"filename of '/home/luciano/.ssh/idrsa.pub': {filename}")
print()

a, b, *rest = range(5)
print(f"a, b, rest: {a}, {b}, {rest}")

a, b, *rest = range(3)
print(f"a, b, rest: {a}, {b}, {rest}")

a, b, *rest = range(2)
print(f"a, b, rest: {a}, {b}, {rest}")

a, *body, c, d = range(5)
print(f"a, body, c, d: {a}, {body}, {c}, {d}")

*head, b, c, d = range(5)
print(f"a, body, c, d: {head}, {b}, {c}, {d}")

