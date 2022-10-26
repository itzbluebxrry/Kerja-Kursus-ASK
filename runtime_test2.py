def kira_purata(x,y):
     purata = jumlah / bilangan
     return(purata)

senaraiNo = []
cont = True
while cont:
     try:
          nom = float(input("Masukkan nombor [X untuk berhenti]: "))
     except ValueError:
          cont = False

bilangan = len(senaraiNo)
jumlah = sum(senaraiNo)

if bilangan > 0:
     jumlah = sum(senaraiNo)
     print ("Purata = ",str(kira_purata(jumlah,bilangan)))
print ("Tamat.")