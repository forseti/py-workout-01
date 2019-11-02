# 02_sequences/0203_tuples/020302_tuple_unpacking

To get `latitude` and `longitude` of `lax_coords`:
```python
lax_coords = (33.9425, -118.408056)

latitude, longitude = lax_coords
```

To get a tuple of `(quotient, remainder)` from 
`divmod` function:
```python
result = divmod(20, 8)
```

A different way to get the `(quotient, remainder)` from
`divmod` function by using prefix `*`:
```python
t = (20, 8)

result = divmod(*t)
```

The `os.split.path(x)` function builds a tuple of
`(path, last_part)`, and we can use it to assign the filename 
which is `"idrsa.pub"` to variable `filename`:
```python
import os

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
```

We can use prefix `*` to grab excess items

The `rest` will retain empty array `[2, 3, 4]`, and `a` 
and `b` respectively will retain `0` and `1`
```python
a, b, *rest = range(5)
```

The `rest` will retain empty array `[2]`, and `a` 
and `b` respectively will retain `0` and `1`
```python
a, b, *rest = range(3)
```

The `rest` will retain empty array `[]`, and `a` 
and `b` respectively will retain `0` and `1`
```python
a, b, *rest = range(2)
```

The `body` will retain `[1, 2]`, and `a`, `c`, and `d` 
respectively will retain `0`, `3`, and `4`
```python
a, *body, c, d = range(5)
```

The `head` will retain `[0, 1]`, and `b`, `c`, and `d` 
respectively will retain `2`, `3`, and `4`:
```python
*head, b, c, d = range(5)
```