"""
A code that helps banks to know if one client are a good client for a loan
"""

income = int(input("Welcome to Bank of Columbia!\nPlease insert the amount of your mothnly wage: \n"))
credit_score = int(input("Insert your credit score: \n"))
student = input("Are you student? 1.Yes 2.No \n")

if income >= 1000 and credit_score >= 600 and not student.lower == "Yes":
    print("Congratulations! You're elegible for a loan")
else:
    print("Sorry! You're not elegible")