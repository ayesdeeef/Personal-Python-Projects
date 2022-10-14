globaldict={}

def solve(n):
    global globaldict
    if (n == 0):
        return (0,None)
    elif (n==1):
        return (0,None)
    elif (n in globaldict.keys()):
        return globaldict.get(n)
    else:
        ls=0
        lp=None
        for i in range(n-1):
            if ((i+1)/n)*(n-(i+1)) + ((n-(i+1))/n)*solve(n-(i+1)-1)[0] > ls:
                ls = ((i+1)/n)*(n-(i+1)) + ((n-(i+1))/n)*solve(n-(i+1)-1)[0]
                lp = (i+1)
        globaldict[n]=(ls,lp)
        return (ls,lp)

for j in range(50):
    print(j,solve(j))
