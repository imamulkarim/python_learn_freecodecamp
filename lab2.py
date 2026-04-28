def apply_discount(price, discount):
    if not isinstance(price, float) and not isinstance(price, int):
        return 'The price should be a number'
    if not isinstance(discount, int) and not isinstance(discount, float):
        return 'The discount should be a number'
    if (price <= 0):
        return 'The price should be greater than 0'
    if (discount < 0 or discount > 100):
        return 'The discount should be between 0 and 100'

    discount_amount = round((price * discount)/100,2)

    return price - discount_amount


print(apply_discount(74.5, 20.0));