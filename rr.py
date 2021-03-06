process = [0,1,2,3]
bt = [7,2,5,1]
wt = []
tat= []
q = 3

def waitingTime(bt,q):
    remBt = bt.copy()
    wt = [0]* len(bt)
    time = 0
    count = [0]* len(bt)
    finished = [False]*len(bt)

    while(True):
        for i in range(len(bt)):
            if(not finished[i]):
                if(remBt[i]>q):
                    #Remaining time higher than quantum
                    count[i] = count[i] + 1
                    remBt[i] = remBt[i] - q
                    time = time + q
                else:
                    #Process is finished
                        finished[i] = True
                        wt[i] = time - (q*count[i])
                        time = time + remBt[i]
        
        #becomes true if all values in list are true
        if(all(finished)):
            break
    return wt
def turnAroundTime(bt,wt):
    tat = []
    time = 0
    for i in range(len(bt)):
        time = bt[i]+wt[i]
        tat.append(time)
    return tat

wt = waitingTime(bt,q)
tat = turnAroundTime(bt,wt)
print(wt)
print("TAT\n ",tat)
