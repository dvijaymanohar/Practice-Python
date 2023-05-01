discount = 30
total_price_of_the_product = 30
state_tax = 5
shipping_cost = 7.5

after_discount = ((total_price_of_the_product - ((discount / 100) * total_price_of_the_product)))

mrp = after_discount + ((after_discount / 100) * state_tax)
total_cost = mrp

if total_cost >= 50:
    print("Shipping is free. So total payable amount: ")
    print(total_cost)
elif total_cost < 50:
    print("Add more products to the basket to get shipping fee")
    total_cost += shipping_cost
    print("Total payable amount:")
    print(total_cost)
