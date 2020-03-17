#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main(){
    int a = 0;
    int pid = fork();
    if(pid==0){
        a = 2;
        printf("Child pid %d\n",getpid());
        printf("Process of parent %d\n",getppid());
        printf("value of a in child %d\n",a);
        execlp("/bin/ls","ls",(char*)NULL);
        exit(0);
    }else{

        printf("Parent %d\n",pid);
        printf("Value of a in parent %d\n",a);
        exit(0);
    }
    return 0;
}