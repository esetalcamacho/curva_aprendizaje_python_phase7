"""This code calculates the return on an investment with monthly additions without commission"""
# Aqui definimos los datos que necesitara la funcion

def final_capital(inv_initial, inv_time, inv_monthly, inv_annual_rate, inv_monthly_rate):
    total = inv_initial
    annual_investment = [] # List where will storage each value and comissions.
    if inv_monthly == 1:
        inv_monthly_value = int(input("Please insert the amount: \n$"))
        for year in range(1, inv_time+1):
            # Use a for to calculate each add of money in a month
            for month in range(12):
                total *= 1 + inv_monthly_rate
                total += inv_monthly_value
            # Rest the anual comision
            total -= total * inv_annual_fee
            total_comissions = (total * inv_annual_fee)
            annual_investment.append((total, total_comissions))
    else:
        for year in range(1, inv_time + 1):
            total = inv_initial*(1+inv_annual_rate)**year
            total -= total * inv_annual_fee
            total_comissions = (total * inv_annual_fee)*inv_time
            annual_investment.append((total, total_comissions))
    return annual_investment

investment_name = input("Please insert the name of the investment: ")
inv_initial = int(input("Please insert the initial value: $"))
inv_monthly = int(input("Do you want to add monthly values to initial investment?\n Select 1 or 2\n 1.Yes\n 2.No\n "))
# Time
inv_time = int(input("How many years you want to invest? "))
inv_total_months = inv_time * 12
# Rates
inv_annual_rate = 0.0981
inv_monthly_rate = inv_annual_rate / 12
inv_annual_fee = 0.0015

# In this dictionary we will storage the name and values for each investment
investment_data = {}

# In the list storage all values for each year
annual_investment = final_capital(inv_initial, inv_time, inv_monthly, inv_annual_rate, inv_monthly_rate)

# Storage values in dictionary
investment_data[investment_name] = annual_investment

for year, (total_value, total_commission) in enumerate(annual_investment, start=1):
    print(f"Inversión: {investment_name}, Año {year}: Valor total: ${total_value:.2f}, Comisiones totales: ${total_commission:.2f}")
