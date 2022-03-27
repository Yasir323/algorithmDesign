def func(n):
  while True:
    print(n)
    if n == 1:
      break
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1


func(22)
