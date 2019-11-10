# 02_sequences/0206_augmented_assignment/020601_list
The following example is when augmented assignment performed
on (mutable) list:
```python
l = [1, 2, 3]
id1 = id(l)

l *= 2
id2 = id(l)

assert id1 == id2 # No new list is created
```