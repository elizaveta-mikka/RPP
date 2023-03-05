s = str(input())
l = s.split()
m = int(l[0])
for i in l:
    if int(i) < m:
        m = int(i)
print("Минимальный элемент списка: " + str(m))