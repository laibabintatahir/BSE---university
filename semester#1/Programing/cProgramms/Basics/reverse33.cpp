#include<stdio.h>
int main()
{
int num;
printf("----Enter any 5_digit number----\n\nNumber = ");
scanf("%d",&num);
int tenThousandDigit=num%10;
num=num/10;

int thousandDigit=num%10;
num=num/10;

int hundredDigit=num%10;
num=num/10;

int tenDigit=num%10;
num=num/10;

int unitDigit=num%10;
num=num/10;

int reverse=(unitDigit*10 + tenDigit*100 + hundredDigit*1000 + thousandDigit*10000 + tenThousandDigit*100000)/10;

printf("Reverse of digit = %d",reverse);
	
	return 0;
}

