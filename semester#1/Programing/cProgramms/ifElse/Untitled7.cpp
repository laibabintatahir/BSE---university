#include<stdio.h>
int main()
{
int num,ori;

printf("\n Enter any four digit integer no.:");
scanf("%d" &num);
ori= num;
num=num%10*1000+num/10%10*100+num/10%10*10+num/1000;
if(ori==num)
{
printf("Number is palindromic");
}
else
{
printf("Number is not palindromic");
}
}



