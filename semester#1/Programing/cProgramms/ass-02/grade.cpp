#include<stdio.h>
int main()
{
int b,c,d,op;
	int per;
	printf("===============================================================================\n");
	printf("--------------FEDERAL BOARD OF INTERMEDIATE AND SECONDARY EDUCATION------------\n");
	printf("===============================================================================\n");
	printf("Name : laiba binta tahir\n");
	printf("Roll No : 182532\n");
	printf("Group : Pre-Engineering\n\n");

	printf("Enter chemistry marks :");
	scanf("%d",&b);
	printf("Enter mathematics marks : ");
	scanf("%d",&c);
	printf("Enter physics marks  : ");
	scanf("%d",&d);

	printf("\t\t======================================\n");
	printf("\t\t|SUBJECT      |OBT.MARKS      |T.MARKS\n");
	printf("\t\t======================================\n");
	printf("\t\t|Chemistry    |%d \t\t|100|\n",b);
	printf("\t\t|Mathematics  |%d \t\t|100|\n",c);
	printf("\t\t|Physics      |%d \t\t|100|\n",d);
	
	printf("\t\t======================================\n");
	printf("\n");
	int sum = b+c+d;
	per  = (sum * 100)/300;

printf("Enter 1 to get percentage \nEnter 2 to get grade\nYour Option:");
scanf("%d",&op);

switch(op)
{	
	case 1:
	printf("Percentage = %d",per,"%");
	break;
	
	case 2:	
	{
	switch(per/10)
   {
       case 10 :
       case 9 :
	   case 8 :
           printf("\n Your Grade is: A+");
           break;
       case 7 :
           printf("\n Your Grade is: A" );
           break;
       case 6 :
           printf("\n Your Grade is: B" );
           break;
       case 5 :
           printf("\n Your Grade is: B+" );
           break;
       
       default :
        printf("\n You Grade is: F or Fail");
   }
 }	
	break;
	
	default :
	printf("Invalid Option");	
	}
		return 0 ;
}



