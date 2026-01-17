#include <stdio.h>
int main(){
	int a = 1;
	if (a--)
		printf("true\n");
	if (++a)
		printf("false\n");
	return 0;
}
