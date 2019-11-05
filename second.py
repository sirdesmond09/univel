# month = ['jan' , 'feb', 'march', 'april', 'may', 'june']
# sales = [5, 4, 5, 3, 5, 3]
# price = [300, 300, 300, 200, 215, 300]

# num = 0
# for i in range(num, len(month)):
#     print (f'{month[i]} -- N{price[i]} -- {sales[i]} pieces')


# zipped = zip(month, sales, price)
# data = list(zipped)
# print (data[1::2]) 


products = {'fruit':['apple', 'pear', 'orange']}
p = (products['fruit'])
# print(type(p))
# jj = (products['fruit'])[0]
# print (jj)

new_fruit = ['breadfruit', 'banana', 'agege']
p.append('passion')
for fruit in new_fruit:
    p.append(fruit)
    # print (p) 

products['shoe'] = []
new_shoes = ['nikeair', 'jordans', 'skates', 'toms']
for shoe in new_shoes:
    products['shoe'].append(shoe)


products['electronics'] = []
new_electronics = ['tv', 'radio', 'fans']
for electronics in new_electronics:
    products['electronics'].append(electronics)

# print(products)


new_products = {}
for key in products:
    stock = products[key]
    new_products[key] = []

    for item in stock:
        price = len(item)*100
        template = {'name': item,
                    'price': price }
        new_products[key].append(template)

def purchase(cart):
    for key in new_products:
        print(key.upper())
    user1 = input("\nWhat would you like to buy? \n> ").lower()

    selected = new_products[user1]

    print('Here are the available items\n')
    for items in selected:
        print(items['name'].upper(), items['price'])

    user_product = input('Please select a product\n> ').lower()

    for product in selected:
        if product['name'] == user_product.lower():
            cart.append(product)

    return

print( f'Welcome! \nplease check our our list of products below\n ')
cart = []
purchase(cart)

choice = input('\nNeed more stuffs? Y/N \n>').lower()
select = ['y', 'n']
if choice == select[1]:
    break
else:
    purchase(cart)

bill = 0

for item in cart:
    bill += item['price']

    stuff = item['name']

print(f'\nYou bought {stuff}')
print(f'\nYour bill is N{bill}')


# def function(a, b, c, d):
#     num = a + b + c + d
    
#     return num

# result = function(2, 4, 6, 8)

# print(result)

# def formatdetails(_list):
    
#     name = f"{_list[0]} {_list[1]}"
#     age = f"{_list[2]}"
#     height = f"{_list[3]}"
#     detail = {'name' : name, 'age':age, 'height': height }

    

#     return detail


# go = ['attah', 'iyang', '20', '6Feet']

# print(formatdetails(go))
