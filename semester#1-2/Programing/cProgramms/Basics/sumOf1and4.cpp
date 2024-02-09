#include<stdio.h>
int main()
{
int num;
printf("Enter any 5_digit number = ");
scanf("%d",&num);


int num1=num/10000;
num=num%10000;

int num2=num/1000;
num=num%1000;

int num3=num/100;
num=num%100;

int num4=num/10;
num=num%10;


int sum=num1+num;
;printf("reverse of digit =%d",sum);
	
	return 0;
}
