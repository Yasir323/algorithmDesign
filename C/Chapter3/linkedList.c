#include <stdio.h>
#include <stdlib.h>


typedef struct Node {
    int data;
    struct Node *next;
} Node;


void printList(Node *node)
{
  while (node != NULL)
  {
     printf(" %d ", node->data);
     node = node->next;
  }
  printf("\n");
}

void append(Node **head_ref, int new_data)
{
    /* 1. allocate node */
    Node *new_node = malloc(sizeof(Node));
    Node *last = *head_ref;  /* used in step 5*/
    /* 2. put in the data  */
    new_node->data  = new_data;
    /* 3. This new node is going to be the last node, so make next of
          it as NULL*/
    new_node->next = NULL;
    /* 4. If the Linked List is empty, then make the new node as head */
    if (*head_ref == NULL)
    {
       *head_ref = new_node;
       return;
    }
 
    /* 5. Else traverse till the last node */
    while (last->next != NULL)
        last = last->next;
 
    /* 6. Change the next of last node */
    last->next = new_node;
    return;
}


char *search(Node *node, int x)
{
    if (node == NULL) return "Not Found";
    if (node->data == x) return "Found";
    return search(node->next, x);
}


void delete(Node **head_ref, int x)
{
    Node *temp = *head_ref;
    Node *prev;
    // If the data to be edeleted is the head
    if (temp != NULL && temp->data == x)
    {
        *head_ref = temp->next;
        free(temp);
        return;
    }
    //ITerate all elements
    while (temp != NULL && temp->data != x)
    {
        prev = temp;
        temp = temp->next;
    }
    // If x was not present in list
    if (temp == NULL) return;
    // Unlink the node from list
    prev->next = temp->next;
    free(temp);
}


int main()
{
    Node *head = NULL;
    append(&head, 3);
    append(&head, 7);
    append(&head, 8);
    printList(head);
    printf("%s\n", search(head, 7));
    delete(&head, 7);
    printf("%s\n", search(head, 7));
    return 0;
}