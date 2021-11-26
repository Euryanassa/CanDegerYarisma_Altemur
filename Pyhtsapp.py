from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile
from PythonMessage import WhatMsg
import webbrowser
import keyboard
import time
import qdarkstyle

# Arayüz Kodu

class Ui_WP_AutoSender_by_Altemur_v1_3_1(object):
    def setupUi(self, WP_AutoSender_by_Altemur_v1_3_1):
        # Programımızın adı
        WP_AutoSender_by_Altemur_v1_3_1.setObjectName("WP_AutoSender_by_Altemur_v1_3_1")
        # Pencere boyutu
        WP_AutoSender_by_Altemur_v1_3_1.resize(574, 461)
        # setup stylesheet
        WP_AutoSender_by_Altemur_v1_3_1.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # or in new API
        WP_AutoSender_by_Altemur_v1_3_1.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        
        # Butonun işlevini girdik
        self.EmptyFormat = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("EmptyFormat"))
        # Buton başlangıç koordinatları ve boyutu
        self.EmptyFormat.setGeometry(QtCore.QRect(50, 30, 231, 51))
        # Butonun temsili ismi
        self.EmptyFormat.setObjectName("EmptyFormat")

        # create the application and the main window
        # app = QtWidgets.QApplication(sys.argv)
        # window = QtWidgets.QMainWindow()

        # Butonun işlevini girdik
        self.Gonder = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("Gonder"))
        # Buton başlangıç koordinatları ve boyutu
        self.Gonder.setGeometry(QtCore.QRect(50, 90, 231, 51))
        # Butonun temsili ismi
        self.Gonder.setObjectName("Gonder")

        # Butonun işlevini girdik
        self.DGKO = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("DGKO"))
        # Buton başlangıç koordinatları ve boyutu
        self.DGKO.setGeometry(QtCore.QRect(350, 400, 171, 31))
        # Butonun temsili ismi
        self.DGKO.setObjectName("DGKO")

        # Output çıktısını veren paneli tanımladık
        self.Output = QtWidgets.QLabel(WP_AutoSender_by_Altemur_v1_3_1)
        # Etiketin boyutu
        self.Output.setGeometry(QtCore.QRect(50, 150, 471, 51))
        # Çıkarılan yazının boyutu ve sitili
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Output.setFont(font)
        # Panelin görünüşü ve sitili
        self.Output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # Panelin temsili
        self.Output.setObjectName("Output")

        # Butonun işlevini girdik
        self.UploadExcell = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("UploadExcell"))
        # Buton başlangıç koordinatları ve boyutu
        self.UploadExcell.setGeometry(QtCore.QRect(290, 30, 231, 51))
        # Butonun temsili ismi
        self.UploadExcell.setObjectName("UploadExcell")

        # Butonun işlevini girdik
        self.Temizle = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("Temizle"))
        # Buton başlangıç koordinatları ve boyutu
        self.Temizle.setGeometry(QtCore.QRect(290, 90, 231, 51))
        # Butonun temsili ismi
        self.Temizle.setObjectName("Temizle")

        # Text girilen yerin tanımı
        self.Telefon = QtWidgets.QPlainTextEdit(WP_AutoSender_by_Altemur_v1_3_1)
        # Text girilen yerin boyutu ve koordinatları
        self.Telefon.setGeometry(QtCore.QRect(50, 210, 471, 31))
        # Yazımdan önce görülecek uyarı yazısı
        self.Telefon.setPlaceholderText("5xxxxxxxxx Olarak Numara Giriniz")
        # O bölgenin temsili ismi
        self.Telefon.setObjectName("Telefon")

        # Spin kutusu(Dakika İçin) tanımladık
        self.DK = QtWidgets.QSpinBox(WP_AutoSender_by_Altemur_v1_3_1)
        # Spin kutusu boyutu ve koordinatları
        self.DK.setGeometry(QtCore.QRect(290, 400, 51, 31))
        # Spin kutusuna girilebilecek minimum değer
        self.DK.setMinimum(0)
        # Spin kutusuna girilebilecek maksimum değer
        self.DK.setMaximum(59)
        # Spin kutusunun temisi ismi
        self.DK.setObjectName("DK")

        # Spin kutusu(Saat İçin) tanımladık
        self.SAAT = QtWidgets.QSpinBox(WP_AutoSender_by_Altemur_v1_3_1)
        # Spin kutusu boyutu ve koordinatları
        self.SAAT.setGeometry(QtCore.QRect(230, 400, 51, 31))
        # Spin kutusuna girilebilecek maksimum değer
        self.SAAT.setMaximum(24)
        # Spin kutusunun temisi ismi
        self.SAAT.setObjectName("SAAT")

        # Text kutusnu tanımladık (Mesaj için)
        self.Mesaj = QtWidgets.QPlainTextEdit(WP_AutoSender_by_Altemur_v1_3_1)
        # Text kutusunun boyutu ve koordinatları
        self.Mesaj.setGeometry(QtCore.QRect(50, 250, 471, 141))
        # İçiresinde bulunan kaybolan mesajımızı girdik ve bendenizin ismi.
        # Mokoçino kokoçino şekilli şukullu şekilde
        self.Mesaj.setPlaceholderText("""Lütfen mesajınızı buraya yazınız.
Aynı zamanda mesaj göndermek istiyorsanız, lütfen excell ile giridiyi giriniz.
Written by,
██████████████████████████████████████████████
██▀▄─██▄─▄███─▄─▄─█▄─▄▄─█▄─▀█▀─▄█▄─██─▄█▄─▄▄▀█
██─▀─███─██▀███─████─▄█▀██─█▄█─███─██─███─▄─▄█
█▄▄█▄▄█▄▄▄▄▄██▄▄▄██▄▄▄▄▄█▄▄▄█▄▄▄██▄▄▄▄██▄▄█▄▄█
        """)
        # Objemizin temsili ismi
        self.Mesaj.setObjectName("Mesaj")

        # Butonun işlevini girdik
        self.Supra = QtWidgets.QPushButton(WP_AutoSender_by_Altemur_v1_3_1, clicked = lambda: self.PressButton("Supra"))
        # Butonun boyutu ve koordinatları
        self.Supra.setGeometry(QtCore.QRect(50, 400, 171, 31))
        # SUPRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA temsili ismi
        self.Supra.setObjectName("Supra")
