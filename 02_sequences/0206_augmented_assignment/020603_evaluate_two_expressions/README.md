# 02_sequences/0206_augmented_assignment/020603_evaluate_two_expressions

Because tuple is immutable, the following assignment will 
not run within a Python script:
```python
t = [1, 2, [30, 40]]
t[2] += [50, 60]
```

The following error message will show up:
```console
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment
```

Things to remember:
- Putting mutable items in tuples is not a good idea.
- Augmented assignment is not an atomic operation
