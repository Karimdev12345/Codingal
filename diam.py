rowSize= int(input("enter the number of row: "))
if rowSize%2==0:
    halfDiamRow= int(rowSize/2)
else:
    halfDiamRow= int(rowSize/2)+1
    space= halfDiamRow-1 
    for i in range(1,halfDiamRow+1):
        for j in range(1, space+1):
            print(end= "")
            space= space-1
            num=1 