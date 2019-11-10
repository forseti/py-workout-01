from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print(f"floats[-1]: {floats[-1]}")

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(f"floats2[-1]: {floats2[-1]}")

assert floats == floats2
