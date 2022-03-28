#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Stack {
    int top;
    unsigned capacity;
    int *array;
} stack;


stack *createStack(unsigned capacity)
{
    stack *s = malloc(sizeof(stack));
    s->capacity = capacity;
    s->top = -1;
    s->array = malloc(s->capacity * sizeof(int));
    return s;
}


int isFull(stack *s)
{
    return s->top == s->capacity - 1;
}

int isEmpty(stack *s)
{
    return s->top == -1;
}

void push(stack *s, int data)
{
    if (isFull(s)) return;
    s->array[++s->top] = data;
    printf("%d pushed to stack.\n", data);
}

int pop(stack *s)
{
    if (isEmpty(s)) return INT_MIN;
    return s->array[s->top--];
}

int peek(stack *s)
{
    if (isEmpty(s)) return INT_MIN;
    return s->array[s->top];
}


int main()
{
    stack* myStack = createStack(100);
    
    push(myStack, 10);
    push(myStack, 20);
    push(myStack, 30);
    
    printf("%d popped from stack\n", pop(myStack));
    
    return 0;
}
