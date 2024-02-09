#include<stdio.h>
int main()
{
	
	int table;
	int upperLimit;
	int lowerLimit;
	
	printf("Enter a num to get table :");
	scanf("%d",&table);
	printf("Enter lowerLimit :"); 
	scanf("%d",&lowerLimit); 
	printf("Enter upperLimit :"); 
	scanf("%d",&upperLimit); 
	
	printf("\n========Table Of %d=========\n",table);
	
	while(lowerLimit<=upperLimit)
	{
	printf("\t| %d*%d=%d |\n",table, lowerLimit,table*lowerLimit);
	
	lowerLimit++;
	}
}
