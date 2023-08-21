unit = float(input("Enter total unit: "))

if unit >100 and unit < 200:
    unit = unit - 100
    bil = unit * 5
    print(bil)

if unit > 200:
    unit = unit - 200
    bil = 500+(unit*10)
    print(bil)
else:
    print("No charge.")    

