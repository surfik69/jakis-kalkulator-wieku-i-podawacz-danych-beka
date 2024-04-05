from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
from datetime import date
import tkinter.font


def calculate_age(born):
    today= date.today()
    age = today.year - born.year - ((today.month, today.day)<(born.month, born.day))
    return age

def calculate_adulty(born):
    today= date.today()
    age = today.year - born.year - ((today.month, today.day)<(born.month, born.day))
    if age>=18:
        return "Tak"
    else:
        return "Nie"

def sex_checker(name):
    if name == ("Kuba"):
        return "Mężczyzna"
    elif name[-1] == "a":
        return "Kobieta"
    else:
        return "Mężczyzna"
     
name, surname = tkinter.simpledialog.askstring("Dane","Podaj swoję pełne imię i nazwisko").split()
born_input = tkinter.simpledialog.askstring("Dane","Podaj swoją date urodzenia oddzieloną spacjami (dzien miesiac rok)")
email = tkinter.simpledialog.askstring("Dane","Podaj swój adres email")
city, ulica, dom = tkinter.simpledialog.askstring("Dane","Podaj swoje miasto, ulice, nr domu oddzielone przecinkami (miasto, ulica, nr)").split(", ")
weight = tkinter.simpledialog.askinteger("Dane:","Podaj swoją wage")
height = tkinter.simpledialog.askinteger("Dane","Podaj swój wzrost")
born_day, born_month, born_year = map(int, born_input.split())
born = date(born_year, born_month, born_day)

pound = 2.205
inches = 2.54
weight2 = weight * pound
height2 = height / inches

def bmi_calculate_health_check(weight, height, height2, weight2):
    if calculate_adulty == "Tak":
        bmi = weight/(height*height)
        return bmi
    else:
        a = weight2 * 703 
        b = height2 * height2
        bmi = a / b
        return bmi
    
def bmi_calculate(weight, height, height2, weight2):
    if calculate_adulty == "Tak":
        bmi2 = weight/(height*height)
        return "%.1f" % bmi2
    else:
        a = weight2 * 703 
        b = height2 * height2
        bmi2 = a / b
        return "%.1f" % bmi2
    
def health_check(bmi):
    if int(bmi) <= 18.5:
        return "Niedowaga"
    elif int(bmi) >= 18.5 and bmi <= 24.9:
        return "Zdrowy"
    elif int(bmi) >= 24 and bmi <= 29.9:
        return "Nadwaga"
    elif int(bmi) >= 30:
        return "Otyłość"
   
    
def betterlooking_date(born):
    lepszadata1 = ' | ' + '0' + str(born_day) + '-' + str(born_month) + '-' + str(born_year)
    lepszadata2 = ' | ' + '0' + str(born_day) + '-' + '0' + str(born_month) + '-' + str(born_year)
    lepszadata3 = ' | ' + str(born_day) + '-' + '0' + str(born_month) + '-' + str(born_year)
    lepszadata0 = ' | ' + str(born_day) + '-' + str(born_month) + '-' + str(born_year)
    if born_day < 10 and born_month < 10:
        return lepszadata2
    elif born_day < 10 and born_month >= 10:
        return lepszadata1
    elif born_day >= 10 and born_month < 10:
        return lepszadata3
    elif born_day >= 10 and born_month >= 10:
        return lepszadata0


def duzelitery(string):
    return string.capitalize()

 
dane = (
    "================================" + "\n"
    "Imie: " + duzelitery(name) + "\n" + 
    "Nazwisko: " + duzelitery(surname) + "\n" +
    "Płeć: " + sex_checker(name) + "\n" +
    "Wzrost: "+ str(height) + "cm" + "\n" +
    "Waga: " + str(weight) + "kg" + "\n" +
    "BMI: "+ str(bmi_calculate(weight, height, height2, weight2)) + "\n" +
    "Stan zdrowia: " + str(health_check(bmi_calculate_health_check(weight, height, height2, weight2))) + "\n" +
    "Wiek: " + str(calculate_age(born)) + betterlooking_date(born) + "\n" +
    "Czy pełnoletni?: " + calculate_adulty(born) + "\n"
    "Email: " + email + "\n" +
    "Adres: " + (duzelitery(city) + ", " + 'ul. ' + duzelitery(ulica) + " " + dom) + "\n"
    "================================" + "\n" +
    "\n" +
    "by: kizuG" + "\n"
)

tkinter.messagebox.showinfo("Twoje dane:", dane)
output = name + "_" + surname 
with open(output + ".txt","w") as f:
    f.write(dane)

