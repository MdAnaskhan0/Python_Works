#Take values of length and breadth of a rectangle from user and check if it is square or not.
lenth = int(input("Enter length: "))
bre = int(input("Enter breadth: "))

if lenth == bre: 
    print("Length:",lenth,"Breadth: ",bre,"\nThis is not a rectangle.")
else:
    print("Length:",lenth,"Breadth: ",bre,"\nThis is a rectangle.")