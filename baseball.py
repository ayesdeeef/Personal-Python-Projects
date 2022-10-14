#I will use the random module to generate random numbers from 0 to 99 to create a percent likelihood of different discrete events
import random
#The likelihood of an out is 50% in this example
out=50
#The likelihood of a single is 0% in this example
first=0
#The likelihood of a double is 0% in this example
second=0
#The likelihood of a triple is 0% in this example
third=0
#The likelihood of a home run is 50% in this example
home=50
#The likelihood of a walk is 0% in this example
walk=0
#The average number of points per inning accross the trial is initialized to 0
avg=0
#The number of outs is initialized to zero
outs=0
#The points scored in this inning is initializedto zero
pts=0
#The bases are initialized to empty
bases=[0,0,0]
#In this example, we will average accross 100,000 trials
trls=100000
#In this example, the likelihood that a lone runner on first successfully steals second before any thrown pitch is 0%
steal=0
#In this example, the likelihood that a lone runner on first gets out attempting to steal second before any thrown pitch is 0%
stealout=0
#An inning occurs for each trial
for i in range(trls):
    #Pitches are thrown until there are three outs
    while outs<3:
        #If there is a lone runner on first, he may steal
        if bases==[1,0,0]:
            #Generate a random integer to decide the outcome of the steal opportunity
            randsteal=random.randint(0,99)
            #The steal variable is a percentage of events where the base is stolen
            if randsteal<steal:
                #If this happens, the runner moves to second before the pitch
                bases=[0,1,0]
            #The stealout variable is a percentage of events where the runner gets out attempting to steal
            elif randsteal<steal+stealout:
                #If this happens, bases are emptied
                bases=[0,0,0]
                #Also if this happens, the runner's out is tracked
                outs+=1
        #Generate a new random integer to decide the outcome of the pitch
        rand=random.randint(0,99)
        #The out variable is a percentage of events where the runner gets out
        if rand<out:
            #If the runner gets out, noone moves and the out is recorded
            outs+=1
        #This is the case of a single
        elif rand<out+first:
            #Runners on second and third score
            pts+=bases[2]+bases[1]
            #Third base empties
            bases[2]=0
            #Second base empties or gets a runner from first
            bases[1]=bases[0]
            #First base gets a runner
            bases[0]=1
        #This is the case of a double
        elif rand<out+first+second:
            #Runners on second and third score
            pts+=bases[2]+bases[1]
            #Third base empties or gets a runner from first
            bases[2]=bases[0]
            #Second base gets a runner
            bases[1]=1
            #First base empties
            bases[0]=0
        #This is the case of a triple
        elif rand<out+first+second+third:
            #Baserunners score, except the hitter
            pts+=sum(bases)
            #The hitter goes to third
            bases[2]=1
            #Second base empties
            bases[1]=0
            #First base empties
            bases[0]=0
        #This is the case of a homerun
        elif rand<out+first+second+third+home:
            #Baserunners score, including the hitter
            pts+=1+sum(bases)
            #Bases empty
            bases=[0]*3
        #This is the case of a walk
        else:
            #This is the case where there is at least one empty base before the walk
            if 0 in bases:
                #Effectively, the first empty base is filled by a runner
                bases[bases.index(0)]=1
            #This is the case where bases are loaded before the walk
            else:
                #A run is scored and nothing else changes
                pts+=1
    #For now, average is actually a sum of the points scored across all trials, updated after each trial
    avg+=pts
    #Outs are reset between each trial
    outs=0
    #Points in the current trial are reset between each trial
    pts=0
    #Bases are emptied between each trial
    bases=[0,0,0]
#We now divide average, which was the sum, by the number of trials to get the actual average
avg=avg/trls
#We print the average
print(avg)
