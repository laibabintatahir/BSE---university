#include<stdio.h>
int main()
{
	int i=1;
	int num;
	printf("Enter a num :");
	scanf("%d",&num);
	printf("\n======Even Numbers=====\n");
	
	while(i<=num)
	{
		if(i%2==0)
	    printf("%d\n", i);
	
	i++;
	}
}
