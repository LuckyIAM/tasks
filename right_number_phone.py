'''
На вход программе подается строка текста. Напишите программу, 
которая определяет является ли введенная строка корректным телефонным номером. 
Строка текста является корректным телефонным номером если она имеет формат:
abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
'''
s=input()
l=list(s) 
count=0
if len(l)==12 and l.index('-')==3:
    del l[3]
    if l.index('-')==6:
        del l[6]
        for i in l:
            if i in '0123456789' :
                count+=1
    if count==len(l):
        print('YES')
    else:
        print('NO')

elif len(l)==14 and l[0]=='7' and l.index('-')==1:
    del l[1]
    if l.index('-')==4:
        del l[4]
        if l.index('-')==7:
            del l[7]
            for i in l:
                if i in '0123456789' :
                    count+=1
    if count==len(l):
        print('YES')
    else:
        print('NO')
else: 
    print('NO')
    
            

        
        