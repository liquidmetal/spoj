l="TDLF"
x=10
while x>0:
    i=raw_input()
    c=0
    for s in l:
        c+=i.count(s)
    print(2**c)
    x-=1