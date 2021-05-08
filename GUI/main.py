import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import Download

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.returnPressed.connect(self.loginfunction)

    def loginfunction(self):
        login=self.login.text()
        password=self.password.text()
        #print("Successfully logged in with login: ", login, "and password:", password)
        if login == "admin" and password == "passer":
            self.gotoAccueil()
            print("Successfully logged in with login: ", login, "and password:", password)
        else:
            self.showMessage("ERROR!", "Bad Credentiels")


    def gotoAccueil(self):
        accueil=Accueil()
        widget.addWidget(accueil)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def showMessage(self,title, msg):
        QMessageBox.information(None, title, msg)

class Accueil(QDialog):
    def __init__(self):
        super(Accueil,self).__init__()
        loadUi("accueil.ui",self)
        self.md1Button.clicked.connect(self.gotoModule1)
        self.md2Button.clicked.connect(self.gotoModule2)
        self.md3Button.clicked.connect(self.gotoModule3)
        self.md4Button.clicked.connect(self.gotoModule4)
    
    def gotoModule1(self):
        md1 = Module1()
        widget.addWidget(md1)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotoModule2(self):
        md2 = Module2()
        widget.addWidget(md2)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotoModule3(self):
        md3 = Module3()
        widget.addWidget(md3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoModule4(self):
        md4 = Module4()
        widget.addWidget(md4)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Module1(QDialog):
    def __init__(self):
        super(Module1,self).__init__()
        loadUi("md1.ui",self)
        self.telecharger.clicked.connect(self.downloadAndExtract)
        self.retour.clicked.connect(self.gotoPrevious)

    def gotoPrevious(self):
        accueil=Accueil()
        widget.addWidget(accueil)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def downloadAndExtract(self):
        print("Downloading ...")
        Download.downloader()


class Module2(QDialog):
    def __init__(self):
        super(Module2,self).__init__()
        loadUi("md2.ui",self)
        self.charger.clicked.connect(self.loadData)
        self.parcourir.clicked.connect(self.parcours)
        self.previsualiser.clicked.connect(self.previsualize)
        self.retour.clicked.connect(self.gotoPrevious)

    def gotoPrevious(self):
        accueil=Accueil()
        widget.addWidget(accueil)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadData(self):
        print("Loading on db...")

    def parcours(self):
        print("Parcours ...")

    def previsualize(self):
        print("Previsualisation ...")


class Module3(QDialog):
    def __init__(self):
        super(Module3,self).__init__()
        loadUi("md3.ui",self)
        self.explorer.clicked.connect(self.explore)
        self.retour.clicked.connect(self.gotoPrevious)

    def gotoPrevious(self):
        accueil=Accueil()
        widget.addWidget(accueil)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def explore(self):
        print("Exploring ...")


class Module4(QDialog):
    def __init__(self):
        super(Module4,self).__init__()
        loadUi("md4.ui",self)
        self.btn1.clicked.connect(self.explore)
        self.btn2.clicked.connect(self.explore)
        self.btn3.clicked.connect(self.explore)
        self.retour.clicked.connect(self.gotoPrevious)

    def gotoPrevious(self):
        accueil=Accueil()
        widget.addWidget(accueil)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def explore(self):
        print("Exploring ...")

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        login = self.login.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with login: ", login, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(920)
widget.setFixedHeight(920)
widget.show()
app.exec_()