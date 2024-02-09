 #include<stdio.h>
int main()
{
	float num;
	printf("enter float no :");
	scanf("%f",&num);
	
	int whole_num=num;
	float fractional_num=num-whole_num;
	
	printf("fractional part is :%f\n",fractional_num);
	printf("whole part is :%d",whole_num);
	return 0;
} 


#include<stdio.h>
int main()
{
	int C;
	printf("enter value of C :");
	scanf("%d",&C);
	
	int D;
	printf("enter value of D :");
	scanf("%d",&D);
	printf("Before swaping C is :%d\n", C);
	
	printf("Before swaping D is :%d\n", D);
int temp_variable;
     
    temp_variable=C;
    C=D;
    D=temp_variable;
	
	printf("after swaping C is: %d\n",C);
	
	printf("after swaping D is: %d",D);
	
	return 0;
} 

#include<stdio.h>
int main()
{
	int C;
	printf("enter value of C :");
	scanf("%d",&C);
	
	int D;
	printf("enter value of D :");
	scanf("%d",&D);
	printf("Before swaping C is :%d\n", C);
	printf("Before swaping D is :%d\n", D);

    D=D-C;
    C=C+D;
    D=C-D;
	
	printf("after swaping C is: %d\n",C);
	printf("after swaping D is: %d",D);
	
	return 0;
} 

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
int num5=num%10;

int sum=num1+num2+num3+num4+num5;
printf("sum of digits = %d",sum);
	
	return 0;
} 

#include<stdio.h>
int main()
{
int num;
printf("Enter any 5_digit number = ");
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

printf("reverse of digit =%d%d%d%d%d",num1,num2,num3,num4,num5);
	
	return 0;
}

 #include<stdio.h>
int main()
{
int num;
printf("Enter any 5_digit number = ");
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
printf("sum of digits = %d",sum);
	
	return 0;
} 

//Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area
#include<stdio.h>
int main()
{
float radius;
	float pi=3.14;
	printf("Radius is : ");
	scanf("%f",&radius);
	
	int  diameter=radius/2;
	int  circumference=2*pi*radius;
  int area=pi*radius*radius;
	
	printf("Diameter is : %i\n",diameter);
	printf("Circumference is  :%i\n",circumference);
	printf("Area is  :%i\n",area);
	

	return 0;
}


 //  Write a program converts a temperature from Celsius to Fahrenheit. Use the following formula:  F = 1.8 x C + 32 .
#include<stdio.h>
int main()
{
	int temperature;
	printf("Temperature is : ");
	scanf("%i",&temperature);
	
	printf("temperature in celusis :");
	
	int tempCelsius=(temperature-32)*5/9;
	
	printf("%i",tempCelsius);
	printf("\ntemperature in farenhite :");
	int tempFaren=1.8*temperature + 32 ;
	
	printf("%i",tempFaren);

	return 0;
}
