def kira_Isipadu_piramid(sisi,tinggi):
     isipadu_piramid = (1/3) * (sisi*sisi) * tinggi
     return (isipadu_piramid)

print ("Kira isi padu piramid")
sisi = int(input("Masukkan ukuran sisi tapak piramid"))
tinggi = int(input("Masukkan tinggi piramid:"))

print ("Isi padu piramid =", kira_Isipadu_piramid(sisi,tinggi))