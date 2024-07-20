'''print("operation you can perform:\n 1.Addition \n 2.Subtraction\n"
      "3.Multiply \n 4.Division \n 5.Floor Division \n 6.Exponent")
a=int(input("enter the number for a operation : "))
num1= int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
if a==1:
    print("Addition of",num1,"+",num2,"is",num1+num2)
elif a==2:
    print("Subtraction of",num1,"-",num2,"is",num1-num2)
elif a==3:
    print("Multiplication of",num1,"*",num2,"is",num1*num2)
elif a==4:
    print("Division of",num1,"/",num2,"is",num1/num2)
elif a==5:
    print("Floor division of",num1,"//",num2,"is",num1//num2)
elif a==6:
    print("exponentof",num1,"**",num2,"is",num1**num2)
else:
    print("invalid operation")
'''

'''a=int(input("entyer num1: "))
b=int(input("entyer num2: "))
c=int(input("entyer num3: "))
if a>b and a>c:
    print(a,"is the largest number")
elif b>a and b>c:
    print("b is thge greatest number")
else:
    print("c is the greatest number")
'''

'''n=int(input("enter the day number: "))
if n==1:
    print("monday")
elif n==2:
    print("tuesday")
elif n==3:
    print("wed")
elif n==4:
    print("thrusday")
elif n==5:
    print("fri")
elif n==6:
    print("sat")
elif n==7:
    print("sun")
else:
    print("invalid")
'''

'''n=int(input("enter a number"))
if n%2==0:
    print("it is even")
else:
    print("it is odd")'''
    
'''i=1
while i<=10:
    print(i,end=' ')
    i=i+1'''
    
'''i=0
sum=0
while i<10:
    print(i)
    sum=sum+i
    i=i+1
avg = sum/10
print("the sum is ",sum)
print("the average is",avg)
'''

'''n=int(input("enter the number: "))
for i in range(1,n):
    print(i)
    '''

'''sum=0    
n=int(input("enter num: "))
for i in range(n):
    print(i)
    sum=sum+i
avg=sum/n
print("the sum is",sum)
print("the avg is",avg)
'''

'''n=int(input("enter the number for table: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    '''
    
 
'''def linear_search(list1,n):
    for i in range (len(list1)):
        if list1[i]==n:
            print("value found at position",i+1)
            break
    else:
        print("value not found")


list1=[1,2,3,4,5,6,7,8,9]
n=int(input("enter the element to find: "))
linear_search(list1,n)
'''

'''pos=-1
def binary_search(list1,n):
    l=0
    u=len(list1)-1
    
    while l<=u:
        mid = (l+u)//2
        if list1[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else: 
                u=mid+1
            
    return False
            
list1=[1,21,36,4,78,54,3,2,44]
n=4
if binary_search(list1,n):
    print("found at position",pos+1)
else:
    print("not found")
'''


'''def sort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
list1=[1,4,6,2,8,3,7]
sort(list1)
print(list1)
'''

'''import pandas as pd
list1={'name':['hello','pp'],'age':[76,98]}
arr1=pd.DataFrame(list1)
print(arr1)'''

'''class flowershop:
    def __init__(self,name,color,freshness,quality):
        self.name=name
        self.color=color
        self.freshness=freshness
        self.quality=quality
        
    def display(self):
        print("The name of the flower is: ",self.name)
        print("The color of the flower is: ",self.color)
        print("The freshness of the flower is: ",self.freshness)
        print("The quality of the flower is: ",self.quality)
        
f1=flowershop("rose","black","very fresh",9)
f2=flowershop("lotus","white","very fresh",10)
f3=flowershop("lavender","blue","frail",8)
f1.display()
f2.display()
f3.display()
'''

'''class father:
    def show1(self):
        print("this is my father")

class child(father): #single level inheritence
    def show2(self):
        print("this is me")

class grandchild(child):#multilevel inheritence

class grandchild(father,child): #multiple inheritence
    def show3(self):
        print("this is my child")

a1=father()
a2=child()
a3=grandchild()

a3.show1()
'''

'''class encapsulation:
    __x=10#here by adding the double underscore i have created a private
                        #instance variable which cannot be accessed outside the class 
    def display(self):
        print("welcome")
        print(e1.__x)#but i can access the private instance variable inside the class
e1=encapsulation()
e1.display()      
'''

#polymorphism OVERLOADING
'''class methodoverload: # this isan example of method overloadingwhere the same method 
    def add(self,a=None,b=None): # with different arguments is performing differently
        print(a,b)

a1=methodoverload()
a1.add()
a1.add(1,4)
'''

'''#method overriding
class a:
    def show(self):
        print("fly")
    
class b(a):
    def show(self):
        print("fly bird")

b1=b()
b1.show()'''

#python try and except

'''x=int(input("enter the num1: "))
y=int(input("enter the num1: "))
l=[1,2,3,4,5,6]
try:
    print(x/y)
    print(l[3])
    print(x+l)
    print("ooo"+"oi"+99)
except ZeroDivisionError:
    print("zerodiv error was handled")
except IndexError:
    print("index error was handled")
except Exception as e:
    print("error was handled")
else:
    print("no error found")
finally:
    print("all errors soved moving next")
   '''
   
'''class myerror(Exception):
    pass

marks=int(input("enter the marks:"))
try:
    if marks<0 or marks>100:
        raise myerror
except myerror:
    print("error handled") '''
    

'''def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the num"))
fact=factorial(n)
print("the factorial of",n,"is",fact)
'''

'''n=int(input("enter the num"))
sum=0
for i in range(1,n+1):
    square=i**2
    print("the square of", i ,"is", square) 
    sum=sum+square
print("the value of sum is",sum)
'''
    
'''n=int(input("entyer a number: "))
for i in range(2,n):
    if n%i==0:
        print(n,"is not prime")
        break
else:
    print(n,"is prime")
'''
'''n=int(input("entyer a number: "))
a=2
count = 0
while a<=n:
    if n%a==0:
        count=count+1
    a=a+1
    
if count==1:
    print("prime")
else:print("no")
   '''
   
'''n=int(input("enter till you want series: "))
a=0
b=1
print(a)
print(b)
i=2
while i<n:
    next=a+b
    print(next)
    a=b
    b=next
    i=i+1  
'''

'''n=int(input("enter the number"))
x=n
rev=0
while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
if rev==n:
    print("palindome")
else:print("no")
'''

n=int(input("enter the number"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
    if sum==temp:
        print("strong number")
    else:print("no")
