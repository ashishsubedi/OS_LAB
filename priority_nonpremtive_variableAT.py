# Process:[Priority,AT,BT]
processDict = {0:[1,0,4],1:[2,6,2],2:[3,2,10],3:[4,5,11]}
bt = [processDict[i][2] for i in processDict]

def waitingTime(p):
    time = 0
    n = len(p)

    at = [p[i][1] for i in p]
    bt = [p[i][2] for i in p]

    wt = [0]*n
    finished = [False]*n
    arrived = [False]*n
    
    while(True):
        for i in range(n):
            if(not finished[i] and not arrived[i]):
                if(at[i]<= time):
                    arrived[i] = True

        arrived_bt = {i:[p[i][0],p[i][2]] for i in p if arrived[i] and not finished[i]}
        
        min_index = min(arrived_bt,key = lambda x: p[x][0])
        wt[min_index] = time - at[min_index]
        finished[min_index] = True
        time += bt[min_index]

        if(all(finished)):
            break
    return wt

def turnAroundTime(bt,wt):
    tat = []
    for i in range(len(bt)):
        tat.append(bt[i]+wt[i])
    return tat

wt = waitingTime(processDict)
tat = turnAroundTime(bt,wt)
print(wt)
print(tat)