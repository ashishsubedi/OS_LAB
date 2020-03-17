btDict = {0:8,1:2,2:3}
atDict = {0:0,1:1,2:4}

process = [0,1,2]
bt = [8,2,3]

wt = []
tat= []

def waitingTime(btDict,atDict):
    n = len(btDict)
    time = 0

    wt = [0]*n
    finished = [False]*n
    count = [0]*n
    arrived = [False]*n
    rem_bt = [btDict[i] for i in btDict]

    while(True):
        for i in range(n):
            if(not finished[i] and not arrived[i]):
                if(atDict[i]<= time):
                    arrived[i] = True

        arrived_bt = {i:x for i,x in enumerate(rem_bt) if arrived[i] == True and finished[i] == False}

        min_index = min(arrived_bt,key=arrived_bt.get)
        rem_bt[min_index] -= 1
        count[min_index] += 1
        if(rem_bt[min_index] == 0):
            finished[min_index] = True
            wt[min_index] = time - atDict[min_index] - count[min_index] + 1

        time += 1
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

wt = waitingTime(btDict,atDict)
tat = turnAroundTime(bt,wt)

print("Process\tBurst Time\tWaiting Time\t TAT")


for i in range(len(process)):
    print("{}\t\t{}\t\t{}\t\t{}".format(process[i],bt[i],wt[i],tat[i]))
