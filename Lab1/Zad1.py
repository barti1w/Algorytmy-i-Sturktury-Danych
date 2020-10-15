def funkcja1(a,b):
    return a[0].upper()+'.'+b.capitalize()
    
def funkcja2(a,b):
    c=list(a)        
    return c[0].upper()+'.'+b.capitalize()

def funkcja3(a,b,c):
    rok=a+b
    return int(rok)-c

def funkcja4(imie, nazwisko, funkcja):    
    return funkcja(imie, nazwisko)
      
def funkcja5(a,b):
    if a>=0 and b>=0 and b!=0:
        return a/b

def funkcja6():
    a=0
    while a<100:
        a=a+int(input('Podaj liczbe: '))
    print('Podales liczby powyżej 100')

def funkcja7(a):    
    return tuple(a)

def funkcja8():
    slow = [] 
    for x in range(5):
        slow.append(input())
    return tuple(slow)


def funkcja9(a):
    x=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
    return x[a-1]

def funkcja10(a):
    if a==a[::-1]:
        return 'true'
    else:
        return 'false'


#print (funkcja1('B','Wojciechowski'))
#print(funkcja2('bartek','wojciechowski'))
#print(funkcja3('20','00',18))
#print(funkcja4('bartek','wojciechowski',funkcja1))
#print(funkcja5(2,-1))
#funkcja6()
#print(funkcja7(['jeden','dwa','trzy','cztery','piec','szesc']))
#print(funkcja8())
#print(funkcja9(6))
#print(funkcja10("takat"))
