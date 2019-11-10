# 02_sequences/0208_list_alternatives

`list` is flexible and easy to use. But there are better options,
depending on specific requirements.


Below are some examples when `list` is not the answer:

| Requirement | What to use  | Why |
|---|---|---|
| Storing 10 million floating-point values | `array` | `array` does not hold full-fledged `float` object but only packet bytes representing their machine values, just like array in the C language. |
| Constantly adding and removing items from end of a list as a FIFO data structure | `deque` | `deque` (double-dended queue) works faster |
| Your code does a lot of containment checks (e.g. `item in my_collection`) | `set` | `set` is highly optimized for fast membership checking. But they are not sequences, so their content is unordered | 