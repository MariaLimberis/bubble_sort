#7 6 4 3
import random

a = [7, 6, 4, 3]
def sort_first_pass(a, n):
   for i in range(n):
       if a[i] > a[i+1]:
          c = a[i]
          d = a[i+1]
          a[i] = d
          a[i+1] = c

   return a

def sort(a):
    for i in range(len(a)):
        n = len(a) - i - 1
        sort_first_pass(a, n)
    return a
#print(a)
#print(sort(a))


assert sort_first_pass(a, 3) == [6, 4, 3, 7], sort_first_pass(a, 3)
assert sort(a) == [3, 4, 6, 7], sort(a)

xs = [random.randint(-100, 100) for _ in range(1000)]

assert sort(xs) == sorted(xs)
