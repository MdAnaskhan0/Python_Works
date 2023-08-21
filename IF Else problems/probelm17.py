'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''

time = int(input("Enter your service time: "))
salary = float(input("Enter your salary: "))

if time > 5: 
    total_salary = (salary*5)/100
    print("Bonus amount: ",total_salary)
else:
    print(salary)