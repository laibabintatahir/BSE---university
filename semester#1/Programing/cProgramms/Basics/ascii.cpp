#include <iostream>
using namespace std;

int main()
{
   char ch,ch1,ch2,ch3,ch4,ch5;
   printf("Enter a character in Uppercase: "); 
   scanf("%c",&ch);
   ch=ch+32;
   ch1=ch+1;
   ch2=ch1+1;
   ch3=ch2+1;
   ch4=ch3+1;
   ch5=ch4+1;
   
   
   printf("Next 5 chracters in Lowercase are :\n %c=%d\n %c=%d\n %c=%d\n %c=%d\n %c=%d\n",ch1,ch1,ch2,ch2,ch3,ch3,ch4,ch4,ch5,ch5); 
   
   
   return 0;
}
