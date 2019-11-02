# 02_sequences/0201_listcomp/020103_cartesian

## `listcomp` - Part 3

`listcomp` can be used to generate Cartesian products, a list
containing tuples built from all items from two or more lists.

For example:
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [
    (color, size) 
    for color in colors 
    for size in sizes
]
```

