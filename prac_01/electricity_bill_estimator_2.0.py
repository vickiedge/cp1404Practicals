#unsure how to link tariff to constants to call in estimated_bill - ??

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = (input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = [11/31] * daily_use * billing_days
print("Estimated bill: ${:.2f}".format(estimated_bill))