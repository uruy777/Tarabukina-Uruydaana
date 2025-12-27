#1 задание
"""with open ("","") as f:
n = f.readlines()
n = [int(el) for el in n]
print(n)

count = 0
max_sum = 0

for i in range(len(a) - 1):
 a = n[I]
    b = n[I+1]

    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        count += 1
        if a + b > max_sum:
            max_sum = a + b

print(count, max_sum)"""

#2 задание

with open("", "") as f:
    n = [int(el) for el in f]
    max_el = 0

    for el in n:
        if str(el)[-3:] == '562':
            if max_el < el:
                max_el = el
    print(max_el)

    c = 0
    max_sum = 0
    for i in range(len(n) - 3):
        l = [n[1], n[i + 1], n[i + 2], n[i+3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= 1 and len(lnot5) >= 2:
            if len(lcrat3) < len(lcrat7):
                if sum(l) > max_el and sum(l) < max_el*2:
                    c += 1
                    if max_sum < sum(l):
                        max_sum = sum(l)
    print(c, max_sum)

#3 задание

with open ("","") as f:
n = [int(x) for x in f]

count = 0
max_sum = 0

for i in range(len(a) - 1):
 a = n[I]
    b = n[I+1]
     if (
