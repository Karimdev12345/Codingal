try:
    number=int(input("Ënter a number:"))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception:", ex)
