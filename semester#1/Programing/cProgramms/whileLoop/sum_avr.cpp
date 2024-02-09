#include<stdio.h>
int main()
{
	int sum=0;
	//read 10 num ; sum and avr
	int num;
	//printf("Enter 10 numbers:\n");

	for(int i=1; i<=10; i++)
	{
		printf("Enter num %d : ",i);
	    scanf("%d",&num);
	    sum=sum+num;
	}
	
	printf("..........................\n");
	float avr=sum/10;
	printf("Sum = %d\n",sum);
	printf("Average = %.2f\n",avr);
	printf("..........................\n");	
}
