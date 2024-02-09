//Program to relate two integers using =, > or < symbol

#include<stdio.h>
int main()
{
	int num1;
	printf("Enter 1st Number : ");
	scanf("%d",&num1);
	int num2;
	printf("Enter 2nd Number : ");
	scanf("%d",&num2);
	
	if(num1<num2)
	{
		printf("%d is less than %d",num1,num2);
	}
	else if(num1>num2)
	{
		printf("%d is grreater than %d ",num1,num2);
	}
		else 
	{
		printf("%d is equal to %d",num1,num2);
	}
	
	return 0;
	
	}
