//Problem 2: Input 5 values from the user and display the number of positives, 
//the number of negatives, and the number of zeros amongst the 5 values using if-else-if.
#include<stdio.h>
int main()
{
	int n1,n2,n3,n4,n5;
	
	int n=0,p=0,z=0;
	printf("======INPUT VALUES=====\n");
	printf("\nEnter value of n1:");
	scanf("%d",&n1);
	printf("Enter value of n2:");
	scanf("%d",&n2);
	printf("Enter value of n3:");
	scanf("%d",&n3);
	printf("Enter value of n4:");
	scanf("%d",&n4);
	printf("Enter value of n5:");
	scanf("%d",&n5);
	
 if(n1>0)
p++;
{
 if(n1<0)
n++;
else if(n1==0)
z++;
}

	
 if(n2>0)
p++;
{
 if(n2<0)
n++;
else if(n2==0)
z++;
}
	
 if(n3>0)
p++;
{
 if(n3<0)
n++;
else if(n3==0)
z++;
}
	
 if(n4>0)
p++;
{
 if(n4<0)
n++;
else if(n4==0)
z++;
}
	
 if(n5>0)
p++;
{
 if(n5<0)
n++;
else if(n5==0)
z++;
}
printf("\n========RESULT=======\n");
printf("\nNo. of positives =%d\n",p);
printf("No. of negtives  =%d\n",n);
printf("No. of zeros     =%d\n",z);
printf("\n====================\n");
}
