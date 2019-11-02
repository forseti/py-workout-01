# 02_sequences/0204_slicing/020401_excluded_last_item

Sequences can be sliced using `s[a:b]` syntax.

Why slices (`s[a:b]`) and range (`range(x)`) exclude the last item:
- It works well with the zero based indexing used in Python, C, and
many other languages.
- It's easy to see the length of the slice when only one stop
position is given. For example, `range(3)` and `list[:3]`
produce three items.
- It's easy to compute the length of a slice or range when stop
and start. Simply subtract `stop - start`.
- It's easy to split a sequence in two parts at any index `x`.
Simply get `list[:x]` or `list[x:]`.

For example:
```python
l = [10, 20, 30, 40, 50, 60]

# Get items from index 0-1. Skip the rest.
idx_0_to_1 = l[:2] # items: [10, 20]

# Skip index 0-1. Then get all items from index 2 
start_at_idx_2 = l[2:] # items: [30, 40, 50, 60]

# Get items from index 0-2. Skip the rest.
idx_0_to_2 = l[:3] # items: [10, 20, 30]

# Skip index 0-2 then get all items from index 3
start_at_idx_3 = l[3:] # items: [40, 50, 60]

# Skip index 0-1, then get items from index 2-4
idx_2_to_4 = l[2:5] # items: [30, 40, 50]
```
