import tkinter as tk
from math import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from main import *

def odpri_txt():
    datoteka = filedialog.askopenfilename(title="Odpri Datoteko", filetypes=(("Text Files", "*.txt"),)) #odpremo file explorer in zberemo datoteko
    datoteka = open(datoteka, 'r')
    count = 0
    while True:
        count += 1
        #Pridobim vrstico iz datoteke
        vrstica = datoteka.readline()
        if not vrstica:
            break
        if vrstica[-1] == '\n':
            racun = str(vrstica[:-2])
        else:
            racun = str(vrstica[:-1])
        # https://stackoverflow.com/questions/2140614/python-eval-error-suppression
        try:
            rezultat = (round(eval(racun), 4))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            rezultat = "Neresljivo"
        vrstica = str(count) + ". " + racun +" = " +str(rezultat)
        beriDatoteko.insert(END, vrstica + '\n')
    datoteka.close()

calculation = ""
izpis = ""
stevec = 0
def dodaj_v_racun(symbol):
    global calculation
    global izpis
    sqrt = "sqrt"
    global stevec
    dolzina = len(calculation)
    if symbol == "+":
     calculation += symbol 
     izpis = izpis + (" " + symbol + " ") #dam presledke med operacijami, da je lazje berljivo           
    elif symbol =="-":
      izpis = izpis + (" " + symbol + " ")
      calculation += symbol          
    elif symbol == "/":
      izpis = izpis + (" " + symbol + " ") 
      calculation += symbol          
    elif symbol ==  "*":
      izpis = izpis + (" " + symbol + " ") 
      calculation += symbol
    elif symbol == "√" :
      izpis = izpis + (symbol + " ")
      if dolzina == 0:
          pocisti()
          izracun.insert(1.0, "Error")          
      else:    
        calculation = calculation[:(dolzina-3)] + str(sqrt) + calculation[(dolzina-3):] #pred stevilko dodam sqrt 
    elif symbol == "^":
        izpis = izpis + symbol
        calculation = calculation + "**"
    elif symbol == "(":
        izpis = izpis + symbol
        calculation+="("
    elif symbol == ")":
        izpis = izpis + ( symbol + " ")
        calculation+=")" 
    elif symbol == "%":
        izpis = izpis + symbol
        calculation = calculation[:(dolzina-1)] + str("%") + calculation[(dolzina-1):] #pred stevilko 
        stevec=stevec+1       
    else:
        if stevec == 1: 
            izpis = izpis + ( symbol + " ")   
            calculation = calculation[:(dolzina-1)] + symbol + calculation[(dolzina-1):] #dodam znak za % 
            stevec = 0
        elif dolzina == 0:
            izpis = izpis + symbol
            calculation = calculation + ("("+ symbol + ")")
        elif calculation[-1] == ")":
            izpis = izpis + symbol
            calculation = calculation[:(dolzina-1)] + symbol + calculation[(dolzina-1):] #dodam pred oklepaj stevilko    
        else:
            izpis = izpis + symbol   
            calculation = calculation + ("("+ symbol + ")")
    
    print(calculation)
    izracun.delete(1.0, "end")
    izracun.insert('end', izpis, 'tag-right')
    
def dodajSt(symbol):
    global calculation
    global izpis
    # print(calculation)
    izpis += str(symbol)
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert('end', izpis, 'tag-right')    

def izracunaj():
    global calculation
    global izpis
    racun =str(izpis) + " ="
    print("To je pred izracunom: "+ calculation)
    try:
        calculation = str(round(eval(calculation),5))
        izracunano.insert(1.0,racun, 'tag-right')
        izracun.delete(1.0, "end")
        izracun.insert('end', calculation, 'tag-right')
    except:
        pocisti()
        izracun.insert(1.0,"Error")
        
def izracunaj_txt():
    global zracunaj
    global vsebina
    racun = str(beriDatoteko.get(1.0, "end"))

def pocisti():
    global calculation
    global izpis
    calculation = ""
    izpis = ""
    izracun.delete(1.0, "end")
    izracunano.delete(1.0, "end")
    beriDatoteko.delete(1.0, "end")


    
