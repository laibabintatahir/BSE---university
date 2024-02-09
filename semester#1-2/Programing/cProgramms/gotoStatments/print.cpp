#include<stdio.h>
int main()
{
	
	int uperLimit,lowerLimit;
	printf("enter lower Limit  :");
	scanf("%d",&lowerLimit);
		printf("enter uperLimit  :");
	scanf("%d",&uperLimit);
	print:
	printf("%d\n",lowerLimit);
	lowerLimit++;
	if(lowerLimit<=uperLimit)
	goto print;
}
