//Two characters are input through the keyboard into two locations C and D
//.Write a program to interchange the contents of C and D 
// without using any additional variable. 


#include<stdio.h>
int main()
{
	int C;
	printf("Enter value of C: ");
	scanf("%d",&C);
	
	int D;
    printf("Enter value of D: ");
    scanf("%d",&D);
    printf("\nBefore swaping  C is : %d\n",C);
    printf("Before swaping  D is : %d\n",D); 
    D=C+D;
    C=D-C;
    D=D-C;
    printf("\nAfter swaping the value of C is  : %d ",C);
    printf("\nAfter swaping the value of D is  : %d ",D);
}

	

