colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (
    '%s %s' % (color, size)
    for color in colors
    for size in sizes
):
    print(tshirt)