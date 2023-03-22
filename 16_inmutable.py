items = [
    {
      'product': 'camisa',
      'price': 100
    },
    {
      'products': 'pantalones',
      'price': 300
    },
    {
      'products': 'pantalones 2',
      'price': 200
    },
]

# Adding taxes to the price
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)