
cents_per_kWh = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = cents_per_kWh / 100 * daily_use * billing_days
print("Estimated bill: ${:.2f}".format(estimated_bill))