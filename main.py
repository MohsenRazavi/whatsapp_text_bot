# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

class Ui_MainWindow(object):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    # ChromeDriverManager().install()

    # =============================== Qt codes ==========================================

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTab.setGeometry(QtCore.QRect(0, 0, 901, 631))
        self.MainTab.setObjectName("MainTab")
        self.help_tab = QtWidgets.QWidget()
        self.help_tab.setObjectName("help_tab")
        self.photo = QtWidgets.QLabel(self.help_tab)
        self.photo.setGeometry(QtCore.QRect(70, -10, 751, 391))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("logo/f.jpg"))
        self.photo.setScaledContents(False)
        self.photo.setObjectName("photo")
        self.Help_tips = QtWidgets.QTextBrowser(self.help_tab)
        self.Help_tips.setGeometry(QtCore.QRect(0, 390, 891, 192))
        self.Help_tips.setObjectName("Help_tips")
        self.MainTab.addTab(self.help_tab, "")
        self.run_tab = QtWidgets.QWidget()
        self.run_tab.setObjectName("run_tab")
        self.start_button = QtWidgets.QPushButton(self.run_tab)
        self.start_button.setGeometry(QtCore.QRect(10, 360, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.names_getter = QtWidgets.QLineEdit(self.run_tab)
        self.names_getter.setGeometry(QtCore.QRect(150, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.names_getter.setFont(font)
        self.names_getter.setObjectName("names_getter")
        self.message_getter = QtWidgets.QLineEdit(self.run_tab)
        self.message_getter.setGeometry(QtCore.QRect(150, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_getter.setFont(font)
        self.message_getter.setObjectName("message_getter")
        self.number_getter = QtWidgets.QLineEdit(self.run_tab)
        self.number_getter.setGeometry(QtCore.QRect(250, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_getter.setFont(font)
        self.number_getter.setObjectName("number_getter")
        self.name_getter_label = QtWidgets.QLabel(self.run_tab)
        self.name_getter_label.setGeometry(QtCore.QRect(10, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.name_getter_label.setFont(font)
        self.name_getter_label.setObjectName("name_getter_label")
        self.message_getter_label = QtWidgets.QLabel(self.run_tab)
        self.message_getter_label.setGeometry(QtCore.QRect(10, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.message_getter_label.setFont(font)
        self.message_getter_label.setObjectName("message_getter_label")
        self.number_getter_label = QtWidgets.QLabel(self.run_tab)
        self.number_getter_label.setGeometry(QtCore.QRect(10, 160, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.number_getter_label.setFont(font)
        self.number_getter_label.setObjectName("number_getter_label")
        self.Attack_button = QtWidgets.QPushButton(self.run_tab)
        self.Attack_button.setGeometry(QtCore.QRect(240, 360, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Attack_button.setFont(font)
        self.Attack_button.setObjectName("Attack_button")
        self.Stop = QtWidgets.QPushButton(self.run_tab)
        self.Stop.setGeometry(QtCore.QRect(460, 360, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Stop.setFont(font)
        self.Stop.setObjectName("Stop")
        self.done_people_show = QtWidgets.QTextBrowser(self.run_tab)
        self.done_people_show.setGeometry(QtCore.QRect(0, 440, 681, 151))
        self.done_people_show.setObjectName("done_people_show")
        self.sent_messages_show = QtWidgets.QTextBrowser(self.run_tab)
        self.sent_messages_show.setGeometry(QtCore.QRect(680, 10, 221, 581))
        self.sent_messages_show.setObjectName("sent_messages_show")
        self.Defulat_settings = QtWidgets.QLabel(self.run_tab)
        self.Defulat_settings.setGeometry(QtCore.QRect(10, 240, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.Defulat_settings.setFont(font)
        self.Defulat_settings.setObjectName("Defulat_settings")
        self.ip_port = QtWidgets.QRadioButton(self.run_tab)
        self.ip_port.setGeometry(QtCore.QRect(300, 250, 355, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ip_port.setFont(font)
        self.ip_port.setObjectName("ip_port")
        self.hacking = QtWidgets.QRadioButton(self.run_tab)
        self.hacking.setGeometry(QtCore.QRect(20, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hacking.setFont(font)
        self.hacking.setObjectName("hacking")
        self.encripting_data = QtWidgets.QRadioButton(self.run_tab)
        self.encripting_data.setGeometry(QtCore.QRect(190, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encripting_data.setFont(font)
        self.encripting_data.setObjectName("encripting_data")
        self.Wh_photo = QtWidgets.QLabel(self.run_tab)
        self.Wh_photo.setGeometry(QtCore.QRect(390, 20, 281, 221))
        self.Wh_photo.setText("")
        self.Wh_photo.setPixmap(QtGui.QPixmap("logo/Anonymous-1200x818.jpg"))
        self.Wh_photo.setScaledContents(True)
        self.Wh_photo.setObjectName("Wh_photo")
        self.encripting_data_2 = QtWidgets.QRadioButton(self.run_tab)
        self.encripting_data_2.setGeometry(QtCore.QRect(420, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encripting_data_2.setFont(font)
        self.encripting_data_2.setObjectName("encripting_data_2")
        self.MainTab.addTab(self.run_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============================== Qt codes end ==========================================

# ========================================== my codes ======================================
        self.start_button.clicked.connect(self.start_pushed)
        self.Attack_button.clicked.connect(self.attack_pushed)
        self.Stop.clicked.connect(self.stop_pushed)
        self.encripting_data_2.setChecked(True)
# ====================================== my codes end =======================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Help_tips.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Welcome To WhatsApp DDOS Attacker !</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click on START button</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Login to your whatsapp account</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Wait for logging in</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Scroll down to see your intended contact</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. Enter his/her name , your message (you can choose one of defualts) , enter number of repeats</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6. Click on Attack ! to start attack !</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">7. You can cancel every attack by clicking on Stop</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Developer : MohsenRazavi 2095</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">App version : 2.0.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">@2022</span></p></body></html>"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.help_tab), _translate("MainWindow", "Help"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.name_getter_label.setText(_translate("MainWindow", "Names :"))
        self.message_getter_label.setText(_translate("MainWindow", "Message  :"))
        self.number_getter_label.setText(_translate("MainWindow", "Number of repeats :"))
        self.Attack_button.setText(_translate("MainWindow", "Attack !"))
        self.Stop.setText(_translate("MainWindow", "Stop !"))
        self.Defulat_settings.setText(_translate("MainWindow", "Defualt message settings :"))
        self.ip_port.setText(_translate("MainWindow", "Infiltrating through IP-PORT : 192.168.1.1 : i"))
        self.hacking.setText(_translate("MainWindow", "HCKING port : i"))
        self.encripting_data.setText(_translate("MainWindow", "Encripting data part : i"))
        self.encripting_data_2.setText(_translate("MainWindow", "No default message"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.run_tab), _translate("MainWindow", "Run"))
# =============================== Qt codes end ==========================================

# ========================================== my codes =====================================

    def start_pushed(self):
        app.processEvents()
        start_time = datetime.utcnow()
        self.done_people_show.append(f'-----> APP STARTED AT {start_time} <----')
        self.driver.get('https://web.whatsapp.com/')

    def attack_pushed(self):
        names = (self.names_getter.displayText()).split('-')
        num = int(self.number_getter.displayText())
        msg = self.message_getter.displayText()
        self.Wh_photo.setGeometry(QtCore.QRect(390, 20, 281, 171))
        self.Wh_photo.setPixmap(QtGui.QPixmap("logo/82051-anonymus-hoodie-mask-artist-artwork-digital-art.jpg"))

        for name in names:
            app.processEvents()
            tim = time.localtime()
            start_attack_time = time.strftime("%H:%M:%S", tim)
            self.done_people_show.append(f'Start attacking to {name} at {start_attack_time} !')
            chat_name = f'//span[@title="{name}"]'
            # chat = self.driver.find_element_by_xpath(chat_name)
            chat = self.driver.find_element("xpath", chat_name)
            chat.click()
            text_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
            # text_box = self.driver.find_element_by_xpath(text_box_xpath)
            text_box = self.driver.find_element("xpath", text_box_xpath)

            for i in range(1, num + 1):
                app.processEvents()
                if self.ip_port.isChecked():
                    sending_msg = f'IP-PORT 192.168.1.1 : {i}'
                elif self.hacking.isChecked():
                    sending_msg = f'Hacking your device - port : {i}'
                elif self.encripting_data.isChecked():
                    sending_msg = f'Encripting your data and information | part : {i}'
                else:
                    sending_msg = f'{msg}'
                text_box.send_keys(sending_msg, Keys.ENTER)
                self.sent_messages_show.append(f'| {i} {sending_msg} -> sent to {name}! |')
            tim = time.localtime()
            end_attack_time = time.strftime("%H:%M:%S", tim)
            self.done_people_show.append(f'{name} Done at {end_attack_time} !')
            self.sent_messages_show.append('-----------------------------')

        self.Wh_photo.setGeometry(QtCore.QRect(390, 20, 281, 221))
        self.Wh_photo.setPixmap(QtGui.QPixmap("logo/Anonymous-1200x818.jpg"))

    def stop_pushed(self):
        app.processEvents()
        end_time = datetime.utcnow()
        self.done_people_show.append(f'-----> APP STOPPED AT {end_time} <----')
        self.Wh_photo.setGeometry(QtCore.QRect(390, 20, 281, 221))
        self.Wh_photo.setPixmap(QtGui.QPixmap("logo/Anonymous-1200x818.jpg"))
        self.driver.close()
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
