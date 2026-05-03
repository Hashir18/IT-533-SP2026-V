
# EXAMPLE 1 - ASSIGNMENT STATEMENT: Basic Variable Assignment
# Scenario: A coffee shop app stores menu items and prices
# so they can be referenced and displayed throughout the program.

featured_drink = "Caramel Oat Latte"
drink_price = 6.75
drink_size = "Large"
drink_calories = 320
is_available = True

print("Today's Featured Drink:", featured_drink)
print("Size:", drink_size)
print("Calories:", drink_calories)
print("Price: $", drink_price)
print("Available:", is_available)


# EXAMPLE 2 - ASSIGNMENT STATEMENT: Augmented Assignment (+=)
# Scenario: A gym membership tracker updates a running total
# as new members sign up and calculates monthly revenue.

total_members = 120
monthly_fee = 49.99

total_members += 1
total_members += 1
total_members += 1
total_members += 1
total_members += 1

monthly_revenue = total_members * monthly_fee

print("Total gym members:", total_members)
print("Monthly revenue: $", monthly_revenue)


# EXAMPLE 3 - ASSIGNMENT STATEMENT: Multiple/Tuple Assignment
# Scenario: A weather app unpacks GPS coordinates and
# displays location info for a given city.

city = "Dubai"
latitude, longitude = 25.2048, 55.2708
temperature, humidity, wind_speed = 38.5, 60, 14

print("City:", city)
print("Latitude:", latitude, "| Longitude:", longitude)
print("Temperature (C):", temperature)
print("Humidity (%):", humidity)
print("Wind Speed (km/h):", wind_speed)


# EXAMPLE 4 - EXPRESSION STATEMENT: Calling a List Method
# Scenario: A teacher builds a gradebook by appending student
# scores as they are submitted, then calculates the average.


gradebook = [88, 92, 75, 84, 90]

gradebook.append(95)
gradebook.append(67)
gradebook.append(78)
gradebook.append(88)

total_score = sum(gradebook)
average_score = total_score / len(gradebook)

print("All scores:", gradebook)
print("Number of students:", len(gradebook))
print("Class average:", average_score)


# EXAMPLE 5 - PRINT STATEMENT: Formatted String Output
# Scenario: An e-commerce order confirmation page displays
# the customer's full order summary using f-strings.

customer_name = "Alex Rivera"
order_number = 48291
item_one = "Wireless Headphones"
item_two = "Phone Case"
item_three = "USB-C Cable"
subtotal = 119.97
tax = subtotal * 0.08
order_total = subtotal + tax

print(f"===== Order Confirmation =====")
print(f"Customer: {customer_name}")
print(f"Order #: {order_number}")
print(f"Items Ordered:")
print(f"  - {item_one}")
print(f"  - {item_two}")
print(f"  - {item_three}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total Charged: ${order_total:.2f}")
print(f"Thank you for your purchase, {customer_name}!")