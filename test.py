btDict = {0:8,1:2,2:3}
atDict = {0:0,1:1,2:4}
process = [0,1,2]
bt = [8,2,3]

def waitingTime(btDict,atDict):
    time = 0
    n = len(btDict)

    wt = [0]*n
    count = [0]*n
    finished = [False]*n
    rem_bt = [btDict[i] for i in btDict]
    arrived = [False]*n

    while(True):
        for i in range(n):
            if(not finished[i]):

        if(all(finished)):
            break
    return wt

def turnAroundTime(bt,wt):
    tat = []
    for i in range(len(bt)):
        tat.append(wt[i]+bt[i])
    return tat



wt = waitingTime(btDict,atDict)
tat = turnAroundTime(bt,wt)
print(wt,tat);