#include <stdio.h>
#include <stdlib.h>

#define PQ_SIZE 10


typedef struct {
    int q[PQ_SIZE];  // Body of queue
    int n;                     // number of queue elements
} priority_queue;


int parent(int n)
{
    if (n == 0) return -1;
    else return ((int) n / 2); // implicitly take floor of n / 2
}


int young_children(int n)
{
    return (2 * n + 1);
}


void pq_swap(priority_queue *pq, int x, int y)
{
    int temp = pq->q[x];
    pq->q[x] = pq->q[y];
    pq->q[y] = temp;
}


void bubble_up(priority_queue *pq, int p)
{
    if (parent(p) == -1) return;
    if (pq->q[parent(p)] > pq->q[p])
    {
        pq_swap(pq, p, parent(p));
        bubble_up(pq, parent(p));
    }
}


void insert(priority_queue *pq, int x)
{
    if (pq->n >= PQ_SIZE) printf("Warning! Priority Queue Overflow.");
    else
    {
        pq->q[pq->n] = x;
        bubble_up(pq, pq->n);
        pq->n = pq->n + 1;
    }
}


void pq_init(priority_queue *pq)
{
    pq->n = 0;
}


void make_heap(priority_queue *pq, int s[], int n)
{
    pq_init(pq);
    for (int i = 0; i < n; i++)
        insert(pq, s[i]);
}


void bubble_down(priority_queue *pq, int p)
{
    int c; // child index
    int min_index; // index of the smallest child
    c = young_children(p);
    min_index = p;
    for (int i = 0; i <= 1; i++)
    {
        // Compare with both children
        if (c + i <= pq->n)
            if (pq->q[min_index] > pq->q[c+i])
                min_index = c + i;
    }
    if (min_index != p)
    {
        pq_swap(pq, p, min_index);
        bubble_down(pq, min_index);
    }
}


int extract_min(priority_queue *pq)
{
    int min = -1;
    if (pq->n <= 0) printf("Warning! Queue is empty!");
    else
    {
        min = pq->q[0];
        pq->q[0] = pq->q[pq->n - 1];
        pq->n = pq->n - 1;
        bubble_down(pq, 0);
    }
    return min;
}


void print_pq(priority_queue *pq)
{
    for (int i = 0; i < pq->n; i++)
    {
        printf("%d\n", pq->q[i]);
    }
}


void heap_sort(int *array, int n)
{
    priority_queue *pq2 = malloc(sizeof(priority_queue) * n);
    make_heap(pq2, array, n);
    for (int i = 0; i < n; i++)
    {
        array[i] = extract_min(pq2);
        printf("%d\n", array[i]);
    }
}


int main()
{
    priority_queue *pq = malloc(sizeof(priority_queue) * PQ_SIZE);
    int s[PQ_SIZE] = {11, 32, 54, 67, 2, 34, 56, 55, 90, 6};
    make_heap(pq, s, PQ_SIZE);
    print_pq(pq);
    printf("Minimum: %d\n", extract_min(pq));
    printf("After extracting minimum:\n");
    print_pq(pq);
    int r[PQ_SIZE] = {11, 32, 54, 67, 2, 34, 56, 55, 90, 6};
    printf("\nSorted Array:\n");
    heap_sort(r, PQ_SIZE);
}
