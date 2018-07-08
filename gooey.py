""" A GUI based python script to download your favourite videos directly """

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
import downloader
import os
import sys


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


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(428, 199)

        self.exit_button = QtGui.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(270, 140, 88, 34))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.start_download = QtGui.QPushButton(Dialog)
        self.start_download.setGeometry(QtCore.QRect(160, 100, 111, 31))
        self.start_download.setObjectName(_fromUtf8("download_button"))
        self.link = QtGui.QLineEdit(Dialog)
        self.link.setGeometry(QtCore.QRect(80, 60, 281, 31))
        self.link.setObjectName(_fromUtf8("Link"))
        self.about_button = QtGui.QPushButton(Dialog)
        self.about_button.setGeometry(QtCore.QRect(70, 140, 91, 34))
        self.about_button.setObjectName(_fromUtf8("about_button"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(290, 10, 83, 32))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setMaxVisibleItems(4)
        self.comboBox.setMaxCount(1080)
        self.comboBox.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.comboBox.setMinimumContentsLength(4)
        self.comboBox.setProperty("", _fromUtf8(""))
        self.comboBox.setObjectName(_fromUtf8("Video formats"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.comboBox.addItem(_fromUtf8("combobox"))
        self.label = QtGui.QLabel(Dialog, text="<b>Choose video Format!</b> ")
        self.label.setGeometry(QtCore.QRect(30, 10, 241, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Video Downloader", None))
        self.exit_button.setText(_translate("Dialog", "Exit", None))
        self.start_download.setText(_translate("Dialog", "Start Download", None))
        self.about_button.setText(_translate("Dialog", "About", None))
        self.comboBox.setItemText(0, _translate("Dialog", "1080p", None))
        self.comboBox.setItemText(1, _translate("Dialog", "720p", None))
        self.comboBox.setItemText(2, _translate("Dialog", "480p", None))
        self.comboBox.setItemText(3, _translate("Dialog", "360p", None))
        self.comboBox.setItemText(4, _translate("Dialog", "240p", None))
        self.comboBox.setItemText(4, _translate("Dialog", "144p", None))
        self.comboBox.setItemText(4, _translate("Dialog", "best", None))
        self.link.setPlaceholderText('Enter the URL of the video here!')


        self.exit_button.clicked.connect(exit)
        self.about_button.clicked.connect(self.about)
        self.start_download.clicked.connect(self.start_)

    def about(self):
        """ To display the About message box """
        msg = QtGui.QMessageBox()
        msg.setText("This Application is created by Ugtan aka Umang Taneja.")
        msg.setInformativeText("You can download your favourite youtube videos in one go only, just by entering the url of the video!")
        msg.setWindowTitle("About")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def start_(self):
        """ To start the downloading process """
        url = self.link.text()
        url = str(url)
        video_quality = str(self.comboBox.currentText())

        if url.startswith('https://youtu.be/'):
            download_message = QtGui.QMessageBox()
            download_message.setText("Requesting video...")
            download_message.setInformativeText("Video download started!")
            download_message.setWindowTitle("Download Started")
            download_message.setStandardButtons(QMessageBox.Ok)
            download_message.exec_()
            path = self.get_path()
            output = downloader.download(url, video_quality, path)
            finish_message = QtGui.QMessageBox()
            finish_message.setText(str(output))
            finish_message.setWindowTitle("Download Successfully!")
            finish_message.setStandardButtons(QMessageBox.Ok)
            finish_message.exec_()

        else:
            msg = QtGui.QMessageBox()
            msg.setText("Sorry, No videos found for the entered url.")
            msg.setWindowTitle("No Videos found!")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec_()

        sys.exit()


    def get_path(self):
        """ To set the path of the video to be downloaded """
        path = os.getcwd()
        path = path.split("/")[:-1]
        path = "/".join(path)
        path = path + '/Videos/'
        return path


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
