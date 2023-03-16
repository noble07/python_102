# Set methods

set_countries = {'col', 'mex', 'bol'}
print(len(set_countries))

print('col' in set_countries)
print('pe' in set_countries)

# Create
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# Update - unions the current set with any iterable
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# Remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

# removing and item that doesn't exist
# set_countries.remove('arg') # Raise a key error
set_countries.discard('arg') # If not exist does nothing

# Remove all the elements
set_countries.clear()
print(set_countries)
print(len(set_countries))