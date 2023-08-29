"""Triangle:

* 
* * 
* * * 
* * 
* 

"""



def main():
    n = int(input("Enter a number: "))
    print("\n")
    traingle1(n)
    triangle2(n)
    
    
def traingle1(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n") 

def triangle2(n):
    for i in range(1, n+1):
        for j in range(1,n+1-i):
            print("*",end=" ")
        print("\n")    
    
main()