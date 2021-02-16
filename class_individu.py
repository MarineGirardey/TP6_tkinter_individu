#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:53:49 2021

@author: Marine Girardey
"""

# from tkinter import get_fields

# individu = {}

class Individu:
    """
    Individu Class Object for a Tkinter interface
    Parameters
    ----------
    name : int
    lastname : int
    phone : int
    adress : int
    city : int
        datas to insert, search or remove from the database
    """
    def __init__(self, list_of_informations):
        """Class constructor
        Parameters
        ----------
        name, lastname, phone, adress, city : int
            the datas corresponding to informations of the "individu"
        Returns
        -------
        None
            Individu object
        """
        self.name = list_of_informations[0]
        self.lastname = list_of_informations[1]
        self.phone = list_of_informations[2]
        self.adress = list_of_informations[3]
        self.city = list_of_informations[4]

    def __str__(self):
        """data property getter
        Returns
        -------
        int
            value of the data
        """
        return str(self.name + self.lastname + self.phone + self.adress + self.city)

    @staticmethod
    def insert_individu(list_of_informations):
        """
        insert a new "individu" according to input Tkinter informations
        Parameters
        ----------
        name, lastname, phone, adress, city : informations to input about the "individu"
        """
        # Update list to save names as a list of names
        name = list_of_informations[0]
        lastname = list_of_informations[1]
        phone = list_of_informations[2]
        adress = list_of_informations[3]
        city = list_of_informations[4]

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
        """
        search an individu according to the name
        Parameters
        ----------
        name : key value
        individu : dictionnary containing informations associated to the key
        """
        for elem in individu.keys():
            if elem == name:
                informations = individu[elem]
                return informations

    @staticmethod
    def remove_individu(name, individu):
        """
        remove an individu if name == elem from the input
        Parameters
        ----------
        name : searched data to delete
        """
        for elem in individu.keys():
            if name == elem:
                del individu[name]
                break
                # return individu

# print(individu)
