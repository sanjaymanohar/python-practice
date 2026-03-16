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


