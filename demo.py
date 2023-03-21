def phitonacci(n):
    if (n%3 == 0) : return n+3;
    if (n%2 != 1) : return n-3;
    return phitonacci(n-1) + phitonacci(n+1);


strings = int(6)
i=6
s=''
while i > 0:
    s+= str(phitonacci(i))
    i-=1

print(s)