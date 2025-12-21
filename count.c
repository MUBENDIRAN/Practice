#include<stdio.h>
int main(int num){
	int count = 0;
	while (num){
		count++;
		num >>= 1;
	}
	printf("%d\n",count);
}