#--------------------------------------------------------------------------------------------------
        # pencere parametreleri
        self.retranslateUi(WP_AutoSender_by_Altemur_v1_3_1)
        QtCore.QMetaObject.connectSlotsByName(WP_AutoSender_by_Altemur_v1_3_1)

    # Butonlara basınca çalışacaklar ve işlevleri
    def PressButton(self,pressed):
        if pressed == "EmptyFormat":
            WhatMsg.DownloadExcell(),self.Output.setText("Dosya İndirildi") 

        if pressed == "UploadExcell":
            try:WhatMsg.UploadExcell(),self.Output.setText("Dosya Yüklü")
            except:self.Output.setText("Dosya Bulunamadı")

        if pressed == 'Gonder':
            Checker = os.path.isfile('MesajExcel.xlsx')
            if Checker == True:WhatMsg.ThreadSendMsg(WhatMsg.SendMsg),self.Output.setText("Yollanıyor... Lütfen Bir Tuşa Basmayınız")
            else:self.Output.setText("Öncelikle Dosyayı Yükleyiniz")
            
        if pressed == "Temizle":
            try:
                WhatMsg.delete_file()
                self.Output.setText("Silme İşlemi Tamamlandı")
            except: self.Output.setText("Dosyanız Bulunmadığından, Silinemedi")
        if pressed == "DGKO":
            try:
                WhatMsg.ThreadSendMsg(WhatMsg.SendOne,[self.Telefon.toPlainText(),self.Mesaj.toPlainText(),self.SAAT.text(),self.DK.text()])
                self.Output.setText("Mesaj {}:{} Saatinde Gönderiliyor".format(self.SAAT.text(),self.DK.text()))
            except:self.Output.setText("Geçersiz Input")
        if pressed == "Supra":
            self.Output.setText("SUUUUUUUUUUUUPRAAAAAAAAAAAAAA")
            webbrowser.open_new("https://www.youtube.com/watch?v=b8gq88TTCzU")

    # Butonların görünen isimleri ve pencere isimleri
    def retranslateUi(self, WP_AutoSender_by_Altemur_v1_3_1):
        _translate = QtCore.QCoreApplication.translate
        WP_AutoSender_by_Altemur_v1_3_1.setWindowTitle(_translate("WP_AutoSender_by_Altemur_v1_3_1", "WP_AutoSender_by_Altemur_v1_3_1"))
        self.EmptyFormat.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "Excell Format Dosyası"))
        self.Gonder.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "Listedekilere Mesajı Gönder"))
        self.DGKO.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "Doğum Günü Mesajı Gönder"))
        self.UploadExcell.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "Excell Dosyası Kontrol"))
        self.Temizle.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "Listeyi Tezmile"))
        self.Supra.setText(_translate("WP_AutoSender_by_Altemur_v1_3_1", "SUPRAA!"))
        

import pywhatkit as py
import pandas as pd
import os
import threading

