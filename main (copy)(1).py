# implement the factorial recursive funtion


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = 4

res = fact_rec(number)
print("the fasctorial of {} is {}.".format(number, res))
