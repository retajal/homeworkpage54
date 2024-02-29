a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))

def qudratic (a , b , c):
    d = b** - 4*a*c
    if d > 0:
        if d == 0:
            if d < 0:
                print("jjjjj")
            else:
                print("no slotion")
        else:
            b3 = (-b / 2*a)
            print("1 sloution")
            print (b3)
    else:
        b1 = (-b + b ** 2 - 4 * a * c)
        b2 = (-b - b ** 2 - 4 * a * c)
        print("2 sloution")
        print (b1, b2)


print(qudratic(a , b , c))
quit()

