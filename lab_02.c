#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<fcntl.h>
int main(){

    int fd[2];
    char b[25]="Hello World",b1[25];
    fd[0] = open("./file.txt",O_CREAT |  O_RDWR);
    fd[1] = open("./file2.txt",O_CREAT | O_RDWR);

    write(fd[0],b,strlen(b));
    lseek(fd[0],6,SEEK_SET);
    int value = read(fd[0],b1,10);
    printf("%d",value);
    write(fd[1],b1,strlen(b1));

    close(fd[0]);
    close(fd[1]);

    return 0;
}