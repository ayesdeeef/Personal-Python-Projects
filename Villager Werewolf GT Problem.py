#Memoization for smaller subproblems
globaldict={}

#n is the number of villagers initially
def solve(n):
    #Editing the dictionary within a method
    global globaldict
    #Base case with 0 villagers
    if (n == 0):
        #0 people survive on average, it doesn't matter how many take poison
        return (0,None)
    #Base case with 1 villager
    elif (n==1):
        #0 people survive on average, it doesn't matter how many take poison
        return (0,None)
    #Case where we have already solved this subproblem
    elif (n in globaldict.keys()):
        #The return value is the value associated with the argument
        return globaldict.get(n)
    #Case of new problem
    else:
        #ls is the number of people we expect to survive
        ls=0
        #lp is the number of people who should take poison
        lp=None
        #We want to test if anywhere from 1 to n-1 villagers inclusive should take poison
        for i in range(n-1):
            #Check if the number of villagers that would survive if i+1 villagers took poison is greater than the current amount that would survive
            if ((i+1)/n)*(n-(i+1)) + ((n-(i+1))/n)*solve(n-(i+1)-1)[0] > ls:
                #If it is, update the expected number that survive
                ls = ((i+1)/n)*(n-(i+1)) + ((n-(i+1))/n)*solve(n-(i+1)-1)[0]
                #Also if it is, update the number that should take poison
                lp = (i+1)
        #After solving, put our solution in the dictionary for memoization
        globaldict[n]=(ls,lp)
        #Return out solution
        return (ls,lp)

#Solve the problem for when the number of villagers ranges from 0 to 49
for j in range(50):
    #Print the number of villagers followed by a tuple containing the expected number to survive and the amount that should take poison
    print(j,solve(j))
