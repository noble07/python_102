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

prices = map(lambda item: item['price'], items)
print(list(prices))

# Adding taxes to the price
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
