import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

    haystack_copy = HAYSTACK.copy()
    print(f"haystack before insert: {haystack_copy}")

    for needle in reversed(NEEDLES):
        position = bisect.bisect(HAYSTACK, needle)
        haystack_copy.insert(position, needle)

    print(f"haystack after insert: {haystack_copy}")


print('DEMO of ', bisect.bisect.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect.bisect)

print()

print('DEMO of ', bisect.bisect_left.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect.bisect_left)

print()


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


my_scores = [33, 99, 77, 70, 89, 90, 100]
print(f"my_scores: {my_scores}")
my_grades = [grade(score) for score in my_scores]
print(f"my_grades: {my_grades}")
