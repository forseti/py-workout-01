# 02_sequences/0205_plus_and_asterisk/020501_copies_of_same_sequence

To concat multiple copies of the same sequence, multiply
it by an integer:
```python
l = [1, 2, 3] # [1, 2, 3]

l_times_5 = l * 5 # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

abcd_times_5 = 5 * 'abcd' # 'abcdabcdabcdabcdabcd'

my_list = [[]] * 3 # [[], [], []]

others = [4, 5] # [4, 5]

l_plus_others = l + others # [1, 2, 3, 4, 5]
```