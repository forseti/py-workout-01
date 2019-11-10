# 02_sequences/0207_sorting/020702_bisect

Once sequences are sorted, they can be very efficiently searched.

The standard binary search algorithm is provided in
`bisect` module of the Python standard library.

- `bisect(haystack, needle)` does a binary search for `needle`
in `haystack`, which must be a sorted sequence, to locate 
the position where needle can be inserted while maintaining
haystack in ascending order.
- All items appearing up to that position are less than or equal
to `needle`.
- We can use the result of `bisect(haystack, needle)` as the index
argument to `haystack.insert(index, needle)`. `insort(haystack, needle)`
does both steps but faster.

Example of `bisect(haystack, needle)`:
```python
import bisect

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

for needle in reversed(needles):
    # Get the position where we can insert each needle.
    position = bisect.bisect(haystack, needle)
    
    # Insert the needle at the position that keeps the list sorted.
    haystack.insert(position, needle)
```

- `bisect(haystack, needle)` is an alias to 
`bisect_right(haystack, needle)`. The counterpart to this
function is `bisect_left(haystack, needle)`.
- `bisect_right(haystack, needle)` returns the insertion point after the existing item.
- `bisect_left(haystack, needle)` returns the insertion point of the existing item, so
insertion would occur before it.
- With simple type like `int`, there is no difference between both functions. Only when
the sequence contains objects that are distinct and yet compare equal, it may be relevant.
For example, `1` and `1.0` are distinct but `1 == 1.0` is `True` 

Another example is for table lookups by numeric values:
```python
import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    # Get the insertion index for the score.
    i = bisect.bisect(breakpoints, score)
    
    # Use the index to return the grade.
    return grades[i]

my_scores = [33, 99, 77, 70, 89, 90, 100]

# Build up the grades.
my_grades = [grade(score) for score in my_scores]
```