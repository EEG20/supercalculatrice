import math

calculatrice = int(input("""quelle est le calcul que tu veut faire ?
1) savoir si un nombre est un nombre premier :
2) utilisé le théorème de pytgagore :
"""))
if calculatrice == 1 :
    a = int(input("entre un nombre: "))
    b = [2,3,4]
    for i in range(a+1) :
        b.append(b[-1]+1)
        C = a/b[i]+0.01
        y = int(C)+0.01
        if y == C and b[i] != a :
            print("c'est pas un nombre premier")
            exit()

    print("c'est un nombre premier")
if calculatrice == 2 :
    hypoténuse = float(input("entre l'hypoténuse :" ))
    adjacent = float(input("entre le coté adjacent :"))
    opposé = float(input("entre le coté opposé :"))
    if hypoténuse == 0:
        print(f"l'hypoténuse sera de {math.sqrt(opposé^2+adjacent^2)}cm ")
