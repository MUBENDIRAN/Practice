#include<stdio.h>
int main()
{
	int P = 2, Q = 6, R = 3;
	int S = 1;
	if ((P+Q) / R > S)
		S = S + Q;
	if ((P - Q) > S)
		S = S - Q;
	else
		S = 5;
	R = 9;
	return 0;
}
