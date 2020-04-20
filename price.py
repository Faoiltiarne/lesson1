def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)
    price_with_dicounted = price - price * discount / 100
    return price_with_dicounted

p = discounted (382000, 13)

print (p)