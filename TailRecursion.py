def Trec(n, num):
    if n > num:
        return
    Trec(n+1, num)
    print(n)

n= int(input("Enter n to print 1 to n :"))

Trec(1,n)
