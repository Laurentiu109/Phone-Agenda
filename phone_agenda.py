print (" " * 15, "AGENDA TELEFON")

def repeat_operation(k):
    if n == 1:
        print("1. Adauga alt numar: ")
    if n == 2:
        print("2. Cauta alt numar: ")
    if n == 3:
        print("3. Sterge alt numar: ")
    print("0. Pentru revenire la meniul principal.")
    return int(input("Alege optiunea:"))


def display_menu():

    print("1. Adauga numarul de telefon in agenda telefonului")
    print("2. Cauta numarul de telefon din agenda telefonului")
    print("3. Sterge numarul de telefon din agenda telefonului")
    print("0. Iesire din meniu.")
    

d1 = {}
display_menu()
n = int(input("Selectati optiunea: "))
while True:
    while n == 1:
        name=input("Introduceti numele:")
        numar=input("introduceti numarul de telefon:")
        varsta=int(input("Intorduceti varsta:"))
        d1[name]=[numar, varsta]
        n = repeat_operation(n)
    

    while n==2:
        name1=input("Introduceti numele pe care vrei sa il cauti in agenda telefonului: ")
        if name1 in d1.keys():
             print("Numarul de telefon" , name1 , "este", d1[name1][0])
        else:
            print("Numarul nu exista in agenda telefonului!")
        n = repeat_operation(n)
    while n==3:
        name1=input("Introduceti numele contactului pe care vrei sa il stergi din agenda: ")
        if name1 in d1.keys():
            del d1[name1]
            print("Numarul a fost sters!")
        else:
            print("Numarul nu exista in agenda telefonului!")
        n = repeat_operation(n)
    display_menu()
    n = int(input("Selectati optiunea: "))
        
    if n==0:
        break
