#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main(){
    int a = 0;
    int i = fork();
    if(i>=0){
        a = 2;
        printf("Child %d\n",getppid());
        exit(1);
    }else{

        printf("Parent %d\n",i);
    }
    return 0;
}