# 02_sequences/0207_sorting/020701_list_sorting

There are two ways of sorting a list:
- `list.sort(self)` method that sorts a list in place, without 
making a copy. It returns `None`.
- `sorted(iterable)` built-in function that creates a new 
sorted list.

Both `list.sort(self)` and `sorted(iterable)` take two optional,
keyword-only arguments:
- `reverse`
    - If `True`, the items are returned in descending order.
    - The default is `False`.

- `key`
    - A one-argument function that will be applied to each item
    to produce its sorting key.
    - For examples:
        - `key=str.lower` can be used to perform 
        case-insensitive sort.
        - `key=len` can be used to sort strings by character
        length.
    - It can be used with built-in functions like 
    `min(iterable)` and `max(iterable)`, and with functions from
    the standard library like 
    `itertools.groupby(iterable, keyfunc)`
    and `heapnq.nlargest(n, iterable, key)`
 
```python
fruits = ['grape', 'raspberry', 'apple', 'banana']
fruits_copy = fruits.copy()

# Sorted alphabetically.
sorted_fruits = sorted(fruits) # ['grape', 'raspberry', 'apple', 'banana']
assert fruits == fruits_copy # No changes to original.

# Sorted alphabetically (reversed).
sorted_fruits = sorted(fruits, reverse=True) # ['apple', 'banana', 'grape', 'raspberry']
assert fruits == fruits_copy # No changes to original.

# Sorted by length. 'grape' is before 'apple' because both has same length thus no swap is required.
sorted_fruits = sorted(fruits, key=len) # ['grape', 'apple', 'banana', 'raspberry']
assert fruits == fruits_copy # No changes to original.

# Sorted by length (reversed).
sorted_fruits = sorted(fruits, key=len, reverse=True) # ['raspberry', 'banana', 'grape', 'apple']
assert fruits == fruits_copy # No changes to original

# Sorted using 'sort(self)' method.
fruits.sort()
assert fruits != fruits_copy # Original is sorted as ['apple', 'banana', 'grape', 'raspberry']
```