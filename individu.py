#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:53:49 2021

@author: Marine Girardey
"""

# from tkinter import get_fields

individu = {}

class Individu :
    def __init__(self, name, lastname, phone, adress, city):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.adress = adress
        self.city = city

    def __str__(self):
        return str(self.name + self.lastname + self.phone + self.adress + self.city)

    @staticmethod
    def insert_individu(name, lastname, phone, adress, city):
        # Update list to save names as a list of names
        list_all = []
        list_all.append(name)
        list_all.append(lastname)
        list_all.append(phone)
        list_all.append(adress)
        list_all.append(city)
        return list_all

        # Update dico with the list of names and associated informations
        # name = list_all[0]
        # print(name)
        # list_all.remove(name)
        # individu[name] = list_all
        # print(individu)

        # key = get_fields_as_list[0]
        # get_fields_as_list.remove(key)
        # individu[key] = get_fields_as_list

    @staticmethod
    def search_individu(name, individu):
        for elem in individu.keys():
            if elem == name:
                informations = individu[elem]
                return informations
    
    @staticmethod
    def remove_individu(name, individu):
        for elem in individu.keys():
            if name == elem:
                del individu[name]
                break
                print(individu)

print(individu)