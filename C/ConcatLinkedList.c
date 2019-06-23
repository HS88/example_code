#include<stdio.h>
#include<stdlib.h>
 
/* A linked list node */
struct Node
{
    char  *data;
    struct Node *next;
};
 
/* Function to add a node at the beginning of Linked List*/
void push(struct Node** head, char data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data  = data;
    new_node->next = (*head);
    *head = new_node;
}
 
void printList(struct Node *node)
{
    while (node != NULL)
    {
        printf("%c",node->data);
        node = node->next;
    }
}

void concatenate( struct Node** concatList, struct Node *head1, struct Node *head2){
	struct Node *temp_head = (struct Node*)malloc(sizeof(struct Node));
	struct Node *tail = NULL;
	if(head1 == NULL && head2 == NULL )
		return;
	
	if( head1 != NULL ){
		temp_head -> data = head1->data;
		temp_head -> next = head1->next;
		tail = temp_head;
		head1 = head1->next;
	}
	else if( head2 != NULL){
		temp_head -> data = head2->data;
		temp_head -> next = head2->next;
		tail = temp_head;
		head1 = head1->next;
	}
	
	while(head1 != NULL){
		struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
		new_node -> data = head1->data;
		new_node -> next = head1->next;
		tail->next = new_node;
		head1 = head1->next;
		tail = tail->next;
	}
	while(head2 != NULL){
		struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
		new_node -> data = head2->data;
		new_node -> next = head2->next;
		tail->next = new_node;
		head2 = head2->next;
		tail = tail->next;
	}
	*concatList = temp_head;
}

/* Driver program to test above function */
int main()
{
    struct Node *list1= NULL;
	struct Node *list2 = NULL;
	struct Node *list3= NULL;
    char arr1[] = {'h','e','l','l','o'};
	char arr2[] = {'w','o','r','l','d'};
	int i;
    for (i=4; i>=0; i--){
       push(&list1, arr1[i]);
	   push(&list2, arr2[i]);
	}
    printf("Created two linked lists of characters:\n");
    printf("First List: ");
	printList(list1);
	printf("\nSecond List: ");
	printList(list2);
	concatenate(&list3, list1, list2);
	printf("\nConcatenated list: ");
	printList(list3);
	
    return 0;
}