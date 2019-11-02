from .vector import Vector

v1 = Vector(2, 4)
print("v1: %r" % v1)

v2 = Vector(2, 1)
print("v2: %r" % v2)

v3 = v1 + v2
print("v3 = v1 + v2: %r" % v3)

print()

v = Vector(3, 4)
print("v: %r" % v)

print("abs(v): %r" % abs(v))

print("v * 3: %r" % (v * 3))

print("abs(v * 3): %r" % abs(v * 3))
print()
