# 02_sequences/0204_slicing/020404_assigning_to_slices

Slices can be used to change mutable sequences, without rebuilding
them from scratch.

```python
# Create a list of range(10)
l = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replace items from index 2 to 4, which is [2, 3, 4] with [20, 30]
l[2:5] = [20, 30] # [0, 1, 20, 30, 5, 6, 7 ,8, 9]

# Delete items from index 5 to 6, which is [6, 7]
del l[5:7] # [0, 1, 20, 30, 5, 8, 9]

# For every two steps, replace all items from index 3 with [11, 22]
l[3::2] = [11, 22] # [0, 1, 20, 11, 5, 22, 9]

# Replace all items from index 2 to 4, which is [20, 11, 5]  with [100]
l[2:5] = [100] # [0, 1, 100, 22, 9]
```
