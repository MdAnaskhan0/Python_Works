""" Triangle

* * * * 
  * * * 
    * * 
      * 
      
"""


def main():
    n = int(input("Enter a number: "))
    print("\n")
    triangle(n)
    
def triangle(n):
    for i in range(n,0,-1):
        print(" "* 2 *(n-i),end="")
        for j in range(i):
            print("*",end=" ")
        print("\n")
        
main()