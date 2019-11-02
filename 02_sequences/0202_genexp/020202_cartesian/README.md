# 02_sequences/0201_listcomps/020103_cartesian

## `genexp` - Part 2

`genexp` can be used to generate Cartesian products as a feed
to `for` loop, one item at a time, therefore no list is built
in memory.

If the Cartesian product has two lists of 1000 items
each, the `genexp` would save the need of building a list of
a million items just to feed the loop.

For example:
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (
    '%s %s' % (color, size)
    for color in colors
    for size in sizes
):
    print(tshirt)
```

The `genexp` yield items one by one and a list with all T-shirts
is never produced.
