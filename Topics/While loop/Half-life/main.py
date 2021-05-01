initial = int(input())
final = int(input())

current = initial
halfs = 0
while current > final:
    current /= 2
    halfs += 1

days = halfs * 12

print(days)
