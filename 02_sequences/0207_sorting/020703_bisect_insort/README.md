# 02_sequences/0207_sorting/020703_bisect_insort

Sorting is expensive, so it is good to maintain a sorted
sequence. `bisect.insort(sequence, item)` can be used
to insert `item` into `sequence` but keep the `sequence`
in ascending order.

For example:
```python
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
```

Just like `bisect.bisect(sequence, item)`, it takes optional
`lo` and `hi` arguments to limit the search to a sub sequence.
There's also a `insort_left(sequence, item)` variation like 
`bisect_left(sequence, item)`.
