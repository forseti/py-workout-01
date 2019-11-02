# 01_data_model/0102_vector

## Special Methods

Below are several special methods used in this section.

### `__repr__(self)`
This is like `toString()` in Java.
There is another similar special method `__str__(self)`
which is called by the `str(x)` constructor before implicitly
used by `print` function.

Always favor `__repr__` over `__str__` because the former 
will always be triggered by Python when no 
custom `__str__` is available.

### `__abs__(self)`
The built-in `abs(x)` method will trigger `__abs__` of `x` if implemented.

For example:
```python
class Vector(object):
    def __abs__(self):
        raise NotImplementedError("To be implemented")

v = Vector(3, 4)

abs(v) # will give result from 'v.__abs__()'
```

### `__add__(self, item)`
This is like addition operator overloading in C++

For example:
```python
class Vector(object):
    def __add__(self, other):
        raise NotImplementedError("To be implemented")
        
v1 = Vector(2, 4)
v2 = Vector(2, 1)

v3 = v1 + v2 # will trigger v1.__abs__(v2)
```

### `__mul__(self, item)`
This is like multiplication operator overloading in C++

```python
class Vector(object):
    def __mul__(self, scalar):
        raise NotImplementedError("To be implemented")
        
v = Vector(3, 4)

v * 3 # will trigger v.__mul__(3)
```

### `__bool__(self)`

To determine if a value is `True` or `False`, Python uses
`bool(x)`

By default, instances of user-defined classes are `True`,
unless either `__bool__` or `__len__` is implemented.

It will be triggered in the following order:
1. `bool(x)` calls `x.__bool__()` and uses the result.
2. if `__bool__` is not implemented, `x.__len__()` will be invoked, and if it
returns zero, `bool(x)` will return `False`.