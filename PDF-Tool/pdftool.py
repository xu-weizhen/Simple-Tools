# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdftool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtGui import QIcon
from PyPDF2 import PdfFileReader, PdfFileWriter
import requests
from PIL import Image
from aip import AipOcr

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 409)
        self.ub_cut = QtWidgets.QPushButton(Form)
        self.ub_cut.setGeometry(QtCore.QRect(120, 170, 101, 51))
        self.ub_cut.setObjectName("ub_cut")
        self.ub_pdf2word = QtWidgets.QPushButton(Form)
        self.ub_pdf2word.setGeometry(QtCore.QRect(300, 170, 101, 51))
        self.ub_pdf2word.setObjectName("ub_pdf2word")
        self.ub_pic2word = QtWidgets.QPushButton(Form)
        self.ub_pic2word.setGeometry(QtCore.QRect(350, 320, 101, 51))
        self.ub_pic2word.setObjectName("ub_pic2word")
        self.ul_filename = QtWidgets.QLabel(Form)
        self.ul_filename.setGeometry(QtCore.QRect(60, 50, 261, 31))
        self.ul_filename.setObjectName("ul_filename")
        self.ul_page = QtWidgets.QLabel(Form)
        self.ul_page.setGeometry(QtCore.QRect(70, 120, 81, 18))
        self.ul_page.setObjectName("ul_page")
        self.ut_page = QtWidgets.QTextEdit(Form)
        self.ut_page.setGeometry(QtCore.QRect(170, 110, 261, 31))
        self.ut_page.setObjectName("ut_page")
        self.ut_id = QtWidgets.QTextEdit(Form)
        self.ut_id.setGeometry(QtCore.QRect(100, 260, 231, 31))
        self.ut_id.setObjectName("ut_id")
        self.ut_key1 = QtWidgets.QTextEdit(Form)
        self.ut_key1.setGeometry(QtCore.QRect(100, 300, 231, 31))
        self.ut_key1.setObjectName("ut_key1")
        self.ut_key2 = QtWidgets.QTextEdit(Form)
        self.ut_key2.setGeometry(QtCore.QRect(100, 340, 231, 31))
        self.ut_key2.setObjectName("ut_key2")
        self.ul_id = QtWidgets.QLabel(Form)
        self.ul_id.setGeometry(QtCore.QRect(60, 260, 21, 18))
        self.ul_id.setObjectName("ul_id")
        self.ul_key1 = QtWidgets.QLabel(Form)
        self.ul_key1.setGeometry(QtCore.QRect(50, 300, 41, 20))
        self.ul_key1.setObjectName("ul_key1")
        self.ul_key2 = QtWidgets.QLabel(Form)
        self.ul_key2.setGeometry(QtCore.QRect(50, 340, 41, 18))
        self.ul_key2.setObjectName("ul_key2")
        self.ub_folder = QtWidgets.QPushButton(Form)
        self.ub_folder.setGeometry(QtCore.QRect(350, 250, 101, 51))
        self.ub_folder.setObjectName("ub_folder")
        self.ub_choose = QtWidgets.QPushButton(Form)
        self.ub_choose.setGeometry(QtCore.QRect(350, 40, 101, 51))
        self.ub_choose.setObjectName("ub_choose")
        self.ub_choose.raise_()
        self.ub_cut.raise_()
        self.ub_pdf2word.raise_()
        self.ub_pic2word.raise_()
        self.ul_filename.raise_()
        self.ub_choose.raise_()
        self.ul_page.raise_()
        self.ut_page.raise_()
        self.ut_id.raise_()
        self.ut_key1.raise_()
        self.ut_key2.raise_()
        self.ul_id.raise_()
        self.ul_key1.raise_()
        self.ul_key2.raise_()
        self.ub_folder.raise_()

        self.ouput_pdf = "out.pdf"              # 输出分割后PDF文件文件名及路径
        self.output_words_pdf = "words_pdf.txt" # 输出PDF提取文字的文件文件名及路径
        self.picfolder = "pic"                  # 图片文件夹路径
        self.keyfile = "key.dat"                # 百度API秘钥文件
        self.output_words_pic = "words_pic.txt" # 输出图片提取文字的文件文件名及路径

        self.filename = ''
        self.filepath = ''
        self.page = -1
        self.pagelist = []
        self.app = ''
        self.key1 = ''
        self.key2 = ''

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #槽函数
        self.ub_choose.clicked.connect(self.f_choose)
        self.ub_cut.clicked.connect(self.f_cut)
        self.ub_pdf2word.clicked.connect(self.f_pdf2word)
        self.ub_folder.clicked.connect(self.f_openfolder)
        self.ub_pic2word.clicked.connect(self.f_pic2word)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF转换工具"))
        self.ub_cut.setText(_translate("Form", "分割PDF"))
        self.ub_pdf2word.setText(_translate("Form", "PDF转文字"))
        self.ub_pic2word.setText(_translate("Form", "图片转文字"))
        self.ul_filename.setText(_translate("Form", "请选择PDF文件"))
        self.ul_page.setText(_translate("Form", "选择页码"))
        self.ul_id.setText(_translate("Form", "ID"))
        self.ul_key1.setText(_translate("Form", "KEY1"))
        self.ul_key2.setText(_translate("Form", "KEY2"))
        self.ub_folder.setText(_translate("Form", "图片文件夹"))
        self.ub_choose.setText(_translate("Form", "选择PDF"))

        try:
            f = open(self.keyfile, 'rb')
            text = f.read()
            f.close()
            text = str(text)[2:-1]

            if len(text) > 10:
                i = 0
                j = 1
                count = 0
                while count < 3 and j in range(len(text)):
                    if text[j] == '@' and text[j] == '@':
                        if count == 0:
                            self.app = text[i:j]
                        elif count == 1:
                            self.key1 = text[i:j]
                        elif count == 2:
                            self.key2 = text[i:j]
                        count += 1
                        i = j+2
                        j = i+1
                    else:
                        j += 1

            if self.app != '' and self.key1 != '' and self.key2 != '':
                if len(self.app) > 10:
                    self.ut_id.setText((self.app[0:5]+"*****"+self.app[-5:]))
                else:
                    self.ut_id.setText((self.app[0:2] + "*****" + self.app[-2:]))

                if len(self.key1) > 10:
                    self.ut_key1.setText((self.key1[0:5] + "*****" + self.key1[-5:]))
                else:
                    self.ut_key1.setText((self.key1[0:2] + "*****" + self.key1[-2:]))

                if len(self.key2) > 10:
                    self.ut_key2.setText((self.key2[0:5] + "*****" + self.key2[-5:]))
                else:
                    self.ut_key2.setText((self.key2[0:2] + "*****" + self.key2[-2:]))
            else:
                self.app = ''
                self.key1 = ''
                self.key2 = ''
        except Exception as e:
            print(e)
            self.app = ''
            self.key1 = ''
            self.key2 = ''

    # 打开文件
    def f_choose(self):
        new_filename, file_type = QtWidgets.QFileDialog.getOpenFileName(None,"打开文件","./","PDF文件 (*.pdf *.PDF);;所有文件 (*)")
        if new_filename != '':
            self.filepath = new_filename
            print(self.filepath)
            count = len(new_filename)-1
            while count>0:
                if new_filename[count] == '/':
                    break
                count = count-1

            openpdf = open(self.filepath,'rb')
            pdfFileReader = PdfFileReader(openpdf)
            pageCount = pdfFileReader.getNumPages()
            openpdf.close()
            self.page = pageCount

            self.filename = new_filename[count + 1:]
            if len(self.filename) > 22:
                self.filename = self.filename[0:19] + "..."
            self.filename = self.filename + " (" + str(pageCount) + "页)"
            self.ul_filename.setText(self.filename)

            if pageCount>1:
                p = "1-" + str(pageCount)
            else:
                p = str(pageCount)
            self.ut_page.setText(p)
            
        else:
            if self.filename == '':
                self.ul_filename.setText("请选择PDF文件")
            else:
                self.ul_filename.setText(self.filename)

    # 获取需要处理的页码
    def f_get_page(self):

        cutpage = self.ut_page.toPlainText()

        # 未选择文件
        if self.page == -1:
            msg = "请先选择文件 " + cutpage
            self.ut_page.setText(msg)
            return False

        # 输入为空
        if cutpage == '' or cutpage == "请在此输入需要分割出的页面":
            self.ut_page.setText("请在此输入需要分割出的页面")
            return False

        self.pagelist = []
        i = 0
        j = 1
        to = False
        error = False
        while j < len(cutpage) and not error:
            if cutpage[j] == ',' or cutpage[j] == '，':
                if to:
                    try:
                        p2 = int(cutpage[i:j])
                    except Exception as e:
                        msg = '只能输入数字、"，"和"-" ' + cutpage
                        self.ut_page.setText(msg)
                        return False
                    if p1 <= p2:
                        while p1 != p2:
                            self.pagelist.append(p1)
                            p1 = p1+1
                        self.pagelist.append(p2)
                        to = False
                        i = j+1
                        j = j+2
                    else:
                        error = True
                else:
                    try:
                        p2 = int(cutpage[i:j])
                    except Exception as e:
                        msg = '只能输入数字、"，"和"-" ' + cutpage
                        self.ut_page.setText(msg)
                        return False
                    self.pagelist.append(p2)
                    i = j+1
                    j = j+2
            else:
                if cutpage[j] == '-' :
                    to = True
                    try:
                        p1 = int(cutpage[i:j])
                    except Exception as e:
                        msg = '只能输入数字、"，"和"-" ' + cutpage
                        self.ut_page.setText(msg)
                        return False
                    i = j+1
                    j = j+2
                else:
                    j = j+1

        if not error:
            if to:
                try:
                    p2 = int(cutpage[i:j])
                except Exception as e:
                    msg = '只能输入数字、"，"和"-" ' + cutpage
                    self.ut_page.setText(msg)
                    return False
                if p1 <= p2:
                    while p1 != p2:
                        self.pagelist.append(p1)
                        p1 = p1+1
                    self.pagelist.append(p2)
                else:
                    error = True
            else:
                try:
                    p2 = int(cutpage[i:j])
                except Exception as e:
                    msg = '只能输入数字、"，"和"-" ' + cutpage
                    self.ut_page.setText(msg)
                    print(e)
                    return False
                self.pagelist.append(p2)

        if error:
            msg = "输入页码有误 " + cutpage
            self.ut_page.setText(msg)
            return False

        for k in self.pagelist:
            if k > self.page:
                msg = "该文件最大页码为" + str(self.page) + " " + cutpage
                self.ut_page.setText(msg)
                return False

        return True

    # 分割文件
    def f_cut(self):
        if self.f_get_page():
            pdf_output = PdfFileWriter()
            pdf_input = PdfFileReader(open(self.filepath, 'rb'))
            for i in self.pagelist:
                pdf_output.addPage(pdf_input.getPage(i - 1))
            pdf_output.write(open(self.ouput_pdf, 'wb'))
            cutpage = self.ut_page.toPlainText()
            self.ut_page.setText("分割完成 "+cutpage)

    # 提取文字
    def f_pdf2word(self):
        if self.f_get_page():
            cutpage = self.ut_page.toPlainText()
            pdfReader = PdfFileReader(self.filepath)
            try:
                f = open(self.output_words_pdf, 'a')
            except:
                self.ut_page.setText("打开输出文件失败 " + cutpage)
                return

            try:
                for i in self.pagelist:
                    text = pdfReader.getPage(i-1)
                    f.write(text.extractText().encode('GBK','ignore').decode('GBk'))
                    f.write("\n\n")
                f.close()
                self.ut_page.setText("提取文字成功 " + cutpage)
            except Exception as e:
                self.ut_page.setText("提取文字失败 " + cutpage)
                print(e)

    # 打开文件夹
    def f_openfolder(self):
        if not os.path.exists(self.picfolder):
            os.makedirs(self.picfolder)

        pwd = os.getcwd()
        start_directory = pwd + "\\" + self.picfolder
        os.startfile(start_directory)

    # 图片转文字
    def f_pic2word(self):
        if self.app == '' or self.key1 == '' or self.key2 == '':
            id = self.ut_id.toPlainText()
            key1 = self.ut_key1.toPlainText()
            key2 = self.ut_key2.toPlainText()

            if id == '' or key1 == '' or key2 == '':
                if id == '':
                    self.ut_id.setText("请输入id")
                if key1 == '':
                    self.ut_key1.setText("请输入key1")
                if key2 == '':
                    self.ut_key2.setText("请输入key2")
                return
        else:
            id = self.app
            key1 = self.key1
            key2 = self.key2

        success = 0
        fail = 0
        miss = 0
        path = self.picfolder + "\%d.jpg"
        for i in range(1, 1000):
            APP_ID = id
            APP_KEY = key1
            SECRET_KEY = key2
            client = AipOcr(APP_ID, APP_KEY, SECRET_KEY)

            options = {}
            options["language_type"] = "CHN_ENG"
            options["detect_direction"] = "false"
            options["detect_language"] = "false"
            options["probability"] = "false"

            try:
                img = open(path % i, "rb")
                res = client.basicGeneral(img.read(), options)
                img.close()

                word = str(res['words_result'])
                t = word.split("'}, {'")
                t2 = ""
                for i in t:
                    t2 += i[9:]
                    t2 += '\n'
                t2 = t2[3:-4]
                t2 += "\n\n"

                try:
                    f = open(self.output_words_pic, 'a')
                    f.write(t2)
                    f.write("\n\n")
                    f.close()
                    success += 1
                except Exception as e:
                    print(e)
                    fail += 1

                print(t2)
                print("\n\n")

            except Exception as e:
                print(e)
                miss += 1
                if miss == 5:
                    break

        self.ut_page.setText("转换成功：" + str(success) + "页 转换失败：" + str(fail) + "页")
        if success > 0:
            self.app = id
            self.key1 = key1
            self.key2 = key2
            try:
                f = open(self.keyfile, 'w')
                f.write(id + '@@' + key1 + '@@' + key2 + '@@')
                f.close()
            except Exception as e:
                print(e)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())
