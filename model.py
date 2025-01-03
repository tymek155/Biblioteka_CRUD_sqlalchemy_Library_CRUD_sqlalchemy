from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

baza_danych = declarative_base()

class Ksiazka(baza_danych):
    __tablename__= 'Ksiazka'
    id = Column(Integer, primary_key=True)
    tytul = Column(String)
    autor_id = Column(Integer, ForeignKey('Autor.a_id'))
    gatunek_id = Column(Integer, ForeignKey('Gatunek.g_id'))
    dzial_id = Column(Integer, ForeignKey('Dzial.d_id'))

    #Relacje
    autor = relationship('Autor', back_populates='ksiazki')
    gatunek = relationship('Gatunek', back_populates='ksiazki')
    dzial = relationship('Dzial', back_populates='ksiazki')

class Autor(baza_danych):
    __tablename__='Autor'
    a_id = Column(Integer, primary_key=True)
    imie = Column(String)
    nazwisko = Column(String)

    #Relacja
    ksiazki = relationship('Ksiazka', back_populates='autor')

class Gatunek(baza_danych):
    __tablename__='Gatunek'
    g_id = Column(Integer, primary_key=True)
    nazwa_gatunku = Column(String)

    #Relacja
    ksiazki = relationship('Ksiazka', back_populates='gatunek')

class Dzial(baza_danych):
    __tablename__ ='Dzial'
    d_id = Column(Integer, primary_key=True)
    numer_identyfikacyjny_dzialu = Column(String)

    #Relacja
    ksiazki = relationship('Ksiazka', back_populates='dzial')



