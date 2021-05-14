#include<iostream>
using namespace std;

int main(){
    int a=0,b=1,c=0;
    while(c<255){
    cout<< c <<endl;
    a = b;
    b=c;
    c = a + b;
    }
}