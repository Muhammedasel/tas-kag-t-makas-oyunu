
import random

taşkağıtmakas = ["taş", "kağıt", "makas"]

taş = taşkağıtmakas[0]
kağıt = taşkağıtmakas[1]
makas = taşkağıtmakas[2]
i = 0
computer = 0
player = 0
btaş= 0
bkağıt = 0
bmakas = 0
oyuncuismi = input("Lütfen oyuncu adınızı giriniz = ")

def sonuçları_göster():
    if (computer > player):
        print("{} - {} computer kazanıyor.".format(computer, player))
        print("""BİLGİSAYAR     {} = TAŞ
                            {} = KAĞIT
                            {} = MAKAS

                    SEÇTİ.""".format(btaş ,bkağıt ,bmakas))
    elif (player > computer):
        print("{} {} {} kazanıyor.".format(player, computer, oyuncuismi))
        print("""BİLGİSAYAR     {} = TAŞ
                            {} = KAĞIT
                            {} = MAKAS

                    SEÇTİ.""".format(btaş ,bkağıt ,bmakas))
    else:
        print("Computer ve {} {} {} berabere".format(oyuncuismi ,computer ,player))
        print("""BİLGİSAYAR     {} = TAŞ
                            {} = KAĞIT
                            {} = MAKAS

                    SEÇTİ.""".format(btaş ,bkağıt ,bmakas))

while True:
    devammı = input("oyuna DEVAM etmek için 1 e ÇIKMAK için q ya SONUÇLAR için 2 ye basın.")

    if (devammı == "1"):

        gir = input(" taş mı kağıt mı makas mı ")

        a = random.choice(taşkağıtmakas)

        print("bilgisayar {} seçti..".format(a))

        if (gir == taş):

            if (gir == a):
                print("berabere. puan alamadınız")
                btaş +=1
            elif (a == kağıt):
                print("kaybettiniz. kağıt taşı sarar.")
                bkağıt +=1
                computer += 1
            elif (a == makas):
                print("kazandınız. taş makası kırar.")
                bmakas += 1
                player += 1

        elif (gir == kağıt):

            if (a == gir):
                print("berabere. puan alamadınız.")
                bkağıt+=1
            elif (a == taş):
                print("kazandınız. kağıt taşı sarar.")
                player += 1
                btaş +=1
            elif (a == makas):
                print("kaybettiniz. makas kağıdı keser.")
                bmakas +=1
                computer += 1

        elif (gir == makas):

            if (a == gir):
                print("berabere. puan alamadınız.")
                bmakas +=1
            elif (a == taş):
                print("kaybettiniz. taş makası kırar.")
                btaş +=1
                computer += 1
            elif (a == kağıt):
                print("kazandınız. makas kağıdı keser.")
                bkağıt +=1
                player += 1
        else:
            print("geçersiz işlem")

    elif (devammı == "2"):
        sonuçları_göster()

    elif (devammı == "q"):
        print("tekrar bekleriz. sonuçlar birazdan açıklanıyor..")
        break
    else:
        print("geçersiz işlem")
        break

print("""

    ****************
    SONUÇLAR

    ****************

    BİLGİSAYAR = {}
    {} = {}

    BİLGİSAYAR {} = TAŞ
               {} = KAĞIT
               {} = MAKAS

                    SEÇTİ.

""".format(computer, oyuncuismi, player ,btaş ,bkağıt ,bmakas))