def pocistiLogicnaVrata():
    global calculation
    global izpis
    calculation = ""
    izpis = ""
    text_result.delete(1.0, "end")    

# def odstrani_karakter():
#     global calculation
#     global izpis
#     izpis = izpis[:-1]
#     calculation = calculation[:-1]
#     print(calculation)
#     izracun.delete(1.0, "end")
#     izracun.insert(1.0, izpis)

# 2. & 3. točka

def pretvori(st, baza1, baza2, flag=True):
    for i in str(st):
        if i == "A":
            i = 10
        elif i == "B":
            i = 11
        elif i == "C":
            i = 12
        elif i == "D":
            i = 13
        elif i == "E":
            i = 14
        elif i == "F":
            i = 15
        if int(i) >= baza1:
            text_result.insert(1.0, "Neveljaven vnos")
            return 0
    temp = 0
    k = len(str(st)) - 1
    for i in str(st):
        if i == "A":
            i = 10
        elif i == "B":
            i = 11
        elif i == "C":
            i = 12
        elif i == "D":
            i = 13
        elif i == "E":
            i = 14
        elif i == "F":
            i = 15
        temp += int(i) * baza1**k
        k -= 1
    rez = ""
    deli = 1
    while True: # vir za emulacijo do .. while zanke: https://www.educba.com/do-while-loop-in-python/
        deli = temp // baza2
        ost = temp % baza2
        if ost == 10:
            ost = "A"
        elif ost == 11:
            ost = "B"
        elif ost == 12:
            ost = "C"
        elif ost == 13:
            ost = "D"
        elif ost == 14:
            ost = "E"
        elif ost == 15:
            ost = "F"
        rez += str(ost)
        temp = deli
        if deli == 0:
            break
    rez = rez[::-1]
    if flag:
        text_result.insert(1.0, rez)
    return rez

counter = 0

def pretvorba():
    global counter
    global stev
    global b1
    global b2
    counter += 1
    
    if counter == 1:
        stev = text_result.get(1.0, "end-1c")
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "Iz baze: ")
    elif counter == 2:
        b1 = int(str(text_result.get(1.0, "end-1c")).split(" ")[2]) # sketchy...
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "V bazo: ")
        # preberi vnos in ga shrani v globalno spremenljivko
        # string split: https://stackoverflow.com/questions/44384854/split-string-into-array-in-python
    elif counter == 3:
        counter = 0
        b2 = int(str(text_result.get(1.0, "end-1c")).split(" ")[2]) # sketchy...
        text_result.delete(1.0, "end")
        pretvori(stev, b1, b2)

def l_and(tmp1, tmp2):
    rez = ""
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    for i in range(len(tmp1)):
        rez += str(int(tmp1[i]) and int(tmp2[i]))
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)
    return rez

def l_or(tmp1, tmp2):
    rez = ""
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    for i in range(len(tmp1)):
        rez += str(int(tmp1[i]) or int(tmp2[i]))
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)
    return rez

def l_xor(tmp1, tmp2):
    rez = ""
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    for i in range(len(tmp1)):
        rez += str((int(not int(tmp1[i])) and int(tmp2[i])) or (int(tmp1[i]) and int(not int(tmp2[i]))))
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)
    return rez

def l_nor(tmp1, tmp2):
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    rez = ""
    vmes = l_or(tmp1, tmp2)
    for i in vmes:
        if i == "1":
            rez += "0"
        else:
            rez += "1"
    text_result.delete(1.0, "end")
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)

def l_nand(tmp1, tmp2):
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    rez = ""
    vmes = l_and(tmp1, tmp2)
    for i in vmes:
        if i == "1":
            rez += "0"
        else:
            rez += "1"
    text_result.delete(1.0, "end")
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)

def l_xnor(tmp1, tmp2):
    if len(tmp1) != len(tmp2):
        text_result.insert(1.0, "Števili nista iste dolžine!")
        return
    rez = ""
    vmes = l_xor(tmp1, tmp2)
    for i in vmes:
        if i == "1":
            rez += "0"
        else:
            rez += "1"
    text_result.delete(1.0, "end")
    rez_baza = pretvori(rez, 2, baza, False)
    text_result.insert(1.0, rez_baza)

