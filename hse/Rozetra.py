"""

Решение олимпиады по информатике hse
https://olymp.hse.ru/data/2016/10/05/1122855045/%D0%94%D0%B5%D0%BC%D0%BE%20%D0%BE%D1%82%D0%B1%D0%BE%D1%80%D0%B0%202016-2017.pdf

"""

import math

def logs(m):
  print(m)
  return int(input())

n = logs("Введите количество розеток: ")
m = logs("Введите количество эл. приборов: ")
a = logs("Введите сколько стоит 1 розетка: ")
b = logs("Введите сколько стоит 1 мультиплексор: \n")
#n = 1
#m = 3
#a = 1
#b = 10
def main():
  rest = m - n
  if m < 5:
    if a * rest < b:
      print(a * rest)
    else:
      print(b)
  elif m > 5:
    #if (math.floor(m / 5) + 1) * b < rest * a:
    #  print((math.floor(m / 5) + 1) * b)
    if m % 5 != 0:
      summ = 0
      nc = n
      mc = m

      summ += b
      nc -= 1
      mc -= 5
      while nc - 1 > 0:
        if nc == mc:
          break
        summ += a
        nc -= 1
        mc -= 2
      print(summ)
    #else:
    #  print(rest * a)


if __name__ == "__main__":
  main()
