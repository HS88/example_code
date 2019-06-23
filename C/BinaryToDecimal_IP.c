#include <stdio.h>  
#include <string.h>
#include <math.h>	

int main()  
{  
    char input[33];  
	printf("Enter a 32 bit binary number: ");
	scanf("%32[^\n]", input);
	int i = 0;
	int j = 3;
	int exp = 0;
	int sum = 0;
	int values[4];
	for( i = 31;i >= 0; i--){ 
		sum = sum + (input[i]-'0')*pow(2,exp);
		exp = exp + 1;
		if( i%8 == 0 && i!=0 )
		{		
			values[j] = sum;
			sum = exp = 0;
			j--;
		}
	}
	values[0]=sum;
	printf("IP address: %d.%d.%d.%d",values[0], values[1], values[2], values[3]);
	return 0;
}  