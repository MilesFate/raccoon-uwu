#include<iostream>
using namespace std;
void math(){
    int a = 0, b = 1, c = 2, d = 3, e = 4;
    a = b - c + d * e;
    printf("%d\n", a); // will print 1-2+3*4 = 11
    int o = 10;
    printf("%d\n",o); 
}
void write(){
    printf("Hello\n");
    printf("this\n");
    printf("is\n");
    printf("anton\n");
}
void fib(){
    int a=0,b=1,c=0;
    do{
    printf("%d\n",c);
    a=b;
    b=c;
    c=a+b;
    }while(c<255);
}
void jhin(){
    int i;
    for (i = 1;i!=5;++i)
    {
        printf("jhin says %d\n",i);
    }
}

// this one works weird. the code it right and works in atom but just doesnt work right
// using linux commands
void input(){
    int numb;
    printf("insert num\n");
    scanf("%d\n",&numb);
    printf("your number %d\n",numb);
}

int main(){
    jhin();
}