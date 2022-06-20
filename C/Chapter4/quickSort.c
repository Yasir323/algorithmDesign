#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int s[], int low, int high)
{
    int p = high;                // Pivot element index
    int firstHigh = low;        // Divider position for pivot element
    for (int i = low; i < high; i++)
    {
        if (s[i] < s[p])
        {
            swap(&s[i], &s[firstHigh]);
            firstHigh++;
        }
    }
    swap(&s[p], &s[firstHigh]);
    return firstHigh;
}


void quickSort(int array[], int low, int high)
{
    int p;
    if (low < high)
    {
        p = partition(array, low, high);
        quickSort(array, low, p - 1);
        quickSort(array, p + 1, high);
    }
}

int main()
{
    int s[10] = {11, 32, 54, 67, 2, 34, 56, 55, 90, 6};
    printf("Before sorting:\n");
    for (int i = 0; i < 10; i++) printf("%d\n", s[i]);
    quickSort(s, 0, 9);
    printf("After sorting:\n");
    for (int i = 0; i < 10; i++) printf("%d\n", s[i]);
    return 0;
}