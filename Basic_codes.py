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