def reverse_integer(a: int):
  reversed_int = 0
  while a:
    reversed_int = reversed_int * 10
    reversed_int += a % 10
    a = a // 10
  print(reversed_int)

reverse_integer(1234)