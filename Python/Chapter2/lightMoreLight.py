n = int(input())
bulb_state = [True] * n


def toggle(x: bool):
    return not x


for i in range(1, n + 1):
    for j in range(1, n + 1):
        bulb_state[j - 1] = toggle(bulb_state[j - 1]) if j % i == 0 else bulb_state[j - 1]
print(bulb_state)
