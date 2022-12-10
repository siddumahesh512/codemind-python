n=int(input())
sq=n**2
sum=0
while sq>0:
    d=sq%10
    sum=sum+d
    sq=sq//10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')
    