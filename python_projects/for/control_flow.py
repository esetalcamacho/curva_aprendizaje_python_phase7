"""
Write a code that decides if the user are over or equal 22 to admit in university
"""

age = int(input("Please insert your age: \n"))

"""
if age >= 22:
    message = "Congratulations! You're enrolled in the university"
else:
    message = "Sorry, we can accept people underage
"""
# Simplify your code this way

message = "elegible" if age >= 22 else "not elegible"
print(f"Your age is {age}, you are", message)
