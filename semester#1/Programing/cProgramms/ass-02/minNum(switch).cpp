// Prompt user to input 5 values and display the minimum number amongst them using switch statement.
#include<stdio.h>
int main()
{
	int n1,n2,n3,n4,n5;
	printf("=====input 5 values=====\n");
	    printf("Enter value of n1 :");
	scanf("%d",&n1);
		printf("Enter value of n2 :");
	scanf("%d",&n2);
		printf("Enter value of n3 :");
	scanf("%d",&n3);
		printf("Enter value of n4 :");
	scanf("%d",&n4);
		printf("Enter value of n5 :");
	scanf("%d",&n5);
	
		printf("\n========RESULT=======\n");
	switch(n1<n2 && n1<n3 && n1<n4 && n1<n5)
	{
		case 1:
			printf("%d is minmum number ",n1);
			break;
		case 0:
			switch(n2<n3 && n2<n4 && n2<n5)
			{
			case 1:
			printf("%d is minmum number ",n2);
			break;
			    case 0:
					switch(n3<n4 && n3<n5)
					{
						case 1:
							printf("%d is minmum number ",n3);
							break;
						case 0:
						    switch(n4<n5)
							{
								case 1:
								    printf("%d is minmum number ",n4);	
								    break;
								case 0:
									printf("%d is minmum number ",n5);
							break;
							}	
					}
					
			}
	}
	printf("\n=====================\n");
}
