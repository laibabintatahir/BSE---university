#include<stdio.h>
int main()
{
	int num;
	
	printf("num is:");
	scanf("%d",&num);
	int num1=num%2==0;
	int num2=num%2==1;
	
	printf("For Even %d = %d\n",num,num1);
	printf("For Odd %d = %d\n",num,num2);
	printf("// 0 for False\n// 1 for True");
	
	
	

}
