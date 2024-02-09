//vowel consonant using switch

#include <stdio.h>
int main()
{
char ch;
printf("Enter alphabet : ");
scanf("%c ",&ch);

switch(ch)
{
	    case 'a':
		printf("vowel");
		break;
		
		case 'e':
		printf("vowel");
		break;
		
		case 'i':
		printf("vowel");
		break;
		
		case 'o':
		printf("vowel");
		break;
		
		case 'u':
		printf("vowel");
		break;
		
		default:
		printf("consonants");
}
return 0;
}
