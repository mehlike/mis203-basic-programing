item1_name = input("enter item1 name: ")
item1_quantity = int(input("enter item1 quantity: "))
item1_price =int(input("enter item1 price: "))
item2_name = input("enter item2 name: ")
item2_quantity =int(input("enter item2 quantity: "))
item2_price = int(input("enter item2 price:"))
delivery_fee = float(input("enter delivery fee: "))
tax_percentage = float(input("enter tax percentage: "))

item1_total = item1_quantity * item1_price 
item2_total = item2_quantity * item2_price

subtotal = item1_total + item2_total
tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount +  delivery_fee 

print(f"{item1_name}: {item1_quantity} * {item1_price:.2f} TRY = {item1_total:.2f} TRY")
print(f"{item1_name}: {item2_quantity} * {item2_price:.2f} TRY = {item2_total:.2f} TRY")
print(f"subtotal: {subtotal:.2f} TRY")
print(f"tax ({tax_percentage:.2f}%): {tax_amount:.2f} TRY ") 
print(f"delivery fee: {delivery_fee:.2f} TRY")
print(f"expected total: {final_total:.2f} TRY")

