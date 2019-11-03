# 02_sequences/0204_slicing/020403_multi_dim_slicing_and_ellipsis

The `[]` operator can also take multiple indexes or slices
separated by commas. This is used, for instance, in the external
*NumPy* package, where a two dimensional `numpy.ndarray`
can be fetched using syntax `a[i, j]` and a two dimensional slice
can be obtained with an expression like 
`a[m:n, k:l]`.

The `__getitem__` and `__setitem__` special methods that handle
the `[]` operator simply receives the indices in `a[i, j]`
as a tuple. In other words, to evaluate `a[i, j]`, Python will
call `a.__getitem__((i, j))`

The built-in sequence types in Python is one-dimensional, so 
they support only one index or slice, not a tuple of them.

The ellipsis written with three full stops `...` is recognized
as a token by Python parser. It is an alias to `Ellipsis` object,
the single instance of `ellipsis` class. As such, it can be
passed as an argument to functions and as a part of a slice
specification as in `f(a, ..., z)` or `a[i:...]`.

For example, if `x` is a four-dimensional array, `x[i, ...]`
is a shortcut for `x[i, :, :, :]`.

(**Note**: The horizontal ellipsis *…* (Unicode U+2026) is not
recognized as a token.)