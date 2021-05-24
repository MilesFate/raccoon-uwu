#include <stdio.h>

int main(){
    int age;
    char name[20];
    printf("How old are you?\n");
    scanf("%d", &age);
    printf("And what is your name?\n");
    scanf("%s", &name);
    printf("well %s, you are %d years old.\n",name,age);
    if (age >= 18){
        printf("you can legally drive\n");
        if(age >= 21){
            printf("you can legally drink\n");
        }else{
            printf("but you can not legally drink\n");
        }
    }
}