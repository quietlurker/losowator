from tkinter import *
import csv
from random import *

#---------------------------------------
# glowna funkcja losujaca karty
#---------------------------------------
def losowanie():

    # w przestrzeni funkcji losowanie bedziemy uzywac globalnej zmiennej numer_losowania.
    # musimy pythonowi powiedziec, ze zmienna numer_losowania, ktora bedziemy sie poslugiwac jest globalna, zeby jej nie tworzyl podczas kazdorazowego wywolania funkcji
    # potem juz mozemy spokojnie uzywac numer_losowania - python bedzie wiedzial, ze to zmienna globalna
    global numer_losowania
   
    #wyczysc liste kart
    #checkboxy dodaja, nie usuwaja
    #odznaczenie checkbosa nie usuwa kart z list
    del karty_nazwy[:]

    #set zmiennych wykorzystanych w petli do drukowania wynikow
    licznik = 1
    i = 0
    
    #sprawdz checkboxy
    if c1_var.get() == 1:
        dodaj_do_listy("Karty_dmonion_podstawka.csv")
        c1_check  = 1
    else:
        c1_check  = 0
        
    if c2_var.get() == 1:
        dodaj_do_listy("Karty_dmonion_intryga.csv")
        c2_check  = 1
    else:
        c2_check  = 0


    #sprawdz, czy jakies pakiety kart sa wybrane
    if c1_check == 0 and c2_check == 0:


        #set new mark to index END (last position in the text box)
        T.mark_set(my_mark,END)
        T.insert(my_mark, "Czyżby czyżby Manfredzie?\n")
        T.insert(my_mark, "Out of cheese error\n")
        T.insert(my_mark, "--------------------------------------\n")
        #focus okna na ostatniej linijce (ale nie focus kursora)
        T.see(END)
        return

    #losuj karty
    losuj_10_kart = sample(karty_nazwy, 10)

    #wyswietl wynik losowania
    #INSERT to mark - aktualna pozycja kursora - jesli ktos kliknie w okienko, to kursor sie przestawi i kolejne linijki nie beda wrzucane na koncu, tylko tam, gdzie jest kursor
    #jesli ustawimy insert na koncu, to kolejne linijki sa wrzudane na koncu
    T.mark_set(INSERT,END)
    #czemu to nie dziala w jednej linijce T.insert(INSERT, "Wylosowane karty (", numer_losowania, ")\n")
    T.insert(INSERT, "Wylosowane karty (")
    T.insert(INSERT, numer_losowania)
    T.insert(INSERT, ")\n")
    
    T.insert(INSERT, "--------------------------------------")
    T.insert(INSERT, "\n")

    while licznik <=10:
        T.insert(INSERT, losuj_10_kart[i], "\n")
        T.insert(INSERT, "\n")

        i+=1
        licznik+=1
    
    T.insert(INSERT, "--------------------------------------")
    T.insert(INSERT, "\n")
    #focus okna na ostatniej linijce (ale nie focus kursora)
    T.see(END)

    # przed wyjsciem z funkcji zwiekszymy wartosc numer_losowania o jeden
    numer_losowania +=1
    
def dodaj_do_listy(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        reader = csv.reader(f,delimiter=';')
        rownb = 0
        #skip header
        for row in reader:
            if rownb > 0 :
                karty_nazwy.append(row[0])
            rownb = rownb + 1

#---------------------------------------
# zamkniecie programu
#---------------------------------------
    
def koniec ():
    glowne_okno.destroy()

#---------------------------------------
# TEST STUFF
#---------------------------------------
def display():
    print (c1_var.get())


#---------------------------------------
# START
#---------------------------------------

#---------------------------------------        
#GUI
#---------------------------------------
#wywolanie
glowne_okno = Tk()
glowne_okno.wm_title("Wielki losowator kart")

#--------------------------------------
#definicje zmiennych

c1_var = IntVar()
c2_var = IntVar()

karty_nazwy = []

#define new mark
my_mark = StringVar()

# numer_losowania pozwala latwiej zorientowac sie, ktore losowanie z okan wynikow jest najnowsze
# jest to zmienna globalna, ktora jest potem zwiekszana przy kazdorazowym wykonaniu funkcji losowanie
numer_losowania = 0


#--------------------------------------

#display()

c1 = Checkbutton(glowne_okno, text = "podstawka", variable = c1_var)
#wlacz przycisk
c1.select()
c1.pack()

c2 = Checkbutton(glowne_okno, text = "intryga", variable = c2_var)
c2.pack()

#Przycisk do losowania
start_b = Button(glowne_okno, text="Dalej Dalej Programiku Gadgeta!", command=losowanie)
start_b.pack()

#tworzy obiekt scrollbar, ale nie laczy go z niczym
scrollbar = Scrollbar(glowne_okno)
scrollbar.pack( side = RIGHT, fill=Y )

#tworzy obiek okienka tekstowego i podlacza go do scrollbara
#dzieki temu scrollbar rusza sie za kazdym razem, jak okno sie zmienia
#(ale okienko sie nie rusza, jak ruszamy scrollbar - do tego trzeba zmodyfikowac obiekt scrollbar)
T = Text(glowne_okno, yscrollcommand = scrollbar.set)
T.pack()

#a dzieki temu okienko sie rusza, jak ruszamy scrollbarem
#scrollbar i okno tekstowe do dwa osobne obiekty
#wiec trzeba podlaczyc scrollbar do okna i osobno okno do scrollbara
scrollbar.config( command = T.yview )

#Przycisk do konczenia programu
stop_b = Button(glowne_okno, text="Shutting down...", command=koniec)
stop_b.pack()

mainloop()
