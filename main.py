from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from crud import create_autor, create_gatunek, create_dzial, read_autor, read_dzial, read_gatunek, update_autor, update_dzial, update_gatunek, delete_autor, delete_dzial, delete_gatunek, create_ksiazka, read_ksiazka, update_ksiazka, delete_ksiazka, inner_join, left_join
from model import baza_danych, Ksiazka, Autor, Gatunek, Dzial

#Zastąpic 'user', 'password', 'localhost', 'db_name' odpowiednimi danymi dostępowymi z Connection String
#Tworzenie silnika bazy danych
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres', echo=True)

#Tworzenie tabel w bazie danych
baza_danych.metadata.create_all(engine)

#Sesja sqlalchemy
session = Session(engine)

while True:
    print("MENU KSIAZKA")
    print("1. Dodaj ksiazke do bazy")
    print("2. Pokaz wszystkie ksiazki zawierajce sie w bazie")
    print("3. Edytuj ksiazke znajdujaca sie w bazie")
    print("4. Usun ksiazke z bazy\n")
    print("MENU AUTOR")
    print("5. Dodaj autora do bazy")
    print("6. Pokaz autorow w bazie")
    print("7. Edytuj dane o autorze w bazie")
    print("8. Usun autora z bazy\n")
    print("MENU GATUNEK")
    print("9. Dodaj gatunek do bazy")
    print("10. Pokaz gatunki w bazie")
    print("11. Edytuj dane o gatunku w bazie")
    print("12. Usun gatunek z bazy\n")
    print("MENU DZIAL")
    print("13. Dodaj dzial do bazy")
    print("14. Pokaz dzialy w bazie")
    print("15. Edytuj dane o dziale w bazie")
    print("16. Usun dzial z bazy\n")
    print("17. INNER JOIN")
    print("18. LEFT JOIN\n")
    print("19. WYJDZ")
    wybor = int(input())

    if(wybor == 1):
        create_ksiazka(session)

    elif(wybor == 2):
        read_ksiazka(session)

    elif(wybor == 3):
        update_ksiazka(session)

    elif(wybor == 4):
        delete_ksiazka(session)

    elif(wybor == 5):
        create_autor(session)
        
    elif(wybor == 6):
        read_autor(session)

    elif(wybor == 7):
        update_autor(session)

    elif(wybor == 8):
        delete_autor(session)

    elif(wybor == 9):
        create_gatunek(session)

    elif(wybor == 10):
        read_gatunek(session)

    elif(wybor == 11):
        update_gatunek(session)

    elif(wybor == 12):
        delete_gatunek(session)

    elif(wybor == 13):
        create_dzial(session)

    elif(wybor == 14):
        read_dzial(session)

    elif(wybor == 15):
        update_dzial(session)

    elif(wybor == 16):
        delete_dzial(session)

    elif(wybor == 17):
        inner_join(session)
    
    elif(wybor == 18):
        left_join(session)
    
    else:
        break
