//Problem: Write a program that finds the area of a triangle given the len
//gth of its sides: a, b, c.
#include<stdio.h>
#include<math.h>
int main()
{
	float a,b,c;
	
    printf("....Three sides of triangle are....\n\n");
	printf("Enter value of a : ");
	scanf("%f",&a);
	printf("Enter value of b : ");
	scanf("%f",&b);
	printf("Enter value of c : ");
	scanf("%f",&c);
	float s;
	s=(a+b+c)/2;
	
    float  X;
	X=s*(s-a)*(s-b)*(s-c);
	
	float area;
	area = sqrt(X);
	printf("\n....Area of a triangle....\n");
	printf("Area = %0.2f",area);
	return 0;
	
}
