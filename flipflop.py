def palind(r):
    e= len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1

    return True

r=(1,2,33,2,10)
if(palind(r)):
    print("The tuple is Flip-Flop")
else:
    print("The tuple is not a Flip-Flop")