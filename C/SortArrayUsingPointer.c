#include <stdio.h>

void sortIncreasing( int arr[], int size ){
    int i, j, temp;
    for(i = 0; i < size; i++){
        for(j = i + 1; j < size; j++){
            if(*((int*)arr[j]) < *((int*)arr[i]))
			//if(arr[j] < arr[i])
			{
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
}

void sortDecreasing( int arr[], int size ){
    int i, j, temp;
    for(i = 0; i < size; i++){
        for(j = i + 1; j < size; j++){
            if(*((int*)arr[j]) > *((int*)arr[i]))
			{
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
}

void main()
{
	int n,i;   
	printf("Input the number of elements to be stored in array: ");
	scanf("%d",&n);
	int *arr = (int *)malloc(sizeof(int)*n);
	int *increasing = (int *)malloc(sizeof(int)*n); // dpointer array to store increasing index
	int *decreasing = (int *)malloc(sizeof(int)*n); // pointer array to store dewcreasing index
	for(i=0;i<n;i++)
	{
		printf("Enter element-%d: ", i+1);
		scanf("%d",&arr[i]);
		increasing[i] = &arr[i];
		decreasing[i] = &arr[i];
	}   
	sortIncreasing(increasing, n);
	sortDecreasing(decreasing, n);
	printf("Ascending\tOriginal\tDescending\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t\t%d\t\t%d\n",*((int*)increasing[i]),arr[i],*((int*)decreasing[i]));
	}
}