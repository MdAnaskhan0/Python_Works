choise = int(input("Which currency you want to convart ? \n1. USD to Tk\n2.Tk to USD\n"))

if choise == 1:
    usd = int(input("Enter your amount in USD: "))
    total_tk = usd*103.42
    print(total_tk)

elif choise == 2: 
    tk = int(input("Enter your amount in Tk: "))
    total_usd = tk/103.42
    print(total_usd)

else:
    print("Choise 1 or 2 option...!")