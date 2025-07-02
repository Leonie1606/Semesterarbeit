#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 21:23:38 2025

@author: lisametzner
"""

#import threading as th
from PySide6.QtWidgets import QApplication
from mainwindow_v2 import MainWindow
import sys

    
def main()->None:
    """
    Funktion zum Starten der Anwendung.
    """
    app = QApplication(sys.argv)
    # Erzeugung eines Objekts aus Klasse MainWindow mit aktiven Printausgaben
    mainWindow = MainWindow(verbose=False) 
    # Anzeigen des Objekts
    mainWindow.show()
    # Ausfuehren der Anwndung
    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()
