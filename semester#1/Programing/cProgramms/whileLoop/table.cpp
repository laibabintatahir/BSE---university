#include<stdio.h>
int main()
{
	int i=1;
	int table;
	printf("Enter a num to get table :");
	scanf("%d",&table);
	printf("\n=====Table Of %d======\n",table);
	
	while(i<=10)
	{
	printf("%d*%d=%d\n",table, i,table*i);
	
	i++;
	}
}
