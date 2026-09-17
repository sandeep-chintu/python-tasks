num=int(input("Enter a number:"))
if num%2==0:
    print("even")
else:
    print("odd")
print("======================================================")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print("the largest number is = ",a)
elif b>=a and b>=c:
    print("the largest number is = ",b)
else:
    print("the largest number is = ",c)
print("=====================================================")


str=input("enter a name:")
rev=str[::-1]
if str==rev:
    print("plaindrome")
else:
    print("not a plaindrome")
print("====================================================")

str="sandeep is a good boy"
vowels_count=0
vowels="aeiouAEIOU"
res=' '
for i in str:
    if i in vowels:
        res += i
        vowels_count=vowels_count+1
print("vowels are:",res,"\n" "vowels_count are :",vowels_count)

print("===========================================================")

list1=[1,2,3,4,5,6,7,89]
list2=sum(list1)
print("sum of all numbers in a list are : ",list2)
print("===========================================================")

# Program to print Fibonacci series up to N terms

n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("=============================================================")

name="my name is sandeep"
words = name.split()
reverse_words=words[::-1]
result=" ".join(reverse_words)
print(result)
print("=============================================================")

num=int(input("enter the number:"))
fact=1
i=1
if num<0:
    print("not defined")
else:
    while i<=num:
        fact*=i
        i += 1
    print(fact)


