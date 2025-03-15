# Ogólne informacje
Projekt realizuje prostą implementację aplikacji CRUD (Create, Read, Update, Delete), która służy do zarządzania 
potencjalną bazą danych biblioteki (baza danych w przypadku tego projektu zawiera informacje o dostępnych 
ksiązkach tj. tytuły, autorów, gatunki literackie oraz działy. Aplikacja zawiera funkcjonalności dodwania nowych 
książek, wyświetlania rekordów (zapisanych, dostępnych książek), edcyję infomacji o książkach oraz usuwanie 
książek. Możliwe jest wykonywanie operacji INNER JOIN oraz LEFT JOIN między tabelami. Dane w przypadku tej 
aplikacji przechowywane są w bazie PostgreSQL, do mapowania (ORM) służy rozszerzenie SQLAlchemy. Do obsługi bazy 
wykorzystywane jest utworzone menu konsolowe.

# Technologie
W kodzie użyto:
* Python 3.12
* SQLAlchemy 1.4
* PostgresSQL
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku Visual Studio Code na systemie Windows. Struktura projektu składa 
się z plików `model.py`, `crud.py` oraz `main.py`. Pierwsyz plik zawiera definicję tabel bazodanowych 
i zawartych między nimi relacji, drugi skupia się na logice operacji na bazie danych tj. operacji CRUD oraz JOIN 
oraz zabezpieczenia przed błędami. Plik trzeci skupia się na organizacji działania całego progrmu, wraz 
z implementacją interfejsu konsolowego. W apliakcji dane wprowdzane, są wprowadzane interaktywnie przez 
użytkownika. Do prawidłowego działania programu wymagana jest lokalna instalacja PostgreSQL oraz konfiguracja 
parametrów połączenia. SQLAlchemy automatycznie tworzy odpowiednie tabele w bazie danych po uruchomieniu programu.

# General Information  
The project implements a simple CRUD (Create, Read, Update, Delete) application for managing a potential 
library database (the database in this project contains information about available books, such as titles, 
authors, literary genres, and sections). The application includes functionalities for adding new books, 
displaying records (saved, available books), editing book information, and deleting books. It is possible to 
perform INNER JOIN and LEFT JOIN operations between tables. Data for this application is stored in a PostgreSQL 
database, with the SQLAlchemy extension used for mapping (ORM). A console menu is used to interact with the 
database.  

# Technologies  
The code uses:  
* Python 3.12  
* SQLAlchemy 1.4  
* PostgreSQL  

# Usage  
The code was run and written in the Visual Studio Code environment on a Windows system. The project structure 
consists of the files `model.py`, `crud.py`, and `main.py`. The first file contains the definition of database 
tables and the relationships between them. The second focuses on the logic of database operations, such as CRUD 
and JOIN, as well as error handling. The third file focuses on organizing the entire program's operation, 
including the implementation of the console interface. In the application, data is entered interactively by the 
user. Proper program operation requires a local PostgreSQL installation and configuration of connection 
parameters. SQLAlchemy automatically creates the appropriate tables in the database when the program is launched.

