
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 21:23:38 2025

@author: Lisa Metzner und Leonie Ehrle
"""

import time
import sys
import threading as th 
import os
import json
from PySide6.QtWidgets import QApplication
from mainwindow_v3 import MainWindow


class Game:
    def __init__(self, verbose:bool=False, iterations:int=5)->None:
        """
        Initialisierungsfunktion der Klasse Game
        param: verbose: bool; default. False; Aktivieren/Deaktivieren von Printbefehlen
        param: iterations:int; default 5; Angabe der maximalen Versuche
        return: None
        """
        self.verbose = verbose # Zuorndung von verbose als Attribut
        self.iterations = iterations # Zuorndung von iterations als Attribut
        self.trialcount = 0 # Mitzaehlen der Versuche
    
    def run(self)->None:
        # Erzeugen eines Objektes der Klasse QApplication
        self.app = QApplication(sys.argv)
        # Erzeugung eines Objekts aus Klasse MainWindow mit aktiven Printausgaben
        self.mainWindow = MainWindow(verbose=self.verbose, iterations=self.iterations) 
        # Anzeigen des Objekts
        self.mainWindow.show()
        # Aktualisieren des Hauptfensters als Thread, damit parallele die Abfrage nach Kriterien stattfinden kann
        th.Thread(target=self.refreshMainWindow).start()       
        # Ausfuehren der Anwendung 
        self.app.exec()

    def refreshMainWindow(self)->None:
        previous_entries = 0    # Abgleich, ob neue Filterung stattgefunden hat
        while True:
            try:
                # Laden der json-Dateien fuer gefilterte Datensaetze
                with open('resources' + os.sep + 'filtered.json', encoding='utf-8') as file:
                    self.filtered = json.load(file)
                    file.close()
                # Laden der json-Dateien fuer entfernte Datensaetze
                with open('resources' + os.sep + 'removed.json', encoding='utf-8') as file:
                    self.removed = json.load(file)
                    file.close()

                # Zuorndung der Keys aus der json-Datei fuer entfernte Datensaetze
                self.removed_list = list(self.removed.keys()) # Liste fuer Iteration
                if self.removed_list[0]  != "key": # pruefen, ob json-Datei nicht leer ist
                    for lastname in self.removed_list: # Entfernen der jeweiligen Personen aus Hauptfenster
                        self.mainWindow.replaceImage(lastname=lastname) # Uebergabe an Hauptfenster
                    if previous_entries != len(self.removed_list): # aktualisiert Anzeige nur, wenn weitere Personen herausgefiltert wurden
                        self.trialcount +=1 # Wird erhoeht bei Filterung
                        self.mainWindow.updateTrialNumber(count=self.trialcount) # Aktualiseren des Hauptfensters
                        previous_entries = len(self.removed_list) # Zuordnung der aktuellen Anzahl der gefilterten Datensaetze als neuer Zustand
                if len(self.filtered) == 1:
                    # Beenden, wenn nur noch ein Datensatz uebrig
                    self.mainWindow.label_anzahl_versuche.setText('Gewonnen!')
                    break
                elif len(self.filtered) == 0:
                    # Beenden, wenn nur alle Datensaetze ausgeschlossen
                    self.mainWindow.label_anzahl_versuche.setText('Verloren!')
                    break
            except:
                pass
            # 2 s warten bis naechste Iteration
            time.sleep(2)


    def exit(self)->int:
        """
        Funktion zum Beenden des Programms
        param: None
        return: int: 0
        """
        sys.exit()
        QApplication.instance().quit()
        return 0

