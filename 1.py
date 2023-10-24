# menu program to add,multiply,etc. two and three integers

p=int(input("enter no:"))
l=int(input("enter no:"))
o=int(input("enter no:"))

ch="y"
while ch=="y" or ch== "y":
    print("--------------menu-------------")
    print("1.add ")
    print("2.subtract ")
    print("3.multply")
    print("4.divide")
    print("5.exit")
    print("-------------------------------")
    x=int(input("enter choice:"))
    if x==1:
        print("-------------------------------")
        print("1.add two ")
        print("2.add three ")
        print("-------------------------------")
        m=int(input("enter choice:"))
        if m==1:
             print("-------------------------------")
             print("1.add first and second")
             print("2.add third and second ")
             print("3.add first and third")
             print("-------------------------------")
             n=int(input("enter choice:"))
             if n==1:
                  a=p+l
                  print("the summ  of first and secondno. is:",a) 
             if n==2:
                 a=l+o
                 print("the summ  of third and second no. is:",a)
             if n==3:
                 a=p+o
                 print("the summ  of first and third no. is:",a)
        elif m==2:
            a=p+l+o
            print("the summ  of three no. is:",a)
    if x==5:
       break
       
        
