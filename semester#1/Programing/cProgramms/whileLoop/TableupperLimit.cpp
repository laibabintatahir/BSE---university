#include<stdio.h>
int main()
{
	int i=1;
	int table;
	int upperLimit;
	printf("Enter a num to get table :");
	scanf("%d",&table);
	printf("Enter upperLimit "); 
	scanf("%d",&upperLimit); 

	printf("\n=====Table Of %d======\n",table);
	
	while(i<=upperLimit)
	{
	printf("%d*%d=%d\n",table, i,table*i);
	
	i++;
	}
}
