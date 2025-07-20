a = int(input("Enter a first number: "))
b = int(input("Enter an second number: "))
c= int(input("enter a third number:"))
def largest_number(a,b,c):
    if(a>b  and a>c):
        return(" first number is largest number",a)
    elif(b>a and b>c):
        return("second number is largest number",b)
    else:
        return("third is largest number",c)
    
print(largest_number(a,b,c))
