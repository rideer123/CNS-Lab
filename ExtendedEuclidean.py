
def findGCD(num1,num2):
    temp1 = num1
    temp2 = num2
    r = 0
    q = 0
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    t = 0
    s = 0
    print("q       r1       r2       r       s1       s2       s       t1       t2       t")
    
    while num2!=0:

        q = int(num1/num2)

        r = num1-num2*q

        s = s1-q*s2

        t = t1-q*t2

        print(q,"     ",num1,"     ",num2,"     ",r,"     ",s1,"     ",s2,"     ",s,"     ",t1,"     ",t2,"     ",t)
        
        num1 = num2
        num2 = r

        s1 = s2
        s2 = s

        t1 = t2
        t2 = t


    print("GCD of ",temp1," and ",temp2," is ",num1)

    if num1==1:
        print("Multiplicative of ",temp2," Z",temp1," is ",t1)
        if t1<0:
            print(" or ",(t1+temp1)%temp1)
        
    else: 
        print("Multiplicative inverse doesn't exist.")
    

if __name__=="__main__":

    Num1 = int(input("Enter First Number: "))

    Num2 = int(input("Enter Second Number: "))

    findGCD(Num1,Num2)
