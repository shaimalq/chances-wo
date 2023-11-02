p=int(input("entrer le nombre de chevaux joues:"))
n=int(input("entrer le nombre de chevaux partant:"))
y=1  
x=1
for i in range(1,p+1):
    x=x*(i+n-p)
    y=y*i
print("dans l'ordre ,une chance sur",x)
print("dans le desordre , une chance sur",x/y)