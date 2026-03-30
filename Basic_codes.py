#1Q. Factorial  of a number

Number=int(input("Enter a number: "))
fact=1

for i in range (1,Number+1):
    fact=fact*i
print("factorial of given number is :",fact)

#2Q. simple intrest
P,T,R=map(int, input().split())
SI=(P*T*R)/100
print(SI)

# # 3Q. compound intrest
P,T,R=map(int, input().split())
A=P*(1+R/100)**T
CI=A-P
print(round(CI,2))#to get 2 decimal only


# 4Q. amstrong no
number=int(input())
n=number
length=len(str(number))
total=0
while number>0:
    digit=number%10
    total=total+(digit**length)
    number=number//10

if total==n:
    print("true")
else :
    print("false")


# 5Q. Area of a circle
radius=int(input())
area=3.14*(radius**2)
print(area)

#6Q. prime numbers
number=int(input())
count=0

for i in range(2,number):
    print(i)
    if i % number ==0:
        count+=1
       
if count>0:
    print("not prime")
else:
    print("prime")    

# 7Q. Prime number in range
start,end=map(int,input().split(","))
b=[]
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            b.append(i)    
print(b)            

# 8Q. fibonacci
number=int(input())
n=int(input("n th multiple"))

a=0
fib_number=1
for i in range(number):
    a,fib_number=fib_number,a+fib_number
    print(a,end=" ")
print(a,"last")   
 
# .1 to check given no is fib or not
number=int(input())
a,b=0,1
for i in range(number+1):
    if a==number:
        print("yes")
        break
    a,b=b,a+b
    print(a,b)
else:
    print("no")

# Nth multiple of a number(divisor) in Fibonacci Series 
a,b=0,1
n_th_multiple=4
divisor=3
count=0
while True:
    a,b=b,a+b
    if b%divisor==0:
        count+=1
        if count==n_th_multiple:
            print(b) 
            break       

# ASCII Value
a='g'
print(ord(a))

# 9Q. Sum of list
a=list(map(int, input().split(",")))
b=0
for i in a[0:]:# else for i in a:
    b+=i
print(b)#just sum(a)  will find sum

# 10Q. max in list
a=list(map(int,input().split(" ")))
b=a[0]
for i in a:
    if  i>b:
        b=i
print(b)

# 11Q. Rotate the list
a=list(map(int,input().split(",")))
r=3
b=a[r:]+a[0:r]
print(b)

# 12Q. Split the Array and Add First Part to the End
a=list(map(int,input().split(",")))
k=2
b=a[k:]
c=b+a[0:k]
print(c)
# 13Q. reminder of array multiplication divided by n
a=[2,4,5,6]
b=1
n=7
for i in a:
    b=b*i
d=b% n
print(d)   

# 13Q. sum of even and odd digits
a=232211
b=str(a)
c=0
d=0
for i in b:
    if int(i)%2==0:
        c+=int(i)
    else:
        d+=int(i)

print(c,d)

# 14.Q reverse number
a=1239876
b=str(a)
c=b[::-1]
print(int(c))

14Q. perfect number 

a=280
b=0
for i in range(1,a):
    if a % i==0:
        b=b+i
if a==b:
    print("perfect")
else:
    print("not")

# Q15. move 0s  to last
a=[12,0,8,9,0,6,8]
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
d=b+c
print(d)


# Q.16 frequency of number
a=[12,0,8,9,0,6,8]
f={}
for i in a:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)  

# Q.17 anagram
a="sanjay"
b="yajnaS"
a=a.lower()
b=b.lower()
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not")