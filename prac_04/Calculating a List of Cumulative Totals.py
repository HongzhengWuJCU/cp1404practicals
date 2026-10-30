"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    monthly = int(input("How many months? "))
    incomes= add_income(monthly, incomes)
    print("\nIncome Report\n-------------")
    report_income(monthly,incomes)


def add_income(months, money):
    """Add the income into incomes"""
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        money.append(income)
    return money


def report_income(months, money):
    """shows the income's report"""
    total = 0
    max_income_width=max(len(str(i)) for i in money)
    for month in range(1, months + 1):
        income = money[month - 1]
        total += income
        print(f"Month  {month} - Income: $ {income:>{max_income_width}.2f} Total: $ {total:.2f}")

main()