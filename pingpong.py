d = {}

def ping(s1,s2,r):
    global d
    if s1 == 21:
        return 1
    elif s2 == 21:
        return 0
    elif (s1 >= 11) & (s1-s2 >= 2):
        return 1
    elif (s2 >= 11) & (s2-s1 >= 2):
        return 0
    elif (s1,s2,r) in d.keys():
        return d[(s1,s2,r)]
    else:
        d[(s1,s2,r)]=r * ping(s1+1,s2,r) + (1-r)*ping(s1,s2+1,r)
        return d[(s1,s2,r)]


def optimize(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):
    ans=10
    r=.5
    a=ping(s1,s2,r)
    b=ping(s3,s4,r)
    c=ping(s5,s6,r)
    d=ping(s7,s8,r)
    e=ping(s9,s10,r)
    step=.1
    while(abs(ans-.5)>1e-3):
        print(abs(ans-.5)>1e-3)
        print(ans)
        if ans>.5:
            print("going down")
            r-=step
        else:
            print("going up")
            r+=step
        step*=.9
        a=ping(s1,s2,r)
        b=ping(s3,s4,r)
        c=ping(s5,s6,r)
        d=ping(s7,s8,r)
        e=ping(s9,s10,r)
        ans=a*b*c+d*((1-a)*b*c+a*(1-b)*c+a*b*(1-c))+e*((1-a)*(1-b)*c*d+(1-a)*b*(1-c)*d+(1-a)*b*c*(1-d)+a*(1-b)*(1-c)*d+a*(1-b)*c*(1-d)+a*b*(1-c)*(1-d))
    return r

print(optimize(0,9,0,9,0,0,0,0,0,0))
