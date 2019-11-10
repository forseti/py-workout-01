fruits = ['grape', 'raspberry', 'apple', 'banana']
fruits_copy = fruits.copy()

print(f"fruits: {fruits}")

sorted_fruits = sorted(fruits)
assert fruits == fruits_copy
print(f"sorted(fruits): {sorted_fruits}")

sorted_fruits = sorted(fruits, reverse=True)
assert fruits == fruits_copy
print(f"sorted(fruits, reverse=True): {sorted_fruits}")

sorted_fruits = sorted(fruits, key=len)
assert fruits == fruits_copy
print(f"sorted(fruits, key=len): {sorted_fruits}")

sorted_fruits = sorted(fruits, key=len, reverse=True)
assert fruits == fruits_copy
print(f"sorted(fruits, key=len, reverse=True): {sorted_fruits}")

fruits.sort()
assert fruits != fruits_copy
print(f"fruits after fruits.sort(): {fruits}")
