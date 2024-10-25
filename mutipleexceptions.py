try:
    num1,num2=eval(input("Enter numbers seperated by a comma : "))
    result= num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero us error !!")

except SyntaxError:
    print("Comma is missing. Emter number seperated by a comma like 1, or 2")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")