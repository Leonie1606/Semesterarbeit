# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CriteriaWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_CriteriaWindow(QWidget):
    def setupUi(self, CriteriaWindow):
        #if not CriteriaWindow.objectName():
        #CriteriaWindow.setObjectName(u"CriteriaWindow")
        CriteriaWindow.resize(331, 213)
        self.label_heading_kriterien = QLabel(CriteriaWindow)
        self.label_heading_kriterien.setObjectName(u"label_heading_kriterien")
        self.label_heading_kriterien.setGeometry(QRect(138, 10, 58, 16))
        self.label_heading_kriterien.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(CriteriaWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 271, 151))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_vorname = QPushButton(self.layoutWidget)
        self.pushButton_vorname.setObjectName(u"pushButton_vorname")

        self.gridLayout.addWidget(self.pushButton_vorname, 0, 0, 1, 1)

        self.pushButton_nachname = QPushButton(self.layoutWidget)
        self.pushButton_nachname.setObjectName(u"pushButton_nachname")

        self.gridLayout.addWidget(self.pushButton_nachname, 0, 1, 1, 1)

        self.pushButton_professor = QPushButton(self.layoutWidget)
        self.pushButton_professor.setObjectName(u"pushButton_professor")

        self.gridLayout.addWidget(self.pushButton_professor, 1, 0, 1, 1)

        self.pushButton_harrfarbe = QPushButton(self.layoutWidget)
        self.pushButton_harrfarbe.setObjectName(u"pushButton_harrfarbe")

        self.gridLayout.addWidget(self.pushButton_harrfarbe, 1, 1, 1, 1)

        self.pushButton_geschlecht = QPushButton(self.layoutWidget)
        self.pushButton_geschlecht.setObjectName(u"pushButton_geschlecht")

        self.gridLayout.addWidget(self.pushButton_geschlecht, 2, 0, 1, 1)

        self.pushButton_brille = QPushButton(self.layoutWidget)
        self.pushButton_brille.setObjectName(u"pushButton_brille")

        self.gridLayout.addWidget(self.pushButton_brille, 2, 1, 1, 1)


        self.retranslateUi(CriteriaWindow)

        QMetaObject.connectSlotsByName(CriteriaWindow)
    # setupUi

    def retranslateUi(self, CriteriaWindow):
        CriteriaWindow.setWindowTitle(QCoreApplication.translate("CriteriaWindow", u"Auswahl der Kriterien", None))
        self.label_heading_kriterien.setText(QCoreApplication.translate("CriteriaWindow", u"Kriterien", None))
        self.pushButton_vorname.setText(QCoreApplication.translate("CriteriaWindow", u"Vorname", None))
        self.pushButton_nachname.setText(QCoreApplication.translate("CriteriaWindow", u"Nachname", None))
        self.pushButton_professor.setText(QCoreApplication.translate("CriteriaWindow", u"Professor", None))
        self.pushButton_harrfarbe.setText(QCoreApplication.translate("CriteriaWindow", u"Haarfarbe", None))
        self.pushButton_geschlecht.setText(QCoreApplication.translate("CriteriaWindow", u"Geschlecht", None))
        self.pushButton_brille.setText(QCoreApplication.translate("CriteriaWindow", u"Brille", None))
    # retranslateUi

