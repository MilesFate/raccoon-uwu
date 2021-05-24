// vim is pretty fun ngl
#include <stdio.h>

void check(){
	int a,b,c;
	a=0;
	b=1;
	c=0;
	do{
		printf("%d\n",c);
		a = b;
		b = c; 
		c = a + b;
		}while(c < 255);
}
int main(){
	int test = 0;
	printf("hello friend\n");
	printf("%d\n",test);
	check();
}
