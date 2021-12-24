'''На вход программе подается строка текста, содержащая целые числа. 
Из данной строки формируется список чисел. Напишите программу,
которая сортирует и выводит данный список сначала по возрастанию,
а затем по убыванию. '''
s = input()
l0=s.split()
l=l0.copy()
l2=l0.copy()
l1=[]
ld=[]
# список отсортирован по убыванию
mx_=l2[0]
for c in range(len(l2)):
    if int(l2[c])>=int(mx_):
            mx_=l2[c]
for j in range(len(l2)):
    mn_=l2[0]
    for i in range(len(l2)):
        if int(l2[i])<=int(mn_):
            mn_=l2[i]
            s_i=i
    ld.append(mn_)
    l2[s_i]=mx_
print(*ld)
# список отсортирован по возростанию
min_=l[0]
for c in range(len(l)):
    if int(l[c])<=int(min_):
            min_=l[c]
for j in range(len(l)):
    max_=l[0]
    for i in range(len(l)):
        if int(l[i])>=int(max_):
            max_=l[i]
            si=i
    l1.append(max_)
    l[si]=min_
print(*l1)