# ProcessNUmber: [BurstTime,QueueNumber]
processDict = {0:[3,1],1:[7,1],2:[4,2],3:[2,3]}

process = [0,1,2,3]
bt = [3,7,4,2]
priority = [1,1,2,3]

q1 = 2
q2 = 4

wt = []
tat= []

def waitingTime(p,q1,q2):
    n = len(p)
    time = 0

    finished = [False] *n
    #Index 0 = BT, Index 1 = QueueNumber
    wt = [0]*n
    countInQ1 = [0]*n
    countInQ2 = [0]*n
    
    rem_bt = [p[i][0] for i in p]
    #If completed, set current_queue to 0
    current_queue = [p[i][1] for i in p]
    while (True):
        for i in range(n):
            print(current_queue)
            if(not finished[i]):
                if(current_queue[i] == 1):
                    if(rem_bt[i] <= q1):

                        wt[i] = time 
                        time += rem_bt[i]
                        rem_bt[i] = 0
                        finished[i] = True
                        current_queue[i] = 0
                    else:
                        time += q1
                        rem_bt[i] -= q1
                        current_queue[i] = 2
                        countInQ1[i] = 1

                elif(current_queue[i] == 2 and not(1 in current_queue)):
                    if(rem_bt[i] <= q2):
                        wt[i] = time - (q1*countInQ1[i])
                        time += rem_bt[i]
                        rem_bt[i] = 0
                        finished[i] = True
                        current_queue[i] = 0

                    else:
                        time += q2
                        rem_bt[i] -= q2
                        current_queue[i] = 3
                        countInQ2[i] = 1

                elif(current_queue[i] == 3 and not(2 in current_queue)):
                    wt[i] = time - (q1*countInQ1[i]) - (q2*countInQ2[i])
                    time += rem_bt[i]
                    rem_bt[i] = 0
                    finished[i] = True
                    current_queue[i] = 0


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

wt = waitingTime(processDict,q1,q2)
tat = turnAroundTime(bt,wt)

print("Process\tPriority\tBurst Time\tWaiting Time\t TAT")


for i in range(len(process)):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(process[i],priority[i],bt[i],wt[i],tat[i]))
