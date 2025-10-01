d1 = {}  # create new empty dict

# initialize dict with key/value pairs 
# (keys can be any string, number or tuple of strings or numbers)
airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',  
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = dict()  # new empty dict -- {} preferred

# initialize dict with named parameters; keys must be valid identifier names
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]
state_capitols = dict(pairs)  # initialize dict with an iterable of pairs

print(f"{d3['red'] = }") # print value for given key

print(f"{airports['LAX'] = }")

airports['SLC'] = 'Salt Lake City'  # assign to new key
airports['LAX'] = 'Los Angeles (main)'  # overwrite existing key
print(f"{airports['SLC'] = }")
print()

print(f"{airports = }")
