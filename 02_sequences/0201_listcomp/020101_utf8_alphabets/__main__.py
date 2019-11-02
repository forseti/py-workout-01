alphabets = 'AXBYCZ'

codes = []

for char in alphabets:
    codes.append(ord(char))

print(f"codes for '{alphabets}' (built using 'for' loop): {codes}")

codes = [ord(char) for char in alphabets]

print(f"codes for '{alphabets}' (built using 'listcomps'): {codes}")
