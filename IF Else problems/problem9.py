price = int(input("Enter total prise of bike: "))

if price <= 50000:
    tax = (price*5)/100
    print("Tax Paid",tax)
elif price > 50000 and price <= 100000:
    tax = (price*10)/100
    print("Tax Paid",tax)
elif price > 100000:
    tax = (price*15)/100
    print("Tax Paid",tax)
