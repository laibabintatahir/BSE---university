//write a program to solve the quadratic equation using quadratic formulas
#include <stdio.h>
#include <math.h>
int main()
{
float a,b,c,X1,X2;
printf("Please enter a :");
scanf("%f",&a);
printf("Please enter b :");
scanf("%f",&b);
printf("Please enter c :");
scanf("%f",&c);
X1 = (-b + sqrt(b*b-4*a*c) ) / (2*a);
X2 = (-b - sqrt(b*b-4*a*c) ) / (2*a);
printf("\n First root :%0.2f ",X1);
printf("\n Second root :%0.2f ",X2);
printf("\n ");
return 0;
}

