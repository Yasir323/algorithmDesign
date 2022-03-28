#include <stdio.h>

char* game(int n, int multiplier)
{
    int counter = 0;
    int p = 1;
    char* winner;
    while (p < n)
    {
        p *= multiplier;
        counter ++;
    }
    if (counter % 2 == 0) winner = "ollie";
    else winner = "stan";
    return winner;
}

int main()
{
    int tries, multiplier, target;
    char* winner;
    scanf("%d", &multiplier);
    scanf("%d", &tries);
    for (int i = 0; i < tries; i++)
    {
        scanf("%d", &target);
        winner = game(target, multiplier);
        printf("Winner: %s\n", winner);
    }
    return 0;
}