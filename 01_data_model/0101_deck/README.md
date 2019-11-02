# 01_data_model/0101_deck

## Special Methods
Special methods are reserved for Python's `class`. 
They are inherited from `object`. 
Below are several special methods used in this section.

### `__init__(self, ...)`
This is the constructor method, similar to the ones found in other OO languages like Java.

### `__getitem__(self, item)`
The method `__getitem__` makes an object iterable using `for` loop.

For example:
```python
class FrenchDeck(object):
    def __getitem__(self, item):
        raise NotImplementedError("To be implemented")
    
deck = FrenchDeck()

for card in deck:
    print(card)
```

### `__len__(self)`
The built-in function `len(x)` will call the object's implementation of `__len__`.

```python
class FrenchDeck(object):
    def __len__(self):
        raise NotImplementedError("To be implemented")
    
deck = FrenchDeck()

len(deck)
```

### `__iter__(self)`
The loop `for i in x:` triggers `iter(x)` 
which in turn call `x.__iter__()` if implemented.