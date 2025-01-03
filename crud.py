from model import baza_danych, Ksiazka, Autor, Gatunek, Dzial
from sqlalchemy.orm import Session
from sqlalchemy.orm import aliased

def create_autor(session):
    imiein = input("Podaj imie autora: ")
    nazwiskoin = input("Podaj naziwsko autora: ")
    autor = Autor(imie = imiein, nazwisko = nazwiskoin)
    session.add(autor)
    session.commit()

def create_gatunek(session):
    nazwagatin = input("Podaj nazwe gatunku: ")
    gatunek = Gatunek(nazwa_gatunku = nazwagatin)
    session.add(gatunek)
    session.commit()

def create_dzial(session):
    nriden = input("Podaj numer identyfikacyjny dzialu: ")
    dzial = Dzial(numer_identyfikacyjny_dzialu = nriden)
    session.add(dzial)
    session.commit()

def read_autor(session):
    autor = session.query(Autor).all()
    for i in autor:
        print(f"ID autora: {i.a_id}, imie autora: {i.imie}, nazwisko autora: {i.nazwisko}")

def read_gatunek(session):
    gatunek = session.query(Gatunek).all()
    for i in gatunek:
        print(f"ID gatunku: {i.g_id}, nazwa gatunku: {i.nazwa_gatunku}")

def read_dzial(session):
    dzial = session.query(Dzial).all()
    for i in dzial:
        print(f"ID dzialu: {i.d_id}, numer identyfikacyjny dzialu: {i.numer_identyfikacyjny_dzialu}")

def update_autor(session):
    id_autora= int(input("Podaj ID autora do edycji: "))
    autor_e = session.query(Autor).get(id_autora)

    if autor_e:
        imie_e = input("Podaj nowe imie autora: ")
        nazwisko_e = input("Podaj nowe naziwkso autora: ")
        autor_e.imie = imie_e
        autor_e.nazwisko = nazwisko_e
        session.commit()
        print("Operacja UPDATE wykonana")
    else:
        print("Brak autora o podany ID")

def update_gatunek(session):
    id_gatunku= int(input("Podaj ID gatunku do edycji: "))
    gatunek_e = session.query(Gatunek).get(id_gatunku)

    if gatunek_e:
        nazwa_gatunku_e = input("Podaj nowa nazwe dla wybranego gatunku: ")
        gatunek_e.nazwa_gatunku = nazwa_gatunku_e
        session.commit()
        print("Operacja UPDATE wykonana")
    else:
        print("Brak gatunku o podanym ID")

def update_dzial(session):
    id_dzialu = int(input("Podaj ID dzialu do edycji: "))
    dzial_e = session.query(Dzial).get(id_dzialu)

    if dzial_e:
        nr_e = input("Podaj nowy numer identyfikacyjny dzialu: ")
        dzial_e.numer_identyfikacyjny_dzialu = nr_e
        session.commit()
        print("Operacja UPDATE wykonana")
    else:
        print("Brak dzialu o podanym ID")

def delete_autor(session):
    id_autor_u = int(input("Podaj ID autora do usuniecia: "))
    autor_u = session.query(Autor).get(id_autor_u)

    if autor_u:
        session.delete(autor_u)
        session.commit()
        print("Operacja DELETE wykonana")
    else:
        print("Nie znaleziono autora o podanym ID")

def delete_gatunek(session):
    id_gatunek_u = int(input("Podaj ID gatunku do usuniecia: "))
    gatunek_u = session.query(Gatunek).get(id_gatunek_u)

    if gatunek_u:
        session.delete(gatunek_u)
        session.commit()
        print("Operacja DELETE wykonana")
    else:
        print("Nie znaleziono gatunku o podanym ID")

def delete_dzial(session):
    id_dzial_u = int(input("Podaj ID dzialu do usuniecia: "))
    dzial_u = session.query(Dzial).get(id_dzial_u)

    if dzial_u:
        session.delete(dzial_u)
        session.commit()
        print("Operacja DELETE wykonana")
    else:
        print("Nie znaleziono dzialu o podanym ID")


def create_ksiazka(session):
    tytulin = input("Podaj tytul nowej ksiazki: ")
    print("Dostepni autorzy do wyboru: ")
    read_autor(session)
    wybor = int(input("Podaj numer ID autora dla nowej ksiazki: "))
    autor_in = session.query(Autor).get(wybor)
    while not autor_in:
        print("Nie ma autora o podanym ID, dodaj nowego autora")
        create_autor(session)
        print("Dostepni autorzy do wyboru: ")
        read_autor(session)
        wybor = int(input("Podaj numer ID autora dla nowej ksiazki"))
        autor_in = session.query(Autor).get(wybor)
    
    print("Dostepne gatunki do wyboru: ")
    read_gatunek(session)
    wybor_g = int(input("Podaj numer ID gatunku dla nowej ksiazki: "))
    gatunek_in = session.query(Gatunek).get(wybor_g)
    while not gatunek_in:
        print("Nie ma gatunku o podanym ID, dodaj nowy gatunek")
        create_gatunek(session)
        print("Dostepne gatunki do wyboru: ")
        read_gatunek(session)
        wybor_g = int(input("Podaj numer ID gatunku dla nowej ksiazki: "))
        gatunek_in = session.query(Gatunek).get(wybor_g)

    print("Dostepne dzialy do wyboru: ")
    read_dzial(session)
    wybor_d = int(input("Podaj numer ID dzialu dla nowej ksiazki: "))
    dzial_in = session.query(Dzial).get(wybor_d)
    while not dzial_in:
        print("Nie ma dzialu o podanym ID, dodaj nowy dzial: ")
        create_dzial(session)
        print("Dostepne dzialy do wyboru: ")
        read_dzial(session)
        wybor_d = int(input("Podaj numer ID dzialu dla nowej ksiazki: "))
        dzial_in = session.query(Dzial).get(wybor_d)
    
    ksiazka_in = Ksiazka(tytul = tytulin, autor_id = autor_in.a_id, gatunek_id = gatunek_in.g_id, dzial_id = dzial_in.d_id)
    session.add(ksiazka_in)
    session.commit()


