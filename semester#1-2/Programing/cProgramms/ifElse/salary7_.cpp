#include<stdio.h>
int main()
{
	int current_year;
	int joined_year;
	int experience;
	float bonous=0.0;
	int salary;
	printf("Enter Currrent Year :");
	scanf("%d",&current_year);
	
	printf("Enter joined Year :");
	scanf("%d",&joined_year);
	
	printf("Enter Salary :");
	scanf("%d",&salary);
	
	experience=current_year-joined_year;
	
	if(experience>3)
	{
		bonous=0.07*salary;
	}
	float new_salary=salary+bonous;
	
	printf("New Salary : %0.2f ",new_salary);
	return 0;
}
