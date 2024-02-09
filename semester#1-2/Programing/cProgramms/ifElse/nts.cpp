
#include<stdio.h>
int main()
{
	int Nts_marks;
	int FSC_marks;
	
	printf("Enter Nts_marks: ");
	scanf("%d",&Nts_marks);
		
	printf("Enter FSC_marks : ");
	scanf("%d",&FSC_marks);
	
	
	if(Nts_marks>50 && FSC_marks>50 )
	{
		printf("You are eligible");
	}
	else
	{
		printf("Sorry, better luck for the next time");
	}
	return 0;
	
	
	}
