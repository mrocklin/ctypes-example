#include <stdio.h>
int fib(int i)
{
	if (i<=1)
		return 1;
	else
		return fib(i-1)+fib(i-2);
}

void doubleme(double *A, int n)
{
    int i;
    for(i = 0; i < n; i++)
        A[i]*=2;
}

