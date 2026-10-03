tickets_sold = 0
total_revenue = 0
free_tickets = 0 
while True:
  name = input("customer name (or q to quit): ")
  if name == "q" or name == "Q":
    break
  try:
    age = int(input("age: " ))
  except ValueError:
    print("Invalid age.")
    continue
  if age < 0 or age > 120:
    print("Invalid age.")
    continue
  day = input("Day (weekday/weekend): ").lower()
  if day != "weekend" and day != "weekday":
    print("Invalid day.")
    continue
  student = input("student (yes/no): ").lower()
  if student != "yes" and student!= "no":
    print("please answer yes or no ")
    continue
  if day == "weekday":
    base_price = 200.0
  else:
    base_price = 250.0
  if age < 6:
    discount = 1.0
    ticket_type = "free"
  elif age >= 65:
    discount = 0.50
    ticket_type = "senior"
  elif age > 6 and age <= 12:
    discount = 0.40
    ticket_type = "child"
  elif student == "yes" and age <= 25:
    discount = 0.30
    ticket_type = "student"
  else:
    discount = 0.0
    ticket_type = "standard"
  price = base_price * (1 - discount ) 
  tickets_sold = tickets_sold + 1 
  total_revenue = total_revenue + price
  if price == 0:
    free_tickets = free_tickets + 1
  print(f"{name}: {price:.2f} TRY ({ticket_type})")
if tickets_sold == 0:
  print("no tickets sold")
else:
  avg_price = total_revenue / tickets_sold
  print(f"Tickets sold: {tickets_sold} / Total revenue: {total_revenue:.2f} TRY / Average price: {avg_price:.2f} TRY / Free tickets: {free_tickets}") 
  
