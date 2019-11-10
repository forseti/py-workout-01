# 02_sequences/0208_list_alternatives/020801_array

If the list will only contain a number, `array.array` is more efficient
than a `list`. It supports all mutable sequences operations including
`.pop`, `.insert`, and `.extend`, and additional methods for fast
loading and saving such as `.frombytes` and `.tofile`.

A Python array is as lean as a C array. When creating an `array`, we
provide a `typecode`, a letter to determine the underlying C type used
to store each item in the array. For example `b` is the `typecode` for
`signed char`. If `array('b')` is created, then each item will be
stored in a single byte and interpreted as an integer from -128 to 127.

For large sequences of numbers, this saves a lot of memory. Python
will not let us to put any number that does not match the type for the
`array`.

An example of `array`:
```python
from array import array
from random import random

# Generate an array of double precision floats (typecode 'd') from any iterable object, using generator expression
floats = array('d', (random() for i in range(10**7)))

# Save the array to a binary file
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# Read the array from the binary file.
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

# Assert the last number
assert floats[-1] == floats2[-1]

# Assert the content of the arrays.
assert floats == floats2
```