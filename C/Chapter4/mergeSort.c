#include <stdio.h>
#include "queue.h"

void merge(int array[], int low, int middle, int high);

void mergeSort(int array[], int low, int high);

int main()
{
    int s[10] = {11, 32, 54, 67, 2, 34, 56, 55, 90, 6};
    printf("Before sorting:\n");
    for (int i = 0; i < 10; i++) printf("%d\n", s[i]);
    mergeSort(s, 0, 9);
    printf("After sorting:\n");
    for (int i = 0; i < 10; i++) printf("%d\n", s[i]);
}


void mergeSort(int array[], int low, int high)  // O(log n)
{
    int middle;
    if (low < high)
    {
        middle = low + (high - low) / 2;
        mergeSort(array, low, middle);
        mergeSort(array, middle + 1, high);
        merge(array, low, middle, high);
    }
}


void merge(int s[], int low, int middle, int high) // O(n)
{
    Queue* buffer1 = createQueue(10);
    Queue* buffer2 = createQueue(10);
    for (int i = low; i <= middle; i++) enqueue(buffer1, s[i]);
    for (int i = middle + 1; i <= high; i++) enqueue(buffer2, s[i]);

    int i = low;
    while(!(isEmpty(buffer1) || isEmpty(buffer2)))
    {
        if (front(buffer1) <= front(buffer2))
        {
            s[i++] = dequeue(buffer1);
        }
        else
        {
            
            s[i++] = dequeue(buffer2);
        }
    }
    while (!isEmpty(buffer1)) s[i++] = dequeue(buffer1);
    while (!isEmpty(buffer2)) s[i++] = dequeue(buffer2);
}
