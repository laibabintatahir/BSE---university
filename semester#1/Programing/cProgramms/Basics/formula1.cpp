#include<stdio.h>
int main()
{
int a;
printf("Enter value of a :");
scanf("%d",&a);
int b;
printf("Enter value of b :");
scanf("%d",&b);		
int formula=a*a*a*a - 4*a*a*a*b + 6*a*a*b*b -  4*a*b*b*b + b*b*b*b ;

printf("formula =");
printf("a*a*a*a - 4*a*a*a*b + 6*a*a*b*b - 4*a*b*b*b + b*b*b*b\n\t=%d*%d*%d*%d - 4*%d*%d*%d*%d + 6*%d*%d*%d*%d  4*%d*%d*%d*%d + %d*%d*%d*%d \n\t=%d",a,a,a,a  ,a,a,a,b , a,a,b,b , a,b,b,b ,b,b,b,b,formula);
}   



