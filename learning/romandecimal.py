I=1
V=5
X=10
L=50
C=100
D=500
M=1000
s = input()
for i in range(0,len(s)-1):
    if s[i]>=s[i+1]:
        b = s[i]+s[i+1]
    else:
        b = s[i+1]-s[i]
print(b)


