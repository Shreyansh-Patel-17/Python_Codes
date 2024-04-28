#Code to print pyramid
rows = int(input("Enter the rows: "))

for i in range(0,rows+1):
    for j in range(i):
        print("*",end='')
    print()    

