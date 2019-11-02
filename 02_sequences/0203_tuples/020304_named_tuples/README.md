# 02_sequences/0203_tuples/020304_named_tuples

We can use `collections.namedtuple` to add field names 
to our tuple:
```python
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

city_name = tokyo.name
city_population = tokyo.population
city_coordinates = tokyo.coordinates
```

Any instances of a class that we build with `namedtuple`
take exactly the same amount of memory as tuples, because
the field names are stored in the class

- `namedtuple` takes two parameters:
    * a class name (`"City"`).
    * a list of field names which can be an iterable of strings or 
a single space-delimited string (`"name country population coordinates"`).

- Data must be passed as positional arguments
(`City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))`).

- Fields can be accessed by name or position (`tokyo.population`).

`namedtuple` has a number of useful attributes. Below are the
example of the most useful (`_fields`, `_asdict()`, 
`_make(iterable)`):
```python
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
city_fields = City._fields

LatLong = namedtuple("LatLong", 'lat long')
lat_long_fields = LatLong._fields

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)

delhi_as_dict = delhi._asdict()

result = []
for key, value in delhi._asdict().items():
    result.append(f"{key}:{value}")
```

- `_fields` is a tuple of the field names of the class.
- `_make(iterable)` can instantiate a named tuple from an iterable.
For the example above `City(*delhi_data)` would do the same.
- `_asdict()` returns a `collections.OrderedDict` built from
the `namedtuple`'s instance 