def neg():
    global counter
    global baza
    counter += 1
    if counter == 1:
        text_result.insert(1.0, "Baza: ")
    elif counter == 2:
        baza = int(str(text_result.get(1.0, "end-1c")).split(" ")[1])
        text_result.delete(1.0, "end")
    elif counter == 3:
        counter = 0
        rez = ""
        st = str(text_result.get(1.0, "end-1c"))
        st = str(pretvori(st, baza, 2, False))
        for i in st:
            if i == "1":
                rez += "0"
            else:
                rez += "1"
        text_result.delete(1.0, "end")
        rez = str(pretvori(rez, 2, baza, False))
        text_result.insert(1.0, rez)

def sprozi():
    global tmp1
    global n
    global baza

    tmp2 = text_result.get(1.0, "end-1c")

    text_result.delete(1.0, "end")
    tmp1 = str(pretvori(tmp1, baza, 2, False))
    tmp2 = str(pretvori(tmp2, baza, 2, False))

    if len(tmp1) > len(tmp2):
        for _ in range(len(tmp1) - len(tmp2)):      # prepend: https://stackoverflow.com/questions/44792399/prepend-a-string-in-python
            tmp2 = "0" + tmp2
    elif len(tmp1) < len(tmp2):
        for _ in range(len(tmp2) - len(tmp1)):
            tmp1 = "0" + tmp1

    if n == 1:
        l_and(tmp1, tmp2)
    elif n == 2:
        l_or(tmp1, tmp2)
    elif n == 3:
        l_xor(tmp1, tmp2)
    elif n == 4:
        l_nor(tmp1, tmp2)
    elif n == 5:
        l_xnor(tmp1, tmp2)
    elif n == 6:
        l_nand(tmp1, tmp2)

def nalozi(k):
    global tmp1
    global n
    global counter
    global baza
    counter += 1
    n = k
    if counter == 1:
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "Baza: ")
    elif counter == 2:
        baza = int(str(text_result.get(1.0, "end-1c")).split(" ")[1])
        text_result.delete(1.0, "end")
    elif counter == 3:
        tmp1 = text_result.get(1.0, "end-1c")
        text_result.delete(1.0, "end")
        counter = 0


root = Tk()
root.title("Kalkulator")
root.geometry("375x350")

ikona = PhotoImage(file='calculator_icon.png')
root.iconphoto(True, ikona)

moj_okvir = ttk.Notebook(root)
moj_okvir.pack(pady=5)
osnovniKalkulator = Frame(moj_okvir, width=400, height=450, bg ="gray")
logicniOperatorji = Frame(moj_okvir, width=400, height=450, bg ="gray")
deloZDatotekami = Frame(moj_okvir, width=400, height=400, bg="gray")

osnovniKalkulator.pack(fill="both", expand=1)
logicniOperatorji.pack(fill="both", expand=1)
deloZDatotekami.pack(fill="both",expand=1)

moj_okvir.add(osnovniKalkulator, text="Kalkulator")
moj_okvir.add(logicniOperatorji, text="Logični operatorji")
moj_okvir.add(deloZDatotekami, text="Branje iz datotek")



#================================================ OSNOVNI KALKULATOR =============================================================
izracunano = Text(osnovniKalkulator, height=1, width=24, font=("Arial", 20))
izracun = Text(osnovniKalkulator, height=1, width=20, font=("Arial", 24))
izracun.tag_configure('tag-right', justify='right')
izracunano.grid(row=1,columnspan=7)
izracunano.tag_configure('tag-right', justify='right')
izracun.grid(row=2,columnspan=7)

