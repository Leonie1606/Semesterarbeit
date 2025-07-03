


import os
#import traceback
#import sys
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QInputDialog, QLineEdit
from PySide6.QtPdf import QPdfDocument
from windows.MainWindow import Ui_MainWindow
from windows.CriteriaWindow import Ui_CriteriaWindow
from dataloader import DataLoader
from filter import Filter


class CriteriaWindow(Ui_CriteriaWindow):
    """
    Klasse zur Erstellung des Fensters, das zur Eingabe der Auswahlkriterien verwendet wird.
    Die grundlegende Formatierung wird aus Ui_CriteriaWindow geerbt.
    """
    def __init__(self, verbose:bool=False)->None:
        """
        Initiierungsfunktion.
        param: verbose: bool, default: False; Aktivierung bzw. Deaktivierung von Printausgaben
        return: None
        """
        super().__init__() # erben aus uebergeordneter init-Funktion
        self.setupUi(self) # Aufsetzen des Fensters
        self.verbose = verbose # Zuweisung von verbose als Attribut
        # Dictionary zur Speicherung der Eingaben. Initialisiert mit None
        self.filter = Filter(verbose=self.verbose) # Erzeugen eines Filter-Objekts
        self.input_data = {'Vorname': None,
                           'Nachname': None,
                           'Professor': None,
                           'Lehrgebiet': None,
                           'Haarfarbe': None,
                           'Geschlecht': None,
                           'Brille': None}
        
        
        
        #=========Zuordnung der Buttons zu den Funktionen============
        self.pushButton_vorname.clicked.connect(self.selectFirstname)
        self.pushButton_nachname.clicked.connect(self.selectLastname)
        self.pushButton_professor.clicked.connect(self.selectProfessor)
        self.pushButton_harrfarbe.clicked.connect(self.selectHairColor)
        self.pushButton_geschlecht.clicked.connect(self.selectGender)
        self.pushButton_brille.clicked.connect(self.selectGlasses) 
    
    #=======================Buttonfunktionen=======================

    def selectFirstname(self)->None:
        """
        Funktion zur Eingabe des Vornamens als String mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data gespeichert.
        param: None
        return: None
        """
        firstname, ok = QInputDialog.getText(self, "Eingabe",
                                "Vorname:", QLineEdit.Normal)
        if ok and firstname:
            self.input_data['Vorname'] = firstname
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Vorname', filter_value=str(firstname))
        
        

    def selectLastname(self)->None:
        """
        Funktion zur Eingabe des Nachnamens als String mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data gespeichert.
        param: None
        return: None
        """
        lastname, ok = QInputDialog.getText(self, "Eingabe",
                                "Nachname:", QLineEdit.Normal)
        if ok and lastname:
            self.input_data['Nachname'] = lastname
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Nachname', filter_value=str(lastname))

    def selectProfessor(self)->None:
        """
        Funktion zur Auswahl, ob die Person Prof. ist, mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data als Bool gespeichert.
        param: None
        return: None
        """
        professor_list = ['ja', 'nein']
        professor, ok = QInputDialog.getItem(self, "Eingabe",
                                "Professor:", professor_list, 0, False)
        if ok and professor:
            if professor == 'ja':
                self.input_data['Professor'] = True
                prof = 'true'
            elif professor == 'nein':
                self.input_data['Professor'] = False
                prof = 'false'
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Professor', filter_value=prof)
    
    def selectHairColor(self)->None:
        """
        Funktion zur Auswahl der Haarfarbe mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data als String gespeichert.
        param: None
        return: None
        """
        colors = ['blond', 'braun', 'grau', 'keine Haare']
        color, ok = QInputDialog.getItem(self, "Eingabe",
                                "Haarfarbe:", colors, 0, False)
        if ok and color:
            self.input_data['Haarfarbe'] = color
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Haarfarbe', filter_value=color)
    
    def selectGender(self)->None:
        """
        Funktion zur Auswahl des Geschlechts mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data als String gespeichert.
        param: None
        return: None
        """
        genders = ['m', 'w', 'd']
        gender, ok = QInputDialog.getItem(self, "Eingabe",
                                "Geschlecht:", genders, 0, False)
        if ok and gender:
            self.input_data['Geschlecht'] = gender
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Geschlecht', filter_value=str(gender))

    def selectGlasses(self)->None:
        """
        Funktion zur Auswahl, ob Person eine Brille traegt, mit einem Dialogfenster.
        Eingabe wird im Dictionary self.input_data als Bool gespeichert.
        param: None
        return: None
        """
        glasses_list = ['ja', 'nein']
        glasses, ok = QInputDialog.getItem(self, "Eingabe",
                                "Brille:", glasses_list, 0, False)
        if ok and glasses:
            if glasses == 'ja':
                self.input_data['Brille'] = True
            elif glasses == 'nein':
                self.input_data['Brille'] = False
        if self.verbose:
            print(self.input_data)
        # Anwenden des Filters
        self.filter.apply(filter_category='Brille', filter_value=str(self.input_data['Brille'])) 

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Klasse zur Erstellung des Hauptfensters der Anwendung mit Darstellung 
    der Bilder und Namen der jeweiligen im Spiel befindlichen Personen.
    Grundlegende Funktionen des Fensters werden aus QMainWindow geerbt.
    Die grundlegende Formatierung des Fensters wird aus Ui_MainWindow geerbt.
    """
    def __init__(self, verbose:bool=False, iterations:int=5)->None:
        super().__init__() # erben aus uebergeordneter init-Funktion
        self.setupUi(self) # Aufsetzten des Fensters
        self.verbose = verbose # Zuweisung von verbose als Attribut
        self.iterations = iterations # Zuweisung der Anzahl an Versuchen als Attribut
        self.dl = DataLoader(verbose=self.verbose) # Erzeugung eines Objekts der Klasse DataLoader fuer spaetere Datenfilterung
        self.imageFilePath = 'Bilder' # Definition des Pfades, indem die Personenbilder abgelegt sind
        # Extrahieren der Dateinamen der Bilder und Speichern in Liste, wenn diese JPG-Dateien sind
        self.filenames = [file for file in os.listdir(self.imageFilePath) if '.jpg' in file]
        if self.verbose:
            print(self.filenames)
        #self.threadpool = QThreadPool()
        self.__loadData() # Aufrufen des Datenloaders
        self.__setImageToLabels() # Zuweisung der Personenbilder auf Labels im MainWindow
        self.__setNameToLabels() # Zuweisung der Personenname auf Labels im MainWindow
        self.updateTrialNumber()
        self.background = QPdfDocument(self)
        self.background.load("resources" + os.sep + "Hintergrund game.pdf")
        self.pushButton_eingabe.clicked.connect(self.openSelectionWindow) # Oeffnen des Auswahlfensters
        
    def paintEvent(self, event):
        painter = QPainter(self)
        img = self.background.render(0, QSize(self.width(), self.height()))
        painter.drawImage(self.rect(), img)
        painter.end()
        # restliche Widgets normal zeichnen
        super().paintEvent(event)
    
    def __loadData(self)->None:
        """
        Funktion zum Einladen des kompletten Datensatzes aus Excel-Datei
        und Zuweisung als Attribut
        param: None
        return: None
        """
        self.dataset = self.dl.getDataSet()
        if self.verbose:
            print(self.dataset)

    def __setImageToLabels(self)->None:
        """
        Funktion zur Zuweisung der Personenbilder auf die Labels im MainWindow
        param: None
        return: None
        """
        # Zuweisung der labels in eine Liste fuer spaetere iterative Zuweisung
        self.img_label_list = [
            self.img_label_1, self.img_label_2, self.img_label_3, self.img_label_4, self.img_label_5,
            self.img_label_6, self.img_label_7, self.img_label_8, self.img_label_9, self.img_label_10,
            self.img_label_11, self.img_label_12, self.img_label_13, self.img_label_14, self.img_label_15,
            self.img_label_16, self.img_label_17, self.img_label_18, self.img_label_19, self.img_label_20,
            self.img_label_21, self.img_label_22, self.img_label_23, self.img_label_24, self.img_label_25]
        
        # Fix-Groesse für alle Labels
        target_w, target_h = 110, 130

        for idx, label in enumerate(self.img_label_list):
            # 1) Bild direkt mit QPixmap laden
            path = os.path.join(self.imageFilePath, self.filenames[idx])
            pixmap = QPixmap(path)
            if pixmap.isNull():
                print("konnte nicht laden:", path)
                continue

            # 2) Pixmap manuell auf Wunschgröße skalieren
            scaled = pixmap.scaled(
                target_w, target_h,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            # 3) ins Label setzen
            label.setFixedSize(target_w, target_h)
            label.setScaledContents(False)   # Scaling per Pixmap, nicht per Label
            label.setPixmap(scaled)
            label.setAlignment(Qt.AlignCenter)

        # Iterative Zuweisung von Personenbilder an ensprechende Labels
        for index, label in enumerate(self.img_label_list):
            file = self.filenames[index]
            img = QImage('Bilder' + os.sep + file)  # Einladen des Bildes
            pixmap = QPixmap(img) # Umwnaldung in Pixmap, erforderlich fuer Zuweisung an Label
            label.setPixmap(pixmap) # Zuweisung an Label
            # Skalierung der Bilder
            label.setScaledContents(True)
            picSize = QSize(label.width() / 2 , label.height() / 4) #FIXME hier noch Bildgroesse anpassen
            label.resize(picSize)

    def __setNameToLabels(self)->None:
        """
        Funktion zur Zuweisung der Personennamen und der jeweiligen Anrede auf die Labels im MainWindow
        param: None
        return: None
        """
        # Zuweisung der labels in eine Liste fuer spaetere iterative Zuweisung
        self.text_label_list = [
            self.text_label_26, self.text_label_27, self.text_label_28, self.text_label_29, self.text_label_30,
            self.text_label_31, self.text_label_32, self.text_label_33, self.text_label_34, self.text_label_35,
            self.text_label_36, self.text_label_37, self.text_label_38, self.text_label_39, self.text_label_40,
            self.text_label_41, self.text_label_42, self.text_label_43, self.text_label_44, self.text_label_45,
            self.text_label_46, self.text_label_47, self.text_label_48, self.text_label_49, self.text_label_50]
        # Iterative Zuweisung von Personennamen an ensprechende Labels
        for index, label in enumerate(self.text_label_list):
            # Erfassung des Nachnamens anhand des Dateinamens des Bildes
            lastname = str(self.filenames[index]).removesuffix('.jpg')
            # Automatische Feststellung der Anrede
            label.setText(str(self.getPrefix(lastname=lastname)) + " " + lastname)
            label.setWordWrap(False) #  kein Zeilenumbruch
            label.setStyleSheet("""
                background-color: #262626;
                color: #FFFFFF;
                font-family: Helvetica;
                font-size: 18px;
                """)
    """
    def openThreadedSelectionWindow(self)->None:
        worker = Worker(self.openSelectionWindow)
        self.threadpool.start(worker)
    """

    def openSelectionWindow(self)->None:
        """
        Funktion zum Oeffnen des Auswahlfensters
        param: None
        return: None
        """
        self.w = CriteriaWindow(verbose=self.verbose) # Muss Attribut sein, damit sich das Fenster oeffnet
        self.w.show() 

    def getPrefix(self, lastname:str=None)->str:
        """
        Funktion zur automatischen Feststellung der Anrede der Personen.
        param: lastname: str, default: None, Nachname der Person
        return: str: self.prefix
        """
        # Einladen des Personendatensatzes (pd.DataFrame) anhand des Nachnamens und Transposition als Zeilenvektor
        dataset = self.dl.getDataSetByLastName(lastname=lastname).T
        # Pruefen, ob Person Professor/Professorin ist und ggf. Umwandlung in bool
        self.prof = self.checkBoolean(str(dataset.loc['Professor']).split()[1]) # Entfernen von Uberschriften aus pandas DataFrame
        if self.verbose: # Falls Printbefehle aktiv: Ausgabe des Datensatzes
            print(dataset)

        # Auswahl der Anrede
        if self.prof == True:
            self.prefix = 'Prof.'
        else:
            if str(dataset.loc['Geschlecht']).split()[1] == 'm':
                self.prefix = 'Herr'
            elif str(dataset.loc['Geschlecht']).split()[1] == 'w': 
                self.prefix = 'Frau'
            elif str(dataset.loc['Geschlecht']).split()[1] == 'd':
                self.prefix = 'Divers'
            else: # falls Eingabe nicht zugeordnet werden kann
                self.prefix = ''

        return self.prefix
    
    def checkBoolean(self, var:str=None)->bool:
        """
        Funktion zur Erkennung von Bool-Werten im Datensatz, 
        da diese als String in pd.DataFrame gespeichert werden.
        param: var: str, default: None, Zu pruefender Wert
        return: bool
        """
        if var == 'True' or var == 'true' or var == True:
            return True
        else: 
            return False
        
    def replaceImage(self, lastname:str=None)->None:
        """
        Funktion zum Ersetzen eines bestimmten Personenbildes durch
        ein rotes X. Dies bedeuted ein Ausschluss der Person im Spiel
        param: lastname: str, default: None; Nachname der Person
        return: None
        """
        lastname = f"{lastname}.jpg" # Erstellen des Dateipfads
        if lastname in self.filenames: # Iteration ueber alle gefundene Datensaetze
            index = self.filenames.index(lastname) # Zuordnung der Person zu einem einzigen Label
            label = self.img_label_list[index] # Auswahl des Labels fuer Bild
            img = QImage('resources' + os.sep + 'cross.jpg') # Einladen des Bilds
            pixmap = QPixmap(img) # Umwandlung als QPixmap
            label.setPixmap(pixmap) # Darstellung des Bilds in Hauptfenster
            label.setScaledContents(True) # Skalieren des Bilds
            picSize = QSize(label.width() / 2 , label.height() / 4)
            label.resize(picSize)

    def updateTrialNumber(self, count:int=0)->None:
        """
        Funktion zur Aktualisierung der verbleibenden Versuchsanzahl
        param: count:int; default: 0
        return: None
        """
        self.remaining_trials = self.iterations-count
        self.label_anzahl_versuche.setText(str(self.remaining_trials))

        
