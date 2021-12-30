import tkinter as tk
import math
from tkinter import *

calculation = ""
izpis = ""

def dodaj_v_racun(symbol):
    global calculation
    global izpis
    print(calculation)
    izpis += str(symbol)
    calculation += str(symbol)
    calculation.replace("√", "")
    text_result.delete(1.0, "end")
    text_result.insert(1.0, izpis)

def izracunaj():
    global calculation
    global izpis
    racun = str(izpis) + " = "
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_result.insert(1.0, racun)
    except:
        pocisti()
        text_result.insert(1.0,"Error")

def pocisti():
    global calculation
    global izpis
    calculation = ""
    izpis = ""
    text_result.delete(1.0, "end")

def odstrani_karakter():
    global calculation
    global izpis
    izpis = izpis[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, izpis)

root = tk.Tk()
root.title("Kalkulator")
root.geometry("375x350")

ikona = PhotoImage(file='calculator_icon.png')
root.iconphoto(True, ikona)

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24))
text_result.grid(columnspan=5)


btn_eksponent = tk.Button(root, text="^", command=lambda: dodaj_v_racun('^'), width=5, font=("Arial", 14))
btn_eksponent.grid(row=2, column = 2)
btn_koren = tk.Button(root, text="√", command=lambda: dodaj_v_racun('√'), width=5, font=("Arial", 14))
btn_koren.grid(row=2, column = 1)
btn_1 = tk.Button(root, text="1", command=lambda: dodaj_v_racun(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column = 1)
btn_2 = tk.Button(root, text="2", command=lambda: dodaj_v_racun(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column = 2)
btn_3 = tk.Button(root, text="3", command=lambda: dodaj_v_racun(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column = 3)
btn_plus = tk.Button(root, text="+", command=lambda: dodaj_v_racun('+'), width=5, font=("Arial", 14))
btn_plus.grid(row=3, column = 4)
btn_4 = tk.Button(root, text="4", command=lambda: dodaj_v_racun(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column = 1)
btn_5 = tk.Button(root, text="5", command=lambda: dodaj_v_racun(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column = 2)
btn_6 = tk.Button(root, text="6", command=lambda: dodaj_v_racun(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column = 3)
btn_minus = tk.Button(root, text="-", command=lambda: dodaj_v_racun('-'), width=5, font=("Arial", 14))
btn_minus.grid(row=4, column = 4)
btn_7 = tk.Button(root, text="7", command=lambda: dodaj_v_racun(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column = 1)
btn_8 = tk.Button(root, text="8", command=lambda: dodaj_v_racun(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column = 2)
btn_9 = tk.Button(root, text="9", command=lambda: dodaj_v_racun(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column = 3)
btn_mnozenje = tk.Button(root, text="*", command=lambda: dodaj_v_racun('*'), width=5, font=("Arial", 14))
btn_mnozenje.grid(row=6, column = 4)
btn_leviOklepaj = tk.Button(root, text="(", command=lambda: dodaj_v_racun('('), width=5, font=("Arial", 14))
btn_leviOklepaj.grid(row=6, column = 1)
btn_0 = tk.Button(root, text="0", command=lambda: dodaj_v_racun(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column = 2)
btn_desniOklepaj = tk.Button(root, text=")", command=lambda: dodaj_v_racun(')'), width=5, font=("Arial", 14))
btn_desniOklepaj.grid(row=6, column = 3)
btn_deljenje = tk.Button(root, text="/", command=lambda: dodaj_v_racun('/'), width=5, font=("Arial", 14))
btn_deljenje.grid(row=5, column = 4)
btn_izracunaj = tk.Button(root, text="=", command=izracunaj, width=13, font=("Arial", 14))
btn_izracunaj.grid(row=7, column = 1, columnspan=2)
btn_pocisti = tk.Button(root, text="C", command=lambda: pocisti(), width=5, font=("Arial", 14))
btn_pocisti.grid(row=7, column = 3)
btn_brisiEnZnak = tk.Button(root, text="<=", command=lambda: odstrani_karakter(), width=5, font=("Arial", 14))
btn_brisiEnZnak.grid(row=7, column = 4)

root.mainloop()



