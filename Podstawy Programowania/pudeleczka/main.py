ile_pudeleczek = int(input())

StringInsideBox = input().split()
insideBox = [int(a) for a in StringInsideBox]

ile_zapytan = int(input())
for i in range(ile_zapytan):
    a, b =input().split()
    print(sum(insideBox[int(a)-1:int(b)]))

