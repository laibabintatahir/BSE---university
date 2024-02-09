
#include<stdio.h>
int main()
{
	int day,month,year;
	    printf("enter day :");
	scanf("%d",&day);
		printf("enter month :");
	scanf("%d",&month);
		printf("enter year :");
	scanf("%d",&year);
	
	if(month==1) 
	printf("%d : Januarary : %d",day,year);
	
	else	if(month==2) 
	printf("%d : Feburary : %d",day,year);
	else	if(month==3) 
	
	printf("%d :March: %d",day,year);
	
	else	if(month==4) 
	printf("%d : April : %d",day,year);
	
	else	if(month==5) 
	printf("%d : May : %d",day,year);
	
	else	if(month==6) 
	printf("%d : June : %d",day,year);
	
	else	if(month==7) 
	printf("%d : July : %d",day,year);
	
	else	if(month==8) 
	printf("%d : August : %d",day,year);
	
	else	if(month==9) 
	printf("%d : September : %d",day,year);
	
	else	if(month==10) 
	printf("%d : October : %d",day,year);
		
	else if(month==11) 
	printf("%d : Nopvember : %d",day,year);
	
	else	if(month==12) 
	printf("%d : December : %d",day,year);
	else
	printf("invalid");
	
	
	
	return 0;
	
	
	}
