#5 5 4 4 1 5 5 1 4 4 1 1 1 5 4 3 2 1 0
#4+5+4+4+4+1
def NWD(a, b):
    M = a
    m = b
    r = M % m
    while(r!=0):
        M = m
        m = r
        r = M % m
    return m

suma =0
second = 1
stringValues = input().split()
numberValues = [int(a) for a in stringValues]
for values in range(len(numberValues)):
    if numberValues[values] == 1 and values>1:
        suma = suma + NWD(first,second)
    if numberValues[values] == 0:
        print(suma)
    if numberValues[values] >1:
        first = second
        second = numberValues[values]