def read_ksiazka(session):
    ksiazki = session.query(Ksiazka).all()
    for i in ksiazki:
        print(f"ID ksiazki: {i.id if i.id is not None else "NULL"}, tytul ksiazki: {i.tytul if i.tytul is not None else "NULL"}\nID autora: {i.autor_id if i.autor_id is not None else "NULL"}\nID gatunku: {i.gatunek_id if i.gatunek_id is not None else "NULL"}\nID dzialu: {i.dzial_id if i.dzial_id is not None else "NULL"}\n")
        if i.autor_id is not None:
            print(f"Imie autora: {i.autor.imie}, Nazwisko autora: {i.autor.nazwisko}")
        if i.gatunek_id is not None:
            print(f"Nazwa gatunku: {i.gatunek.nazwa_gatunku}")
        if i.dzial_id is not None:
            print(f"Numer identyfikacyjny dzialu: {i.dzial.numer_identyfikacyjny_dzialu}\n\n")
        


def update_ksiazka(session):
    id_ksiazki = int(input("Podaj ID ksiazki do edycji: "))
    ksiazka_e = session.query(Ksiazka).get(id_ksiazki)

    if ksiazka_e:
        tytul_e = input("Podaj nowy tytul ksiazki: ")

        read_autor(session)
        autor_e = int(input("Podaj nowe ID dla nowego autora ksiazki: "))
        autorob = session.query(Autor).get(autor_e)
        while not autorob:
            autor_e = int(input("Podano bledne ID, podaj ID jeszcze raz: "))
            autorob = session.query(Autor).get(autor_e)
        
        read_gatunek(session)
        gatunek_e = int(input("Podaj nowe ID dla nowego gatunku ksiazki: "))
        gatunekob = session.query(Gatunek).get(gatunek_e)
        while not gatunekob:
            gatunek_e = int(input("Podano bledne ID, podaj ID jeszcze raz: "))
            gatunekob = session.query(Gatunek).get(gatunek_e)
        
        read_dzial(session)
        dzial_e = int(input("Podaj nowe ID dla nowego dzialu ksiazki: "))
        dzialob = session.query(Dzial).get(dzial_e)
        while not dzialob:
            dzial_e = int(input("Podano bledne ID, podaj ID jeszcze raz: "))
            dzialob = session.query(Dzial).get(dzial_e)

        ksiazka_e.tytul = tytul_e
        ksiazka_e.autor_id = autor_e
        ksiazka_e.gatunek_id = gatunek_e
        ksiazka_e.dzial_id = dzial_e
        session.commit()
        print("Operacja UPDATE wykonana")
        
    else:
        print("Brak ksiazki o podanym ID")


def delete_ksiazka(session):
    id_ksiazka_u = int(input("Podaj ID ksiazki do usuniecia: "))
    ksiazka_u = session.query(Ksiazka).get(id_ksiazka_u)

    if ksiazka_u:
        session.delete(ksiazka_u)
        session.commit()
        print("Operacja DELETE wykonana")
    else:
        print("Nie znaleziono ksiazki o podanym ID")

def inner_join(session):
    wybierz = int(input("INNER JOIN miedzy tabelami Ksiazka i: \n1.Autor\n2.Gatunek\n3.Dzial\n"))
    if wybierz == 1:
        innerjoin = session.query(Ksiazka, Autor).join(Autor, Ksiazka.autor_id == Autor.a_id).all()

        for i, j in innerjoin:
            print(f"{i.tytul}, {j.imie} {j.nazwisko}")
    
    elif wybierz == 2:
        innerjoin = session.query(Ksiazka, Gatunek).join(Gatunek, Ksiazka.gatunek_id == Gatunek.g_id).all()

        for i,j in innerjoin:
            print(f"{i.tytul}, {j.nazwa_gatunku}")

    elif wybierz == 3:
        innerjoin = session.query(Ksiazka, Dzial).join(Dzial, Ksiazka.dzial_id == Dzial.d_id).all()

        for i, j in innerjoin:
            print(f"{i.tytul}, {j.numer_identyfikacyjny_dzialu}")

def left_join(session):
    wybierz = int(input("LEFT JOIN miedzy tabelami Ksiazka i: \n1.Autor\n2.Gatunek\n3.Dzial\n"))
    if wybierz == 1:
        leftjoin = session.query(Ksiazka, Autor).outerjoin(Autor, Ksiazka.autor_id == Autor.a_id).all()

        for i, j in leftjoin:
            if j:
                print(f"{i.tytul}, {j.imie} {j.nazwisko}")
            else:
                print(f"{i.tytul}, brak autora")
    elif wybierz == 2:
        leftjoin = session.query(Ksiazka, Gatunek).outerjoin(Gatunek, Ksiazka.gatunek_id == Gatunek.g_id).all()

        for i, j in leftjoin:
            if j:
                print(f"{i.tytul}, {j.nazwa_gatunku}")
            else:
                print(f"{i.tytul}, brak gatunku")
    elif wybierz == 3:
        leftjoin = session.query(Ksiazka, Dzial).outerjoin(Dzial, Ksiazka.dzial_id == Dzial.d_id).all()

        for i, j in leftjoin:
            if j:
                print(f"{i.tytul}, {j.numer_identyfikacyjny_dzialu}")
            else:
                print(f"{i.tytul}, brak numeru dzialu")

    
        

        
    

