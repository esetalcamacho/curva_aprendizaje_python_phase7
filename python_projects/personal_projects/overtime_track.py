"""
This code that helps you to know the value of a extra hour
"""
"""
income_worker = int(input("Insert your monthly wage\n" "$ "))

daily_hours = 42.5
monthly_hours = daily_hours/6*30
hour_value = int(income_worker / monthly_hours)

ot = input("You worked extra hours this month? 1.Yes 2. No \n")

if (ot.lower() == "yes"):
    hour_qty = int(input("Insert the quantity of extra hours \n"))

    hour_value_ot = int((hour_value*0.25)+hour_value)
    my_ot = int(hour_qty*hour_value_ot)
    income_ot = int(income_worker+my_ot)

    ot_weekend = input("You worked extra hourse on weeknd this month? 1.Yes 2. No \n")

    if (ot_weekend.lower == "no"):
        print(f"You worked this week {hour_qty} and you earned for each extra hour ${my_ot}")
        print(f"Your wage this month with OT is ${income_ot}")
        print(f"Each extra hour worked with your actual wage has a value of ${hour_value_ot}")
    else:
        hour_qty_weekend = int(input("Insert the quantity of extra hours \n"))
        hour_value_weekend_ot = int((hour_value * 2)+hour_value)
        my_ot_weekend = int(hour_qty*hour_value_weekend_ot)
        income_ot = int(income_worker+my_ot_weekend+my_ot)
        print(f"You worked this week {hour_qty} hours and the weeknd {hour_qty_weekend} you earned for each extra hour ${my_ot} and the weeknd ${my_ot_weekend}")
        print(f"Your wage this month with OT is ${income_ot}")
        print(f"Each extra hour worked with your actual wage has a value of ${hour_value_ot} and weekends ${hour_value_weekend_ot}")
else:
    print(f"Each hour worked has a value of ${hour_value} and your monthly income is ${income_worker}")

"""

def calculate_hour_value(income_worker):
    daily_hours = 42.5
    monthly_hours = daily_hours / 6 * 30
    hour_value = int(income_worker / monthly_hours)
    return hour_value

def calculate_extra_hours(income_worker, hour_value):
    ot = input("Did you work extra hours this month? (Yes/No)\n")
    if ot.lower() == "yes":
        hour_qty = int(input("Insert the quantity of extra hours\n"))
        hour_value_ot = int((hour_value * 0.25) + hour_value)
        my_ot = int(hour_qty * hour_value_ot)
        income_ot = int(income_worker + my_ot)
        return hour_qty, hour_value_ot, my_ot, income_ot
    else:
        return 0, 0, 0, 0

def calculate_extra_hours_weekend(income_worker, hour_value, my_ot):
    ot_weekend = input("Did you work extra hours on weekends this month? (Yes/No)\n")
    if ot_weekend.lower() == "yes":
        hour_qty_weekend = int(input("Insert the quantity of extra hours on weekends\n"))
        hour_value_weekend_ot = int((hour_value * 2) + hour_value)
        my_ot_weekend = int(hour_qty_weekend * hour_value_weekend_ot)
        income_ot = int(income_worker + my_ot_weekend + my_ot)
        return hour_qty_weekend, hour_value_weekend_ot, my_ot_weekend, income_ot
    else:
        return 0, 0, 0, 0

def main():
    income_worker = int(input("Insert your monthly wage ($)\n"))

    hour_value = calculate_hour_value(income_worker)

    hour_qty, hour_value_ot, my_ot, income_ot = calculate_extra_hours(income_worker, hour_value)

    if hour_qty > 0:
        hour_qty_weekend, hour_value_weekend_ot, my_ot_weekend, income_ot = calculate_extra_hours_weekend(income_worker, hour_value, my_ot)

        if hour_qty_weekend > 0:
            print(f"You worked {hour_qty} hours during weekdays and {hour_qty_weekend} hours during weekends. You earned ${my_ot} for each extra hour during weekdays and ${my_ot_weekend} for each extra hour during weekends.")
            print(f"Your total wage this month with overtime is ${income_ot}.")
            print(f"Each extra hour worked during weekdays has a value of ${hour_value_ot} and during weekends has a value of ${hour_value_weekend_ot}.")
        else:
            print(f"You worked {hour_qty} hours this month and you earned ${my_ot} for each extra hour.")
            print(f"Your total wage this month with overtime is ${income_ot}.")
            print(f"Each extra hour worked has a value of ${hour_value_ot}.")
    else:
        print(f"Each hour worked has a value of ${hour_value} and your monthly income is ${income_worker}.")

if __name__ == "__main__":
    main()
