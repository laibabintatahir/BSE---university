#include<stdio.h>
int main()
{
	int num;
	int i;
	int uperLimit,lowerLimit;
	printf("enter no whse table you want :");
	scanf("%d",&num);
	printf("enter lower Limit of table :");
	scanf("%d",&lowerLimit);
		printf("enter uperLimit of table :");
	scanf("%d",&uperLimit);

		table:
	printf("%d*%d=%d\n",num,lowerLimit,num*lowerLimit);
	lowerLimit++;
	if(lowerLimit<=uperLimit)
	goto table;
}
