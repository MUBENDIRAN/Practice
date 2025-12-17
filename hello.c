# include <stdio.h>
int main(){
	int x = 1;
	if (x--)
		printf("HEllo\n");
		--x;
	else
		printf("%d",x);
	return 0;
}
