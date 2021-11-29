'''На вход программе подается натуральное число nn, затем nn строк, 
затем число k — количество поисковых запросов, затем kk строк — поисковые запрос
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
'''



n=int(input())
l=[]
l1=[]
l2=[]
l_2=[]
l_f=[]
for i in range(n):
    x=input()
    l.append(x)
k=int(input())
for y in range(k):
    e=input()
    e=e.lower()
    l1.append(e)
    for j in range(len(e)):
        for o in range(j,len(e)):
            e1=e[0:j]+e[j:o+1].upper()+e[o+1:]
            l1.append(e1)
    for t in range(len(l)):
        for r in range(len(l1)):
            if l1[r] in l[t] and l[t] not in l2:
                l2.append(l[t])
            if l1[r] in l[t] and l1[r] not in l_2:
                l_2.append(l1[r])
for w in range(len(l2)):
    count=0
    for q in range(len(l_2)):
        if l_2[q] in l2[w]:
            count=count+1
        if count==k and l2[w] not in l_f:
            l_f.append(l2[w])
for a in range(len(l)):
    for s in range(len(l_f)):
        if l[a]==l_f[s]:
            print(l[a])
        