# 02_sequences/0203_tuples/020305_tuples_as_immutable_list

Tuple support all list methods that do not involve 
adding/removing items, with one exception: tuple lacks
`__reversed__` method.

However, `reversed(x)` function can be used to reverse
a tuple.