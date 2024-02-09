#include<stdio.h>
int main(){
	
	int exp;
	int sal=0;
	char gender,qual;
	printf("=======================================================\n");
	printf("=====Program that prints the salary of an employee=====\n");
	printf("=======================================================\n");
	printf("\n\t=== Your Data===\n");
	printf("\n//male=M and female=F");
	printf("\nEnter your Gender :");
	scanf("%c",&gender);
		fflush(stdin);
		
	printf("\n//Graduation=G and Post-Graduation=P"); 
	printf("\nEnter your qualification :");
	scanf("%c",&qual);
		fflush(stdin);
		
	printf("\nWhat's your working experience :");
	scanf("%d",&exp);
		fflush(stdin);
		
	printf("\n\t===Your Salary===\n");
		
	if(gender=='M'&&qual=='P'&&exp>=10)
	sal= 15000;
	else	if(gender=='M'&&qual=='G'&&exp>=10)
    sal= 10000;
	else	if(gender=='M'&&qual=='P'&&exp<10)
    sal=10000;
	else	if(gender=='M'&&qual=='G'&&exp<10)
    sal=7000;
	else	if(gender=='F'&&qual=='P'&&exp>=10)
	sal=12000;
	else	if(gender=='F'&&qual=='G'&&exp>=10)
    sal=9000;
	else	if(gender=='F'&&qual=='P'&&exp<10)
    sal=10000;
	else	if(gender=='F'&&qual=='G'&&exp<10)
	sal = 6000;
	printf("\n salary = %d ",sal);
	
	
}
