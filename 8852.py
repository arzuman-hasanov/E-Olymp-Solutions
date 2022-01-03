n = int(input())

count = ""

a = int(n / 10000)
b = int(n / 1000 % 10)
c = int(n / 100 % 10)
d = int(n % 100 / 10)
e = int(n % 10)

a = str(a)
count += a

c = str(c)
count += c

e = str(e)
count += e

print(count)
