//Write a complete program of tourism guide for three countries 
//(each country contains four cites) using nested if-else-if statement.
#include<stdio.h>
int main()
{	printf("===================================================================== \n");
	printf("................ Tourism Development Corporation......................\n");
	printf("===================================================================== \n");
	int op1;
	printf("\nYou can visit the following countries\nYou are requested to select any of the following options:\n");
	printf("\n1: To visit Pakistan\n2: To visit Turkey \n3: To visit lebnon\n");
		printf("Option :");
	scanf("%d",&op1);
	if(op1==1)
	{	int op2;
		printf("\n\t\t===Pakistan===\n");
		printf("\n1. Lahore\n2. Islamabad \n3. Abbottabad\n4. Peshawar\n");
			printf("Option :");
		scanf("%d",&op2);
		
		if(op2==1)
	    printf("\nTHE BEST PLACES TO VISIT IN LAHORE, PAKISTAN\n 1. BADSHAHI MOSQUE\n 2. FORT ROAD FOOD STREET\n 3.  DELHI GATE MARKET");
	    else if(op2==2)
	    printf("\nTHE BEST PLACES TO VISIT IN ISLAMABAD, PAKISTAN\n 1.The Pakistan Monument\n 2. Faisal Mosque\n 3.Margalla hills and Daman-e-Koh Park");
	    else if(op2==3)
	    printf("\nTHE BEST PLACES TO VISIT IN ABBOTTABAD, PAKISTAN\n 1.NathiaGali\n 2. Miranjani Top\n 3.Shimla Hill");
	    else if(op2==4)
	    	printf("\nTHE BEST PLACES TO VISIT IN PESHAWAR, PAKISTAN\n 1.Qissa Khwani Bazaar\n 2.Mohabbat Khan Mosque \n 3.Bala Hissar Fort");
	}
	else if(op1==2)
	{	int op2;
		printf("\t\t===Turkey===\n");
		printf("\n1. Istanbul\n2. Antalya \n3. Izmir\n4. Ankara\n");
			printf("Option :");
		scanf("%d",&op2);
		
		if(op2==1)
	    printf("\nTHE BEST PLACES TO VISIT IN ISTANBUL, TURKEY\n 1. Blue Mosque\n 2. Süleymaniye Mosque\n 3. Dolmabahçe Palace");
	    else if(op2==2)
	    printf("\nTHE BEST PLACES TO VISIT IN ANTLYA, TURKEY\n 1. Antalya's Old Town\n 2. Konyaalti Beach\n 3. Yivli Minare");
	    else if(op2==3)
	    printf("\nTHE BEST PLACES TO VISIT IN IZMIR, TURKEY\n 1. Izmir Clock Tower\n 2. Key Museum\n 3. SSt. Polycarp Church");
	    else if(op2==4)
	    printf("\nTHE BEST PLACES TO VISIT IN ANKARAR, turkey\n 1.Anatolian Civilizations Museum\n 2.Roman Bath \n 3.Atakule");
	}
	
	else if(op1==3)
	{	int op2;
		printf("\t\t===lebanon===\n");
		printf("\n1. Tripoli\n2. sidon\n3. Beirut\n4. Lebnon\n");
		printf("Option :");
		scanf("%d",&op2);
		
		if(op2==1)
	    printf("\nTHE BEST PLACES TO VISIT IN TRIPOLI, LEBANON\n 1. Clock Tower\n 2. Rabbit Island\n 3. Souk El-Haraj");
	    else if(op2==2)
	    printf("\nTHE BEST PLACES TO VISIT IN SIDON, LEBANON\n 1. Sea Castle\n 2. Soap Museum\n 3. Khan Al Franj");
	    else if(op2==3)
	    printf("\nTHE BEST PLACES TO VISIT IN BEIRUT, LEBANON \n 1. Byblos\n 2. Mohammad Al-Amin Mosque\n 3. Beirut Souks");
	    else if(op2==4)
	    printf("\nTHE BEST PLACES TO VISIT IN , LEBANON \n 1. Baalbek\n 2. Jbeil, Byblos\n 3. Tannourine");
	}
	else 
	printf("invalid option");
	
} 
