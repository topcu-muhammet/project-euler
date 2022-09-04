"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""
import time
start=time.time()
perms=[]
for a in range(1, 10000000):
    for b in range(2,7):
        perms.append(sorted(list(str(a*b))))
    if perms.count(perms[0])==5:
        print(a)
        break
    else:
        perms=[]
end=time.time()
print(end-start)