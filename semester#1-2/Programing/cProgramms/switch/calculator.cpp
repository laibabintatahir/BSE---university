// C program to create Simple Calculator using switch case
#include <stdio.h>
int main()
{
char ch;
int n1,n2;
printf("Enter any operators * / + - :");
scanf("%c ",&ch);
fflush(stdin);
printf("Enter any number n1 :");
scanf("%d ",&n1);
fflush(stdin);
printf("Enter any number n2 :");
scanf("%d ",&n2);
fflush(stdin);

int sum=n1+n2;
int subs=n1-n2;
int multiply=n1*n2;
int division=n1/n2;

switch(ch)
{
	    case '+':
		printf("sum : %d ",sum);
		break;
		case '-':
		printf("Substration : %d ",subs);
		break;
		case '*':
		printf("Multply : %d ",multiply);
		break;
		case '/':
		printf("Division : %d ",division);
		break;
		default:
		printf("invalid");
}
return 0;
}
