#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:20:20 2021

@author: Marine Girardey
"""

from tkinter import Entry, Label, StringVar, Tk , Button
from individu import Individu

individu = {}

def get_fields():
    get_fields_as_list = []
    get_fields_as_list = Individu.insert_individu(widgets_entry["name"].get(), widgets_entry["last_name"].get(), widgets_entry["phone"].get(), widgets_entry["adress"].get(), widgets_entry["city"].get())
    key = get_fields_as_list[0]
    get_fields_as_list.remove(key)
    individu[key] = get_fields_as_list
    
    individu_file = open("/home/marine/Documents/M1_DLAD/INLO/TP6/individus.txt","a")
    for elem in get_fields_as_list:
        individu_file.writelines(elem)
        individu_file.writelines("\t")

    individu_file.writelines("\n")
    individu_file.close()
    
def search_datas():
    get_informations = Individu.search_individu(widgets_entry["name"].get(), individu)
    print(get_informations)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    widgets_entry["last_name"].config(text=var1)
    var1.set(get_informations[0])
    
    widgets_entry["phone"].config(text=var2)
    var2.set(get_informations[1])
    
    widgets_entry["adress"].config(text=var3)
    var3.set(get_informations[2])
    
    widgets_entry["city"].config(text=var4)
    var4.set(get_informations[3])
    
def del_datas():
    get_informations = Individu.remove_individu(widgets_entry["name"].get(), individu)
    

root = Tk()
root.title('Annuaire')

ids = ["name", "last_name", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

i, j = 0, 0

for idi in ids:
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.grid(row=i,column=0)

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.grid(row=i,column=1)

    i += 1

for idi in bouton:
    button = Button(root, text = idi)
    widgets_button[idi] = button
    button.grid(row=i+1,column=j)

    j += 1

widgets_button["inserer"].config(command = get_fields)
widgets_button["chercher"].config(command = search_datas)
widgets_button["effacer"].config(command = del_datas)

root.mainloop()

print(individu)


# 2.1− Implémentez le carnet d’adresse en utilisant une table associative 
# (un dictionnaire Python) indexée par lenom. Vous choisirez le type des valeurs 
# du dictionnaire. La classe représentant ce modèle de données doit avoirau moins 
# les méthodes permettant de chercher et d’insérer une fiche.
# 2.2− Implémentez le contrôleur et modifiez votre vue pour faire en sorte que les boutons appellent 
# ce contrôleur.Pour   rappel,   le   contrôleur   appelle   le   modèle   pour  
#  récupérer/modifier   des   données,   puis   modifie   la   vue   enconséquence 
#  (laquelle doit avoir les méthodes adéquates).Indications•Pour afficher des 
#  fenêtres «pop-up», utilisez le module tkMessageBox de Tkinter1.•Prenez soin 
#  de votre architecture..
# 3 Bonus
# 2.1− Faites en sorte de sauvegarder les données 
#  dans un fichier. Au lancement du programme, les données sontchargées à partir 
#  du fichier, si celui-ci existe. Utilisez, soit un fichier texte et un parser, 
#  soit le module pickle.
# 2.2− Créez une interface en ligne de commandes qui 
#  remplacerai la vue.