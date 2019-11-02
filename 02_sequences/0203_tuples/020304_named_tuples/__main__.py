from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(f"City's Name: {tokyo}")
print(f"City's Population: {tokyo.population}")
print(f"City's Coordinates: {tokyo.coordinates}")

print()
print(f"City._fields: {City._fields}")

print()

LatLong = namedtuple("LatLong", 'lat long')
print(f"LatLong._fields", LatLong._fields)

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)

print(f"delhi._asdict(): {delhi._asdict()}")
for key, value in delhi._asdict().items():
    print(f"{key}:{value}")
