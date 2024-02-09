//Program to find the largest number of the three

#include<stdio.h>
int main()
{
	int num1;
	printf("Enter 1st Number : ");
	scanf("%d",&num1);
	int num2;
	printf("Enter 2nd Number : ");
	scanf("%d",&num2);
		int num3;
	printf("Enter 3rd Number : ");
	scanf("%d",&num3);
	
	if(num1>num2 && num1>num3) 
	{
		printf("%d is greater among all",num1);
	}
	else if(num2>num3 && num2>num1)
	{
		printf("%d is grreater among all",num2);
	}
		else 
	{
		printf("%d is grreater among all",num3);
	}
	
	return 0;
	
	}
