// Program to display a number if it is negative

#include<stdio.h>
int main()
{
	int num;
	printf("Enter any Number : ");
	scanf("%d",&num);
	
	if(num%2==0)
	{
		printf("%d is Even",num);
	}
	else
	{
		printf("%d is Odd",num);
	}
	return 0;
	
	
	}
