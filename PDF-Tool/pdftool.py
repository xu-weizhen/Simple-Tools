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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 409)
        self.ub_cut = QtWidgets.QPushButton(Form)
        self.ub_cut.setGeometry(QtCore.QRect(50, 170, 101, 51))
        self.ub_cut.setObjectName("ub_cut")
        self.ub_pdf2pic = QtWidgets.QPushButton(Form)
        self.ub_pdf2pic.setGeometry(QtCore.QRect(200, 170, 101, 51))
        self.ub_pdf2pic.setObjectName("ub_pdf2pic")
        self.ub_pdf2word = QtWidgets.QPushButton(Form)
        self.ub_pdf2word.setGeometry(QtCore.QRect(350, 170, 101, 51))
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
        self.ub_pdf2pic.raise_()
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

        self.filename = ''
        self.filepath = ''
        self.page = -1

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #槽函数
        self.ub_choose.clicked.connect(self.f_choose)
        self.ub_cut.clicked.connect(self.f_cut)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF转换工具"))
        self.ub_cut.setText(_translate("Form", "分割PDF"))
        self.ub_pdf2pic.setText(_translate("Form", "PDF转图片"))
        self.ub_pdf2word.setText(_translate("Form", "PDF转文字"))
        self.ub_pic2word.setText(_translate("Form", "图片转文字"))
        self.ul_filename.setText(_translate("Form", "请选择PDF文件"))
        self.ul_page.setText(_translate("Form", "选择页码"))
        self.ul_id.setText(_translate("Form", "ID"))
        self.ul_key1.setText(_translate("Form", "KEY1"))
        self.ul_key2.setText(_translate("Form", "KEY2"))
        self.ub_folder.setText(_translate("Form", "图片文件夹"))
        self.ub_choose.setText(_translate("Form", "选择PDF"))

    # 打开文件
    def f_choose(self):
        new_filename, file_type = QtWidgets.QFileDialog.getOpenFileName(None,"打开文件","./","PDF文件 (*.pdf *.PDF);;所有文件 (*)")
        if new_filename != '':
            self.filepath = new_filename
            print(self.filepath)
            count = len(new_filename)-1
            while count>0:
                if new_filename[count]=='/':
                    break
                count = count-1
                
            self.filename = new_filename[count+1:]
            if len(self.filename) >25:
                self.filename = self.filename[0:25]+"..."
            self.ul_filename.setText(self.filename)

            openpdf = open(self.filepath,'rb')
            pdfFileReader = PdfFileReader(openpdf)
            pageCount = pdfFileReader.getNumPages()
            openpdf.close()
            self.page = pageCount

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

    # 分割文件
    def f_cut(self):
        if self.page == -1:
            cutpage = self.ut_page.toPlainText()
            msg = "请先选择文件 " + cutpage
            self.ut_page.setText(msg)
        else:
            cutpage = self.ut_page.toPlainText()
            if cutpage == '' or cutpage == "请在此输入需要分割出的页面":
                self.ut_page.setText("请在此输入需要分割出的页面")
            else:
                pagelist=[]
                i = 0
                j = 1
                to = False
                error = False
                while j<len(cutpage) and not error:
                    if cutpage[j] ==',' or cutpage[j] == '，':
                        if to:
                            p2 = int(cutpage[i:j])
                            if p1 <= p2:
                                while p1 != p2:
                                    pagelist.append(p1)
                                    p1 = p1+1
                                pagelist.append(p2)
                                to = False
                                i = j+1
                                j = j+2
                            else:
                                error = True
                        else:
                            pagelist.append(int(cutpage[i:j]))
                            i = j+1
                            j = j+2
                    else:
                        if cutpage[j] =='-':
                            to = True
                            p1=int(cutpage[i:j])
                            i = j+1
                            j = j+2
                        else:
                            j = j+1

                if not error:
                    if to:
                        p2 = int(cutpage[i:j])
                        if p1 <= p2:
                            while p1 != p2:
                                pagelist.append(p1)
                                p1 = p1+1
                            pagelist.append(p2)
                        else:
                            error = True
                    else:
                        pagelist.append(int(cutpage[i:j]))

                if error:
                    msg = "输入页码有误 " + cutpage
                    self.ut_page.setText(msg)

                if not error:
                    for k in pagelist:
                        if k > self.page:
                            error = True
                            msg = "该文件最大页码为" + str(self.page) + " " + cutpage
                            self.ut_page.setText(msg)

                if not error:
                    pdf_output = PdfFileWriter()
                    pdf_input = PdfFileReader(open(self.filepath, 'rb'))
                    for i in pagelist:
                        pdf_output.addPage(pdf_input.getPage(i - 1))
                    pdf_output.write(open("out.pdf", 'wb'))
                    self.ut_page.setText("分割完成")

        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())
