#valuations range from 0 to 10
#the 100 elements of blist correspond to increasing valuations
#binv finds a valuation corresponding to a bid using the current blist
#util finds the utility currently associated with
#a given bid and valuation
#The program updates blist until convergence


from scipy.optimize import minimize_scalar
blist=[]
for i in range(101):
    blist.append((0.9*i/10+4.5)/2)
tempblist=blist[:]

def binv(b):
    global blist
    dist = 10
    binv=10
    for i in range(101):
        if abs(blist[i]-b)<dist:
               dist=abs(blist[i]-b)
               binv=i/10
    #print('binv = ' + str(binv))
    return binv

def util(b,v):
    #print('util = ' + str((v-b)*(2*(binv(b)/10)-(binv(b)/10)**2)**9))
    return (v-b)*((binv(b)/10)**2)**9

dist=10
while(dist>1/1000000):
    for i in range(101):
        #print((tempblist[i],minimize_scalar(lambda b: -util(b,i/10), bounds = (0,10)).x))
        tempblist[i]=minimize_scalar(lambda b: -util(b,i/10), bounds = (0,10), method = 'bounded').x
        print((blist[i],tempblist[i]))
        #print((tempblist[i],minimize_scalar(lambda b: -util(b,i/10), bounds = (0,10)).x))
    dist=0
    for i in range(101):
        dist+=abs(tempblist[i]-blist[i])
    print(dist)
    #print(tempblist)
    #print(blist)
    blist=tempblist
    print('iteration')

#print(blist)
