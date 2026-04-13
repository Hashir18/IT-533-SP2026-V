# Step 1: first name lowercase
first_name = "Hashir"

# Step 2: last name uppercase
last_name = "Saqib"

# Step 3: greet with first name uppercased, last name lowercased
print("Hello, " + first_name.upper() + " " + last_name.lower())

# Step 4: two newlines
print("\n")

# Step 5: full name variable
full_name = first_name + " " + last_name

# Step 6: slice last name from full_name and print (one line)
print(full_name[len(first_name) + 1:])

# Step 7: replace last name with college tag
full_name = full_name.replace(last_name, last_name + ", Walsh College Student")
print(full_name)

# Step 8: print quote
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')

# Step 9: two decimal numbers
num1 = 12.5
num2 = 4.2

# Step 10: four math operations stored as variables
addition_result       = num1 + num2
subtraction_result    = num1 - num2
multiplication_result = num1 * num2
division_result       = num1 / num2

# Step 11: print each result using a different technique
print(str(num1) + " plus " + str(num2) + " equals " + str(addition_result))           # concatenation
print("%s minus %s equals %s" % (num1, num2, subtraction_result))                      # % formatting
print("{} times {} equals {}".format(num1, num2, multiplication_result))               # .format()
print(f"{num1} divided by {num2} equals {division_result}")                            # f-string

# Step 12: square root of multiplication result rounded to 2 decimal places
sq_root = round(multiplication_result ** 0.5, 2)
print("The square root of " + str(multiplication_result) + " equals " + str(sq_root))

# Step 13: current month as string, day as numeric
month = "April"
day = 13

# Step 14: print date on new line tabbed twice using .format() (different from step 12)
print("\n\t\tToday is day {} of the month of {}.".format(day, month))