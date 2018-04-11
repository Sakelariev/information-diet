from fbs_runtime.application_context import ApplicationContext, \
    cached_property
import sys
import schedule
import time
from datetime import datetime as dt
import threading
import subprocess
import platform
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QApplication, QInputDialog, QLineEdit)


qtCreatorFile = "deepgui.ui" # Enter file here.
hosts_temp="hosts"
hosts_path=r"/etc/hosts"
redirect="127.0.0.1"
website_list=[]

class AppContext(ApplicationContext):
    def run(self):
        self.window.show()
        return self.app.exec_()
    @cached_property
    def window(self):
        Ui_MainWindow, QtBaseClass = uic.loadUiType(self.get_resource(qtCreatorFile))
        class MyApp2(MyApp, Ui_MainWindow):
            pass
        return MyApp2()
    @cached_property
    def app(self):
        return QApplication(sys.argv)

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.setSchedule)
        self.addButton.clicked.connect(self.addInputTextToListbox)
        self.inputWebsite.returnPressed.connect(self.addButton.click)
        self.removeButton.clicked.connect(self.removeWebsite)
        #self.startButton.clicked.connect(self.close) #Close the application after start is clicked
        #self.ui.startButton.clicked.connect(self.closeIt)

    # def closeIt(self):
    #     self.close()

    def removeWebsite(self):
        website_list.pop()
        self.listWidget.takeItem(self.listWidget.currentRow())


    def addInputTextToListbox(self):
        txt = self.inputWebsite.text()
        self.listWidget.addItem(txt)
        self.inputWebsite.clear()
        website_list.append(txt)
        print(website_list)

    def setSchedule(self):

        choose_s = self.timeBegin.time()
        choose_start = choose_s.toString()
        choose_start = choose_start[:-3]
        print(choose_start)
        choose_e = self.timeEnd.time()
        choose_end = choose_e.toString()
        choose_end = choose_end[:-3]
        print(choose_end)


        schedule.every().day.at(choose_start).do(self.turn_on)
        schedule.every().day.at(choose_end).do(self.turn_off)
        ScheduleThread().start()


    def turn_on(self):
        with open(hosts_path,'r+') as file:
            content=file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
                    if website.startswith('www.'): #We're adding www where needed
                        temp = website.split('www.')[1]
                        file.write(redirect+" " + temp + "\n")
                    else:
                        file.write(redirect+" " + "www." + website + "\n")
                    print("Blocked website")
        ###Turn off the blocker
    def turn_off(self):
        print("Unblocking everything")
        with open(hosts_path,'r+')as file:
            content=file.readlines()
            file.seek(0) #Starts reading at the first character
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #Imame golqm problem s mahaneto na failove ot hosts - maha samo chast ot tqh
        print("Unblocked everything")


class ScheduleThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(schedule.idle_seconds())
