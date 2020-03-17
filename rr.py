process = [0,1,2,3]
bt = [7,2,5,1]
wt = []
tat= []
q = 3

def waitingTime(bt,q):
    oldBt = bt
    time = 0
    for i in range(len(bt)):
        if(bt[i]>q):
            
        wt.append(time)
        time = wt[i] + bt[i]
    return wt
def turnAroundTime(bt,wt):
    tat = []
    time = 0
    for i in range(len(bt)):
        time = bt[i]+wt[i]
        tat.append(time)
    return tat

wt = waitingTime(bt)
tat = turnAroundTime(bt,wt)
print(wt)
print("TAT\n ",tat)
