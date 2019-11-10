# 02_sequences/0206_augmented_assignment
The augmented assignment operators `+=` and `*=` behave
differently depending on the first operand.

The special method that makes `+=` work is `__iadd__`. If it is
not implemented, Python falls back to calling `__add__`.

For example, in the following expressions:
```python
a = [1]
b = [2, 3]

a += b
```

if `a` implements `__iadd__`, the method will be called. In the
case of mutable sequences (e.g. `list`, `bytearray`, `array.array`),
`a` will be changed in place (with similar effect to `a.extend(b)`).

If `a` does not implement `__iadd__`, the expression `a += b` has
the same effect as `a = a + b`. The expression `a + b` is evaluated
first, producing new object, which is then assigned to `a`.

The same rule applies to `*=`, which is implemented via `__imul__`.
