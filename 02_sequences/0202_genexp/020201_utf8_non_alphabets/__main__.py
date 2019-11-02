import array

non_alphabets = "!#%&+_"

codes = tuple(ord(char) for char in non_alphabets)

print(f"codes for '{non_alphabets}' (built using 'genexps') - tuple: {codes}")

codes = array.array('I', (ord(char) for char in non_alphabets))

print(f"codes for '{non_alphabets}' (built using 'genexps') - array: {codes}")
