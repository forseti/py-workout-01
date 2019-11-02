# 02_sequences/0203_tuples/020301_tuples_as_records

Defining LAX Coordinates:
```python
lax_coords = (33,9425, -118.408056)
```

Assigning values from a tuple of Tokyo (city name, year, 
total population, population change, area) to five variables. 
This assignment is an example of *tuple unpacking*:
```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
```

Loop through `traveler_ids` and print `"%s/%s"` format 
of  each passport (and note that each `%s` represent the 
items in each tuple, the country and the passport number. This
is an example of *tuple unpacking*):
```python
traveler_ids = [
    ('USA', '311958955'),
    ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')
]

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)
```

Loop through `traveler_ids` and print the country (and we are 
not interested in the second item which is the passport number 
so we use `_` as a placeholder that represent an unused variable):
```python
traveler_ids = [
    ('USA', '311958955'),
    ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')
]

for country, _ in traveler_ids:
    print(country)
```