# 02_sequences/0201_listcomp/020101_utf8_alphabets

## `listcomp` - Part 1

Two common ways of building a list:
- Using `for` loop.
- Using `listcomp`.

Example of using `for` loop:
```python
alphabets = 'AXBYCZ'

codes = []

for char in alphabets:
    codes.append(ord(char))
```

Example of using `listcomp`:
```python
alphabets = 'AXBYCZ'

codes = [ord(char) for char in alphabets]
```

The `ord(x)` function above is to display unicode of 
a character. A character is a string with length of 1.

When to use `for` loop:
- Scanning a sequence to count or pick items.
- Computing aggregates.
- Any other processing tasks.

When to use `listcomp`:
- Building a new list.
- If it spans more than two lines, break it apart or 
rewrite using `for` loop.

Line breaks are ignored inside pairs of `[]`, `{}`, or `()`.
So we can build multiline lists, `listcomp`, `genexp`, 
dictionaries, and the like without using ` \ ` continuation
escape.