btn_eksponent = Button(osnovniKalkulator, text="^", command=lambda: dodaj_v_racun('^'), width=5, font=("Arial", 14), bg="gray", fg="black")
btn_eksponent.grid(row=3, column = 2)
btn_eksponent = Button(osnovniKalkulator, text="%", command=lambda: dodaj_v_racun('%'), width=5, font=("Arial", 14), bg="gray", fg="black")
btn_eksponent.grid(row=3, column = 3)
btn_koren = tk.Button(osnovniKalkulator, text="√", command=lambda: dodaj_v_racun('√'), width=5, font=("Arial", 14), bg="gray", fg="black")
btn_koren.grid(row=3, column = 1)
btn_1 = tk.Button(osnovniKalkulator, text="1", command=lambda: dodaj_v_racun('1'), width=5, font=("Arial", 14))
btn_1.grid(row=4, column = 1)
btn_2 = tk.Button(osnovniKalkulator, text="2", command=lambda: dodaj_v_racun('2'), width=5, font=("Arial", 14))
btn_2.grid(row=4, column = 2)
btn_3 = tk.Button(osnovniKalkulator, text="3", command=lambda: dodaj_v_racun('3'), width=5, font=("Arial", 14))
btn_3.grid(row=4, column = 3)
btn_plus = tk.Button(osnovniKalkulator, text="+", command=lambda: dodaj_v_racun('+'), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_plus.grid(row=4, column = 4)
btn_4 = tk.Button(osnovniKalkulator, text="4", command=lambda: dodaj_v_racun('4'), width=5, font=("Arial", 14))
btn_4.grid(row=5, column = 1)
btn_5 = tk.Button(osnovniKalkulator, text="5", command=lambda: dodaj_v_racun('5'), width=5, font=("Arial", 14))
btn_5.grid(row=5, column = 2)
btn_6 = tk.Button(osnovniKalkulator, text="6", command=lambda: dodaj_v_racun('6'), width=5, font=("Arial", 14))
btn_6.grid(row=5, column = 3)
btn_minus = tk.Button(osnovniKalkulator, text="-", command=lambda: dodaj_v_racun('-'), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_minus.grid(row=5, column = 4)
btn_7 = tk.Button(osnovniKalkulator, text="7", command=lambda: dodaj_v_racun('7'), width=5, font=("Arial", 14))
btn_7.grid(row=6, column = 1)
btn_8 = tk.Button(osnovniKalkulator, text="8", command=lambda: dodaj_v_racun('8'), width=5, font=("Arial", 14))
btn_8.grid(row=6, column = 2)
btn_9 = tk.Button(osnovniKalkulator, text="9", command=lambda: dodaj_v_racun('9'), width=5, font=("Arial", 14))
btn_9.grid(row=6, column = 3)
btn_mnozenje = tk.Button(osnovniKalkulator, text="*", command=lambda: dodaj_v_racun('*'), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_mnozenje.grid(row=7, column = 4)
btn_leviOklepaj = tk.Button(osnovniKalkulator, text="(", command=lambda: dodaj_v_racun('('), width=5, font=("Arial", 14))
btn_leviOklepaj.grid(row=7, column = 1)
btn_0 = tk.Button(osnovniKalkulator, text="0", command=lambda: dodaj_v_racun('0'), width=5, font=("Arial", 14))
btn_0.grid(row=7, column = 2)
btn_desniOklepaj = tk.Button(osnovniKalkulator, text=")", command=lambda: dodaj_v_racun(')'), width=5, font=("Arial", 14))
btn_desniOklepaj.grid(row=7, column = 3)
btn_deljenje = tk.Button(osnovniKalkulator, text="/", command=lambda: dodaj_v_racun('/'), width=5, font=("Arial", 14), bg="orange", fg="white")
btn_deljenje.grid(row=6, column = 4)
btn_izracunaj = tk.Button(osnovniKalkulator, text="=", command=izracunaj, width=13, font=("Arial", 14), bg="orange", fg="white")
btn_izracunaj.grid(row=8, column = 1, columnspan=2)
btn_pocisti = tk.Button(osnovniKalkulator, text="C", command=lambda: pocisti(), width=5, font=("Arial", 14))
btn_pocisti.grid(row=8, column = 3)
# btn_brisiEnZnak = tk.Button(osnovniKalkulator, text="<=", command=lambda: odstrani_karakter(), width=5, font=("Arial", 14))
# btn_brisiEnZnak.grid(row=8, column = 4)



#================================================ LOGICNI OPERATORJI =============================================================
text_result = Text(logicniOperatorji, height=2, width=20, font=("Arial", 24))
text_result.tag_configure('tag-right', justify='right')
text_result.grid(columnspan=7)


# 3. točka: LOGIČNE OPERACIJE
btn_and = tk.Button(logicniOperatorji, text="AND", command=lambda: nalozi(1), width=5, font=("Arial", 14), pady=2)
btn_and.grid(row=2, column=1)
btn_or = tk.Button(logicniOperatorji, text="OR", command=lambda: nalozi(2), width=5, font=("Arial", 14))
btn_or.grid(row=2, column=2)
btn_xor = tk.Button(logicniOperatorji, text="XOR", command=lambda: nalozi(3), width=5, font=("Arial", 14))
btn_xor.grid(row=2, column=4)
btn_nor = tk.Button(logicniOperatorji, text="NOR", command=lambda: nalozi(4), width=5, font=("Arial", 14))
btn_nor.grid(row=3, column=4)
btn_xnor = tk.Button(logicniOperatorji, text="XNOR", command=lambda: nalozi(5), width=5, font=("Arial", 14))
btn_xnor.grid(row=4, column=4)
btn_nand = tk.Button(logicniOperatorji, text="NAND", command=lambda: nalozi(6), width=5, font=("Arial", 14))
btn_nand.grid(row=5, column=4)
btn_neg = tk.Button(logicniOperatorji, text="NEG", command=lambda: neg(), width=5, font=("Arial", 14))
btn_neg.grid(row=2, column=3)

btn_1 = tk.Button(logicniOperatorji, text="1", command=lambda: dodajSt(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column = 1)
btn_2 = tk.Button(logicniOperatorji, text="2", command=lambda: dodajSt(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column = 2)
btn_3 = tk.Button(logicniOperatorji, text="3", command=lambda: dodajSt(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column = 3)
btn_4 = tk.Button(logicniOperatorji, text="4", command=lambda: dodajSt(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column = 1)
btn_5 = tk.Button(logicniOperatorji, text="5", command=lambda: dodajSt(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column = 2)
btn_6 = tk.Button(logicniOperatorji, text="6", command=lambda: dodajSt(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column = 3)
btn_7 = tk.Button(logicniOperatorji, text="7", command=lambda: dodajSt(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column = 1)
btn_8 = tk.Button(logicniOperatorji, text="8", command=lambda: dodajSt(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column = 2)
btn_9 = tk.Button(logicniOperatorji, text="9", command=lambda: dodajSt(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column = 3)
btn_0 = tk.Button(logicniOperatorji, text="0", command=lambda: dodajSt(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column = 2)
btn_pocisti = tk.Button(logicniOperatorji, text="C", command=lambda: pocistiLogicnaVrata(), width=5, font=("Arial", 14))
btn_pocisti.grid(row=6, column = 4)

# 2. točka: PRETVRAJANJE ŠTEVIL
btn_pretvori = tk.Button(logicniOperatorji, text="PRET", command=lambda: pretvorba(), width=5, font=("Arial", 14))
btn_pretvori.grid(row=6, column=1)

btn_neg = tk.Button(logicniOperatorji, text="=", command=lambda: sprozi(), width=5, font=("Arial", 14))
btn_neg.grid(row=6, column=3) # vir za pisanje v okence: https://www.geeksforgeeks.org/how-to-get-the-input-from-tkinter-text-box/


#================================================ DELO Z DATOTEKAMI =============================================================
#5. tocka: Delo z datotekami

beriDatoteko = Text(deloZDatotekami, height=8, width=33, font=("Arial", 15))
beriDatoteko.grid(columnspan=12)


btn_odpri = tk.Button(deloZDatotekami, text="Odpri Datoteko", command=lambda: odpri_txt(),font=("Arial", 11))
btn_odpri.grid(row=3, column=0, columnspan=2)
btn_pocistiDat = tk.Button(deloZDatotekami, text="Clear", command=lambda: pocisti(), font=("Arial", 11))
btn_pocistiDat.grid(row=3, column = 5)



root.mainloop()