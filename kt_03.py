#Kodutöö 03
#Erki Rehkli ITT20
#26.02.2021

from datetime import *
#3.5 Tahvli juurde

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
vastajad = []

for rida in fail:
    vastajad.append(rida)
fail.close()

kuupaev = datetime.now().day
print("Vastama tuleb: "+vastajad[kuupaev-1])


##############################################

#3.4 Jukebox

failid = input("eesti_muusika.txt\n jukebox.txt\n 80ndad.txt\n edm.txt\n Palun sisestage failinimi: ")

fail = open(failid, encoding="UTF-8")
laulud= []
i = 1
for rida in fail:
    laulud.append(rida)
    jrk = str(i)+"."+rida
    print(jrk, end="")
    i +=1
fail.close()

laul = int(input("\n Mitmendat laulu soovite?: "))
print(laulud[laul-1])


##############################################

#3.3 Sissetulekud

fail= open("konto.txt", encoding="UTF-8")
sissetulek = []
for rida in fail:
    if float(rida) > 0:
        sissetulek.append(float(rida))
fail.close()
for posArv in sissetulek:
    print(posArv)
    

##############################################

#3.2 Jänesevanemate muer ver.3

ringid = int(input("Sisesta ringide arv: "))
summa = 0
for i in range(1, ringid+1):
    if i%2==0:
        summa += i
    
print("Porgandite koguarv on",summa)

##############################################

#3.1 Ülikooli vastuvõetud

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
 vastuvõetud.append(int(rida))
fail.close()

aasta= int(input("Sisesta aasta, mille kohta infot soovid: "))
aastad=[2011,2012,2013,2014,2015,2016,2017,2018,2019]
rebaseid = vastuvõetud[aastad.index(aasta)]
print(str(aasta)+". aastal oli rebaseid", rebaseid)