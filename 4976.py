
for i in range(1, 40):
    for j in range(1, 40):
        for k in range(1, 40):
            a='0'+'1'*i+'2'*j+'3'*k+'0'
            b=a
            while not '00' in b:
                b=b.replace('01','210',1)
                b=b.replace('02','3101',1)
                b=b.replace('03','2012',1)
            if b.count('1')==111 and b.count('2')==101 and b.count('3')==35:
                print(len(a))
                exit(0)