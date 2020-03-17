
process = {0:7,1:2,2:5,3:1}
bt = [7,2,5,1]
wt = []
tat= []

sorted_process = sorted(process,key=process.get)
sorted_bt = sorted(bt)

def waitingTime(bt):
    wt = []
    time = 0
    for i in range(len(bt)):
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

wt = waitingTime(sorted_bt)
tat = turnAroundTime(sorted_bt,wt)

print("Process\tBurst Time\tWaiting Time\t TAT")
for i in range(len(sorted_process)):
    print("{}\t\t{}\t\t{}\t\t{}".format(sorted_process[i],sorted_bt[i],wt[i],tat[i]))
