# 02_sequences/0206_augmented_assignment/020602_tuple
The following example is when augmented assignment performed
on (immutable) tuple:
```python
t = (1, 2, 3)
id1 = id(t)

t *= 2
id2 = id(t)

assert id1 != id2 # A new list is created.
```