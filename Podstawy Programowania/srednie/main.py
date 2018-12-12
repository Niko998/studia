#oceny = []
#wartownik = 1
#while(wartownik):
#    x = int(input())
#    if 2<=x<=5:
#        oceny.append(x)
#    elif x == 1:
#        print(round(float(sum(oceny))/float(len(oceny)),2))
#    elif x == 0:
#        for x in oceny:
#            print (x,end=" ")
#        print()
#    elif x == -1:
#        wartownik = 0


stringValues = input().split()
numberValues = [int(a) for a in stringValues]
marks = []
for x in numberValues:
    if 2<=x<=5:
        marks.append(x)
    elif x == 1:
        avg = round(float(sum(marks))/float(len(marks)),2)
        if avg*100%10==0:
            print(str(avg)+'0')
        else:
            print(avg)
    elif x == 0:
        for y in marks:
            print (y,end=" ")
        print()
    elif x == -1:
        break