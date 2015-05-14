# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timecardreminder.ui'
#
# Created: Thu May 07 15:49:37 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys, pickle

"initial PyQt stuff"
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    dateselected = None
    currentfile = None
    def __init__(self): 
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(389, 238)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setMargin(5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.calendarWidget = QtGui.QCalendarWidget(Form)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "*Reminder!*", None))
        self.label.setText(_translate("Form", "Reminder to do you time card!!", None))
        self.label_2.setText(_translate("Form", "Your timecard is due for filing. Please complete it ASAP then verify todays date on the calendar below \n"
"and click ok. I\'ll take care of the rest.", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton.clicked.connect(self.logSelectedDate)
    def logSelectedDate(self):
        self.dateselected = self.calendarWidget.selectedDate()
        self.storeSelectedDate()
    def storeSelectedDate(self):
        print self.dateselected 
        if self.dateselected is not None: 
            duedate = self.calculateNextDate(self.dateselected)
            self.currentfile = open("date.txt","wb")
            pickle.dump(duedate, self.currentfile)
            print "date stored to file as "+ str(duedate)
        else: print "couldnt write anything"
    def calculateNextDate(self,thisdate):
        return thisdate.addDays(14)

#use this method to prepare the file for reading       
def prepareFile(text):
    try:
        with open(text,'r') as file:
           print "file was found!"
           return
    except IOError as e:
        print "Unable to open file" #Does not exist OR no read permissions
        open(text,'w+')
        print "file created"
        pickle.dump(QtCore.QDate.currentDate(),open(text,"wb"))
        prepareFile(text)
        

if __name__ == '__main__': 
    "check to see if the current date matches with the stored date"
    prepareFile("date.txt")
    currentdate = QtCore.QDate.currentDate()
    storeddate = pickle.load(open("date.txt", "rb"))
    if currentdate == storeddate:
        app = QtGui.QApplication(sys.argv)
        ex = Ui_Form()
        ex.show()
        sys.exit(app.exec_())
    


