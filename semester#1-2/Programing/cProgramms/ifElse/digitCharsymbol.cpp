
#include<stdio.h>
int main()
{
	char ch;
	printf("Enter character  :");
	scanf("%c",&ch); 
	
	if(ch >= 'a' && ch <= 'z')
	printf("Albhabets in lower case  %c :",ch);
		
	else if(ch >= 'A' && ch <= 'Z')
	printf("Alphabets in upper case  %c :",ch);
	
	else if(ch>=0 && ch>=9)
	printf("character is digit %c :",ch);
	
	else
	printf("character is special symbol %c :",ch);
	
	return 0;
	
		}
