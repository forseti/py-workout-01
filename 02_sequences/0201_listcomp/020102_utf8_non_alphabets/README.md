# 02_sequences/0201_listcomp/020102_utf8_non_alphabets

## `listcomp` - Part 2

`listcomp` build lists from sequences or any other 
iterable type by filtering and transforming items.

For example:
```python
non_alphabets = "!#%&+_"

codes = [ord(char) for char in non_alphabets if ord(char) > 38]
```

`filter` and `map` can be composed to do the same, but
readability suffers.

For example:
```python
non_alphabets = "!#%&+_"

codes = list(filter(lambda c: c > 38, map(ord, non_alphabets)))
```