import random

def game(n, multiplier, p):
    counter = 0
    while p < n:
        p *= multiplier
        counter += 1
    if counter % 2 == 0:
        return 'ollie'
    return 'stan'


tries = int(input("Number of tries: "))

targets = []
for i in range(tries):
    targets.append(int(input("Target: ")))
multiplier = int(input("Multiplier: "))

for target in targets:
    print(game(target, multiplier, 1))