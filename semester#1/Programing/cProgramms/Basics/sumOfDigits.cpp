//Problem: 
//If a five-digit number is input through the keyboard,
// write a program to print a new number by adding one to each of its digits.
// For example if the number that is input is 12391 then the output should be displayed as 23402

#include<stdio.h>
int main()
{
	int num;
	printf("Enter a 5-digit number : ");
	scanf("%d",&num);
	int num1=num%10;
	num=num/10;
	
	int num2=num%10;
	num=num/10;
	
	int num3=num%10;
	num=num/10;
	
	int num4=num%10;
	num=num/10;
	
	int num5=num%10;
	num=num/10;
	
	int sum=num1+num2+num3+num4+num5;
	
	printf("sum = %d ",sum);
}
