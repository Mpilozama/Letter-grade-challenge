def letter_grade(mark:int) -> str:
    A=[]
    B=[]
    C =[]
    D=[]
    F=[]

    for i in range(80,101):
        A.append(i)

    for i in range(70,80):
        B.append(i)

    for i in range(60,70):
        C.append(i)

    for i in range(50,60):
        D.append(i)

    for i in range(0,50):
        F.append(i)

    if mark in A:
        return 'A'
    elif mark in B:
        return 'B'
    elif mark in C:
        return 'C'
    elif mark in D:
        return 'D'
    else:
        return 'F'