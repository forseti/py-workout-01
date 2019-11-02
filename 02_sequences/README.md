# 02_sequences
## Built-in Sequences
The standard library has a rich selection of sequence 
types implemented in C:

| Name | Description | Types
|---|---|:---:|
| *Container Sequences* | Hold references to the objects they contain, which can be any type. | `list`, `tuple`, and `collections.deque` can store  items of different types |
| *Flat Sequences* | Store the value of each item within its own memory space (and not as distinct objects) | `str`, `bytes`, `bytearray`, `memoryview` and `array.array` hold items of one type |


Sequences can also be grouped by mutability.

| Name | Types |
|---|:---:|
| *Mutable Sequences* | `list`, `bytearray`, `array.array`, `collections.deque`, and `memoryview` |
| *Immutable Sequences* | `tuple`, `str`, and `bytes` |


A quick way to build a sequence is using:
- A list comprehension (if the target is a list)
- A generator expression (for all other kinds of sequences).

Python programmers refer to list comprehensions as `listcomp`
and generator expressions as `genexp`.