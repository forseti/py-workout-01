non_alphabets = "!#%&+_"

codes = [ord(char) for char in non_alphabets if ord(char) > 38]

print(f"codes for '{non_alphabets}' (built using 'listcomps'): {codes}")

codes = list(filter(lambda c: c > 38, map(ord, non_alphabets)))

print(f"codes for '{non_alphabets}' (built using 'filter' and 'map'): {codes}")
