# 02_sequences/0203_tuples/020303_nested_tuple_unpacking

An example of nested tuple unpacking that we use to get
latitude and longitude of the metro areas that has longitude
less than 0:
```python
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

results = []

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        results.append(f"{name}, {latitude}, {longitude}")
```