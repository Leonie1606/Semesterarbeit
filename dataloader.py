#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 15:56:34 2025

Class DataLoader

@author: lisametzner
"""
import pandas as pd
import numpy as np

class DataLoader:
    """
    Klasse für den Import und die Prozessierung von Personendaten
    aus einer spezifisch angelegten Excel-Datei.
    """
    def __init__(self, verbose:bool=False)->None:
        """
        Initiierungsfunktion der Klasse DataLoader.
        param: verbose: bool, default: False; Aktivierung und Deaktivierung von Printbefehlen
        return: None
        """
        self.verbose = verbose # Zuordnung als Attribut
        self.filepath = 'data.xlsx' # Name der Excel-Datei
        self.data = pd.read_excel(self.filepath) # Einlesen der Excel-Datei mit pandas und speichern als pd.DataFrame

        # Umwandlung des Strings in ein Bool und Beruecksichtigung von unterschiedlichen Schreibweisen (relevant fuer evtl. JSON)
        if str(self.data['Professor']) == 'true' or str(self.data['Professor']) == 'True':
            self.prof = True
        else:
            self.prof = False
        
        if str(self.data['Brille']) == 'true' or str(self.data['Brille']) == 'True':
            self.glasses = True
        else:
            self.glasses = False
        
        # Printbefehl aktiv, wenn self.verbose = True
        if self.verbose:
            # Ausgabe aller Datensaetze
            print(self.data)
    
    #=================Zugriff auf einzelen Spalten=================
    # Return als pd.DataFrame
    def getFirstName(self)->pd.DataFrame:
        return self.data['Vorname']
            
    def getLastName(self)->pd.DataFrame:
        return self.data['Nachname']
    
    def getProf(self)->pd.DataFrame:
        return self.prof
    
    def getSubject(self)->pd.DataFrame:
        return self.data['Lehrgebiet']
    
    def getHairColor(self)->pd.DataFrame:
        return self.data['Haarfarbe']
    
    def getGender(self)->pd.DataFrame:
        return self.data['Geschlecht']
    
    def getBrille(self)->pd.DataFrame:
        return self.glasses
    
    #=====================Zugriff auf einzelen Zeilen=================
    # Return als pd.DataFrame
    # Return einer definierten Zeile anhand eines Zeilenindex
    def getDataSet(self, row:int=0)->pd.DataFrame:
        return pd.DataFrame(self.data.iloc[row,:]).transpose() # Umwandlung von Spalen- in Zeilenvektor
    
    # Filtern eines Datensatze, relevant fuer spaeteren Zugriff auf Bilddateien
    def getDataSetByLastName(self, lastname:str=None)->pd.DataFrame:
        return self.data[self.data['Nachname']==lastname]
    
    # Auswahl eines zufaelligen Datansatzes fuer das Spiel
    def getRandomDataSet(self)->pd.DataFrame:
        row = np.random.randint(0, len(self.data['Vorname'])) # Zufallszahl zwischen 0 und der Anzahl an Personen
        return pd.DataFrame(self.data.iloc[row,:]).transpose() # Umwandlung von Spalten- in Zeilenvektor
    

    
    
# Funkion zum debuggen
#             
def main()->None:
    dl = DataLoader(verbose=True)
    #vorname = dl.getFirstName()
    #data = dl.getHairColor()
    dataset = dl.getDataSet(row=2)
    print(dataset)
if __name__ == "__main__":
    main()
        
        