#include<stdio.h>
int main()
{
	int i=1;
	int num;
	printf("Enter a num :");
	scanf("%d",&num);

	
	while(i<=num)
	{
		if(i%2==0) 
		{
				printf("\n======Even Numbers=====\n");
				printf("%d\n", i);
		}  
	else
	{
	 printf("\n======odd Numbers=====\n");
	 printf("%d\n", i);
	 
	}
	i++;
	}
}
