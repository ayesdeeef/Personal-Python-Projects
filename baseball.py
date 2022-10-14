import random
out=50
first=0
second=0
third=0
home=50
walk=0
avg=0
outs=0
pts=0
bases=[0,0,0]
trls=100000
steal=0
stealout=0
for i in range(trls):
    while outs<3:
        #print("current inning: " + str(i))
        if bases==[1,0,0]:
            randsteal=random.randint(0,99)
            if randsteal<steal:
                #print("steal")
                bases=[0,1,0]
            elif randsteal<steal+stealout:
                #print("out while stealing")
                bases=[0,0,0]
                outs+=1
        rand=random.randint(0,99)
        if rand<out:
            #print("out")
            outs+=1
        elif rand<out+first:
            #print("single")
            pts+=bases[2]+bases[1]
            bases[2]=0
            bases[1]=bases[0]
            bases[0]=1
        elif rand<out+first+second:
            #print("double")
            pts+=bases[2]+bases[1]
            bases[2]=bases[0]
            bases[1]=1
            bases[0]=0
        elif rand<out+first+second+third:
            #print("triple")
            pts+=sum(bases)
            bases[2]=1
            bases[1]=0
            bases[0]=0
        elif rand<out+first+second+third+home:
            #print("homer")
            pts+=1+sum(bases)
            bases=[0]*3
        else:
            #print("walk")
            if 0 in bases:
                bases[bases.index(0)]=1
            else:
                pts+=1
        #print("current bases: " + str(bases))
        #print("current score: " + str(pts))
        #print("current outs: " + str(outs))
    avg+=pts
    outs=0
    pts=0
    bases=[0,0,0]
avg=avg/trls
print(avg)
