//Input 5 characters from the user and display the number of Vowel, the number of Consonant,
 //the number of Capital Letters, the number of Small Letters, and the number of Digits
 // amongst the 5 values using if-else-if.
#include<stdio.h>
int main()
{
	char ch1,ch2,ch3,ch4,ch5;
	int vowel=0;
	int digit=0;
	int Small_Letters=0;
	int Capital_Letters=0;
	int Consonant=0;
	printf("=====Input 5 characters=====\n");
	printf("\nEnter value of ch1:");
	scanf("%c",&ch1);
	fflush(stdin);
		printf("Enter value of ch2:");
	scanf("%c",&ch2);
	fflush(stdin);
	printf("Enter value of ch3:");
	scanf("%c",&ch3);
		fflush(stdin);

	printf("Enter value of ch4:");
	scanf("%c",&ch4);
		fflush(stdin);

	printf("Enter value of ch5:");
	scanf("%c",&ch5);
	
 if(ch1=='a'||ch1=='e'||ch1=='i'||ch1=='o'||ch1=='u'||ch1=='A'||ch1=='E'||ch1=='I'||ch1=='O'||ch1=='U')
vowel++;
else if((ch1>='a'&&ch1<='z')||(ch1>='A'&&ch1<='Z'))
Consonant++;
{
 if(ch1>='0' && ch1<='9')
digit++;

else if(ch1>='a'&&ch1<='z')
Small_Letters++;

else if(ch1>='A'&&ch1<='Z')
Capital_Letters++;

}

 if(ch2=='a'||ch2=='e'||ch2=='i'||ch2=='o'||ch2=='u'||ch2=='A'||ch2=='E'||ch2=='I'||ch2=='O'||ch2=='U')
vowel++;
else if((ch2>='a'&&ch2<='z')||(ch2>='A'&&ch2<='Z'))
Consonant++;
{
 if(ch2>='0' && ch2<='9')
digit++;

else if(ch2>='a'&&ch2<='z')
Small_Letters++;

else if(ch2>='A'&&ch2<='Z')
Capital_Letters++;


}
 if(ch3=='a'||ch3=='e'||ch3=='i'||ch3=='o'||ch3=='u'||ch3=='A'||ch3=='E'||ch3=='I'||ch3=='O'||ch3=='U')
vowel++;
else if((ch3>='a'&&ch3<='z')||(ch3>='A'&&ch3<='Z'))
Consonant++;
{
 if(ch3>='0' && ch3<='9')
digit++;

else if(ch3>='a'&& ch3<='z')
Small_Letters++;

else if(ch3>='A'&& ch3<='Z')
Capital_Letters++;
}
 if(ch4=='a'||ch4=='e'||ch4=='i'||ch4=='o'||ch4=='u'||ch4=='A'||ch4=='E'||ch4=='I'||ch4=='O'||ch4=='U')
vowel++;
else if((ch4>='a'&&ch4<='z')||(ch4>='A'&&ch4<='Z'))
Consonant++;
{
 if(ch4>='0' && ch4<='9')
digit++;

else if(ch4>='a'&&ch4<='z')
Small_Letters++;

else if(ch4>='A'&&ch4<='Z')
Capital_Letters++;

}
 if(ch5=='a'||ch5=='e'||ch5=='i'||ch5=='o'||ch5=='u'||ch5=='A'||ch5=='E'||ch5=='I'||ch5=='O'||ch5=='U')
vowel++;
else if((ch5>='a'&&ch5<='z')||(ch5>='A'&&ch5<='Z'))  
Consonant++;
{
 if(ch5>='0' && ch5<='9')
digit++;

else if(ch5>='a'&&ch5<='z')
Small_Letters++;

else if(ch5>='A'&&ch5<='Z')
Capital_Letters++;
}

printf("\n==========RESULT=========\n");
printf("\nNo. of vowel           =%d\n",vowel);
printf("No. of Capital_Letters  =%d\n",Capital_Letters);
printf("No. of Small_Letters    =%d\n",Small_Letters);
printf("No. of Consonants       =%d\n",Consonant);
printf("No. of digits           =%d\n",digit);
printf("\n========================\n");
return 0;
}
