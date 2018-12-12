#include <stdio.h>

int main()
{
	int a, b;
	char buf;
	scanf("%d %d", &a, &b);
	scanf(" %c", &buf);
	while(a<=b)
	{
		if(buf=='p') {if(a%2==0) printf("%d ", a);}
		else if(a%2==1) printf("%d ", a);
		a=a+1;
	}
}
