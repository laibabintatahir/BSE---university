
#include<stdio.h>
int main()
{
	int current_year;
	int joined_year;
	int experience;
	printf("Enter Currrent Year :");
	scanf("%d",&current_year);
	
	printf("Enter joined Year :");
	scanf("%d",&joined_year);
	
	experience=current_year-joined_year;
	if(experience>3)
	{
		printf("You got bonous Rs.2500/-");
	}
	return 0;
}
