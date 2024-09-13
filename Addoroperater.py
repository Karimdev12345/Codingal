#activity 1
a= 13
b= 4
c= 0

if a and b and c:
    
    print("All of the numbers must have boolean value as True")
else:
    print("Atleast one number has boolean value as false")

a= 9
b= -6
c= 3

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else: 
    print("No number is greater than 0")


#Activity 2
a= 9
b= 6
c= 12
print(a != b)
print(b != c)

a = int(input("enter a number:: "))

if a%2 != 0 :
    print(a, "is not an even number.")
else:
    print(a, "is an even number")