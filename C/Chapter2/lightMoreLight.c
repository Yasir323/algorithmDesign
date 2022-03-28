#include <stdio.h>


int toggle(int x)
{
    if (x == 0) return 1;
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    int bulb_states[n];
    for (int i = 0; i < n; i++)
        bulb_states[i] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (j % i == 0)
                bulb_states[j - 1] = toggle(bulb_states[j - 1]);
    for (int k = 0; k < n; k++)
    {
        printf("%d\n", bulb_states[k]);
    }
    return 0;
}