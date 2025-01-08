print('Bài 1')
x= int(input("x = "))
l=[]
if (-2**23 <= x <= 2**31 - 1): 
    if x<=0:
        print('False')
    else:
        for i in str(x):
            l+=[i]
        if l==l[::-1]:
            print("True")
        else:
            print('False')
else:
    print(0)
print("----------------------------------")


print('Bài 2')
# n = str(input())
n= 'MCMXCIV'
l=[]
s=0
for i in range(0,len(n)):
    if n[i:i+2] == 'CM':
        s+= 900
        l+=[n[i:i+2]]
    elif n[i:i+2] == 'CD':
        s+= 400
        l+=[n[i:i+2]]
    elif n[i:i+2] == 'XC':
        s+= 90
        l+=[n[i:i+2]]
    elif n[i:i+2] == 'XL':
        s+= 40
        l+=[n[i:i+2]]
    elif n[i:i+2] == 'IX':
        s+= 9
        l+=[n[i:i+2]]
    elif n[i:i+2] == 'IV':
        s+= 4  
        l+=[n[i:i+2]]
for i in l:
    if i in n:
        n=n.replace(i,'')
for i in range(0,len(n)):
    if n[i]=='M':
        s+=1000
    elif n[i]=='D':
        s+=500
    elif n[i]=='C':
        s+=100
    elif n[i]=='L':
        s+=50
    elif n[i]=='X':
        s+=10
    elif n[i]=='V':
        s+=5
    elif n[i]=='I':
        s+=1
print(s)
print("----------------------------------")


print('Bài 3')
# n= int(input("n = "))
n = 100
def happynumber(n):
    if n==1:
        return 1
    elif n<10:
        return 0
    else: 
        s=0
        for i in str(n): 
            s+= int(i)**2
        return (happynumber(s))
if happynumber(n)==1:
    print('True')
else:
    print('False')
print("----------------------------------")


print('Bài 4')
def reverseString(s):
    l=[]
    for i in s:
        if i.isalpha()==True:
            l+=[i]
    l.reverse()
    print(l)
# a=str(input("s = "))
a=["h","e","l","l","o"]
reverseString(a)
print("----------------------------------")


print('Bài 5')
l=[]
nums = list(input("nums = "))
for i in nums:
    if i.isnumeric()==True:
        l+=[i]
if int(max(l))==len(l):
    for i in range(0,len(l)+1):
        if str(i) not in l:
            print(i)
            break
else:
    print(0)
print("----------------------------------")

print('Bài 6')
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening 
        self.customer_name =  customer_name
    def guitien(self,sotiengui):
        self.balance = self.balance + sotiengui
        return 1
    def ruttien(self,sotienrut):
        if self.balance >= sotienrut:
            self.balance = self.balance - sotienrut
            return 1
        return 0
    def check_balance(self):
        return self.balance
a = BankAccount(1111111111,100000, '12/3/2023', 'doan')
print(a.guitien(300000))
print(a.ruttien(200000))
print(a.check_balance())
nums=[0,1,3,2,5]
n=len(nums)
nums.sort()
print(nums)
if n!= max(nums):
        print(n)
else: 
    for i in range(0,n):
        if i==nums[i]:
            continue
        else:
            print(i)
            break