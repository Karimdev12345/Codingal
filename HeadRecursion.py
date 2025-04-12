def Hrec(n, num):
    if n > num:
        return
    print(n)
    Hrec(n+1, num)

n= int(input("Enter n to print 1 to n: "))
Hrec(1,n)