# Mesaj gönderme classımız
class WhatMsg():
    # Kodumuz içinde kullandığımız objelerimiz
    def __init__(self,Phone,Message,Year, Month, Day, Hour, Min):
        self.Phone = Phone
        self.Message = Message
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.Hour = Hour
        self.Min = Min

    # Excell indirme fonksiyonu
    def DownloadExcell():
        # pandas ile bir dataframe oluşturuyoruz ve excell'e yazdırıyoruz
        df = pd.DataFrame([["5554443322 (0'sız)","Örnek Satırıdır, Silmeyiniz","2021","12","31","24","59"]],
                          columns=['Telefon','Mesaj','Yıl','Ay','Gün','Saat','Dakika'])
        # Excell oluşturma kodu
        df.to_excel('MesajExcel.xlsx', index = False)
        # Excel'i düzenlememiz için önümüze açılan komut 
        os.system('start excel.exe MesajExcel.xlsx')
        
    # Excell'i upload ediyoruz
    def UploadExcell():
        # Excell dosyasını okuma ve pandasa dökme komutumuz
        df = pd.read_excel('MesajExcel.xlsx')
        return df

    def SendMsg():
        # Verilerimizi saat ve dakika datasını baz alarak sıraladık
        # Çünkü döngümüz sırayla okuyup, mesajlarımızı atacak
        # Ay ve gün ekleme sebebim ise, saat datasına göre sıralama yapınca en küçük sayıyı alıyordu.
        # Ben de sırama gün ekledim. Bu sefer ay sonları halletmem gerektiğinden, ay datası da 
        # eklemenin gerekli olduğunu düşündüm
        df = WhatMsg.UploadExcell()


        # For loopunda kullanılmak üzere satır uzunluğumuzun datasını aldık
        Satir,Sutun=df.shape

        # Sıralanan Datamızı, sırasıyla mesaj atma aşamasına getirdik
        if Satir>1:
            for i in range(Satir):
                # İlk satırımızı bu if'de yolladık
                if i==1:
                    py.sendwhatmsg(f"+90"+str(df["Telefon"][i]),str(df["Mesaj"][i]),int(df["Saat"][i]),int(df["Dakika"][i]))
                    WhatMsg.TabCloser()
                    
                    # Bilgilendirme aşaması: 
                    # print(str(df["Telefon"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))
                    
                
                # Eğer gün ve dakika verisi birbirine eşit değilse, mesajımızı girilen saate göre yolluyoruz
                elif i>1:
                    if (int(df["Dakika"][i])!=int(df["Dakika"][i-1]) and int(df["Saat"][i-1])!=int(df["Saat"][i-1])):
                        py.sendwhatmsg(f"+90"+str(df["Telefon No"][i]),str(df["Mesaj"][i]),int(df["Saat"][i]),int(df["Dakika"][i]))
                        WhatMsg.TabCloser()
                        
                        # Bilgilendirme aşaması:  
                        # print(str(df["Telefon"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))
                    # Eğer gün ve dakikalarımız üstü üste binmişse, mesajımızı direkt gönderiyoruz. çünkü zamanı geldiğinden
                    # dolayı bir satır üstteki mesajı yolladıysa, deiğer mesaj otomatikmen 24 saat sonraya zamanlanıyor.
                    # Bu şekilde bu hatanın önüne geçmiş oluyoruz
                    elif int(df["Dakika"][i])==int(df["Dakika"][i-1]) and int(df["Saat"][i])==int(df["Saat"][i-1]):
                        py.sendwhatmsg_instantly(f"+90"+str(df["Telefon"][i]),str(df["Mesaj"][i]))
                        WhatMsg.TabCloser()
                        
                        #Bilgilendirme Aşaması
                        # print(str(df["Telefon"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))
        else:pass

    def TabCloser():
        time.sleep(6)
        keyboard.press_and_release('ctrl+w')
        time.sleep(2)
        keyboard.press_and_release('enter')

    # Kodumuzu bir kişiye gönderme foksiyonumuz
    def SendOne(P,M,H,S):
        py.sendwhatmsg(f"+90"+P,M,int(H),int(S))
        WhatMsg.TabCloser()

    # Multi işlem yapmak adına threading kullnaıyoruz
    def ThreadSendMsg(input_Func,args=None):
        if args != None:
            t = threading.Thread(target=input_Func,args=args)
        else:
            t = threading.Thread(target=input_Func)
        t.start()
        #print("Mesaj Gönderim İşlemleriniz, Başarıyla Tamamlanmıştır\n Saygılarımla,\nAltemur Çelikayar")

    # Excell dosyasını silme komutumuz
    def delete_file():
        os.remove("MesajExcel.xlsx")

    # Pandas dataframeini temizler
    def ClearList(df = None):
        # Tüm verilerimiz temizlenir
        df=None
        return df


# WhatMsg.DownloadExcell()
# WhatMsg.SendMsg()

# MAIN

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WP_AutoSender_by_Altemur_v1_3_1 = QtWidgets.QWidget()
    ui = Ui_WP_AutoSender_by_Altemur_v1_3_1()
    ui.setupUi(WP_AutoSender_by_Altemur_v1_3_1)
    WP_AutoSender_by_Altemur_v1_3_1.show()
    sys.exit(app.exec_())
