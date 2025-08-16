price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

def calculate_discount (price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    return price

final_price = calculate_discount(price, discount_percent)
print("Final price after discount is:", final_price)