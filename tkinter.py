#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:20:20 2021

@author: Marine Girardey
"""

from tkinter import Entry, Label, StringVar, Tk, Button
from class_individu import Individu

individu = {}
list_of_widgets = []

# Function to add an "individu"
def get_fields():
    """
    get fields from the Tkinter entry and save informations about a given "individu"
    Parameters
    ----------
    None
    """
    # Insert individu with informations in widgets
    get_fields_as_list = []
    list_of_widgets = widgets_entry["name"].get(), widgets_entry["last_name"].get(), widgets_entry["phone"].get(), widgets_entry["adress"].get(), widgets_entry["city"].get()
    get_fields_as_list = Individu.insert_individu(list_of_widgets)
    print(get_fields_as_list + "is added")

    # Update the dictionnary containing individus
    key = get_fields_as_list[0]
    get_fields_as_list.remove(key)
    individu[key] = get_fields_as_list

    # Write in a file each individu
    individu_file = open("/home/marine/Documents/M1_DLAD/INLO/TP6/individus.txt", "a")
    for elem in get_fields_as_list:
        individu_file.writelines(elem)
        individu_file.writelines("\t")
    individu_file.writelines("\n")
    individu_file.close()

# Fuction to search an individu according to the key (name)
def search_datas():
    # Use the class "Individu" to remove the individu
    get_informations = Individu.search_individu(widgets_entry["name"].get(), individu)

    # Create variable to print informations in each field
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    # Configure each entry to print corresponding informations
    widgets_entry["last_name"].config(text=var1)
    var1.set(get_informations[0])

    widgets_entry["phone"].config(text=var2)
    var2.set(get_informations[1])

    widgets_entry["adress"].config(text=var3)
    var3.set(get_informations[2])

    widgets_entry["city"].config(text=var4)
    var4.set(get_informations[3])

# Function to remove an individu
def del_datas():
    # Use the class "Individu" to remove the wanted individu
    get_informations = Individu.remove_individu(widgets_entry["name"].get(), individu)
    print(get_informations + "is delete")

# Creation of the Tkinter window
root = Tk()
root.title('Annuaire')

# Creation of the name of the widgets
ids = ["name", "last_name", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer"]

# Widget creation
widgets_labs = {}
widgets_entry = {}
widgets_button = {}

# Loop to create each widget
i, j = 0, 0

for idi in ids:
    # Label creation
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.grid(row=i, column=0)

    # Entry creation
    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.grid(row=i, column=1)

    i += 1

for idi in bouton:
    # Button creation
    button = Button(root, text=idi)
    widgets_button[idi] = button
    button.grid(row=i+1, column=j)

    j += 1

# Configure buttons
widgets_button["inserer"].config(command=get_fields)
widgets_button["chercher"].config(command=search_datas)
widgets_button["effacer"].config(command=del_datas)

root.mainloop()

print(individu)
