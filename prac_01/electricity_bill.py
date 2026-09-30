print("Electricity bill estimator")
price_per_kWh=float(input("Enter cents per kWh:"))
daily_use_kWh=float(input("Enter daily use in kWh: "))
number_of_days=int(input("Enter number of billing days: "))
estimated_bill=price_per_kWh*daily_use_kWh*number_of_days/100
print(f"Estimated bill: {estimated_bill:.2f}")


print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_choice=input("Which tariff? 11 or 31: ")
daily_use_kWh=float(input("Enter daily use in kWh: "))
number_of_days=int(input("Enter number of billing days: "))
if tariff_choice=="11":
    estimated_bill = TARIFF_11 * daily_use_kWh * number_of_days
    print(f"Estimated bill: {estimated_bill:.2f}")
else:
    estimated_bill = TARIFF_31 * daily_use_kWh * number_of_days
    print(f"Estimated bill: {estimated_bill:.2f}")