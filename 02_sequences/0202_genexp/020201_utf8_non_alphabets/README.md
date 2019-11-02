# 02_sequences/0202_genexps/020201_utf8_non_alphabets

## `genexp` - Part 1

`listcomp` is for building a list. To fill up other sequence
types, we must use `genexp`.

To initialize tuples, arrays, and other sequence types, we
could use `listcomp`, but `genexp` saves memory because
it yields item one by one using iterator protocol instead
of building a new list just to feed another constructor.

`genexp` use the same syntax as `listcomp`, but are enclosed
in parentheses `()` rather than brackets `[]`.

For example, to generate a tuple:
```python
non_alphabets = "!#%&+_"

codes = tuple(ord(char) for char in non_alphabets)
```

If the `genexp` are the single argument in a function call,
there is no need to duplicate the enclosing parentheses.

```python
import array

non_alphabets = "!#%&+_"

codes = array.array('I', (ord(char) for char in non_alphabets))
```

The `array` takes two arguments, so the `genexp` must be
enclosed with parentheses. The first argument `'I'` is the
storage type of unsigned int. 