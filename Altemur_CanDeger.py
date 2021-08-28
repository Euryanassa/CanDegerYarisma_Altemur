import pywhatkit as py
import pandas as pd

# Datamızı, pandas kütüphanesi yardımıyla okuttuk
df=pd.read_csv("TelNo.csv")
# Verilerimizi saat ve dakika datasını baz alarak sıraladık
# Çünkü döngümüz sırayla okuyup, mesajlarımızı atacak
# Ay ve gün ekleme sebebim ise, saat datasına göre sıralama yapınca en küçük sayıyı alıyordu.
# Ben de sırama gün ekledim. Bu sefer ay sonları halletmem gerektiğinden, ay datası da 
# eklemenin gerekli olduğunu düşündüm 
df_siralanmis=df.sort_values(by=['Ay','Gun','Saat','Dakika'])

# For loopunda kullanılmak üzere satır uzunluğumuzun datasını aldık
Satir,Sutun=df.shape

# Sıralanan Datamızı, sırasıyla mesaj atma aşamasına getirdik
for i in range(Satir):
    # İlk satırımızı bu if'de yolladık
    if i==0:
        py.sendwhatmsg(f"+"+str(df["Telefon No"][i]),str(df["Mesaj"][i]),int(df["Saat"][i]),int(df["Dakika"][i]))
        
        # Bilgilendirme aşaması: 
        print(str(df["Telefon No"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))
    
    # Eğer gün ve dakika verisi birbirine eşit değilse, mesajımızı girilen saate göre yolluyoruz
    elif (int(df["Dakika"][i])!=int(df["Dakika"][i-1]) and int(df["Saat"][i-1])!=int(df["Saat"][i-1])):
        py.sendwhatmsg(f"+"+str(df["Telefon No"][i]),str(df["Mesaj"][i]),int(df["Saat"][i]),int(df["Dakika"][i]))
        
        # Bilgilendirme aşaması:  
        print(str(df["Telefon No"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))

    # Eğer gün ve dakikalarımız üstü üste binmişse, mesajımızı direkt gönderiyoruz. çünkü zamanı geldiğinden
    # dolayı bir satır üstteki mesajı yolladıysa, deiğer mesaj otomatikmen 24 saat sonraya zamanlanıyor.
    # Bu şekilde bu hatanın önüne geçmiş oluyoruz
    else:
        py.sendwhatmsg_instantly(f"+"+str(df["Telefon No"][i]),str(df["Mesaj"][i]))
        
        #Bilgilendirme Aşaması
        print(str(df["Telefon No"][i],"Telefon Numaralı Kişiye",str(df["Mesaj"][i]),"Mesajınız Gönderildi"))

print("Mesaj Gönderim İşlemleriniz, Başarıyla Tamamlanmıştır\n Saygılarımla,\nAltemur Çelikayar")



