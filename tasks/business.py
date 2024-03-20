
import random
import sys
import time
import os

money = float()
money = 300.0
bankacc = float()
bankacc = 0.0
increasebuy = 1.0
increasebuy = float()
increasesell = 1.0
increasesell = float()





properties = {
'pen' : 0,
'usb' : 0,
'keyboard' : 0,
'harddrive' : 0,
'computer' : 0,
'cars' : 0,
}
pricesbuy = {
'penP' : round(2.0,2),
'usbP' : round(5.0,2),
'keyboardP' : round(70.0,2),
'harddriveP' : round(130.0,2),
'computerP' : round(250.0,2),
'carsP' : round(500.0,2),
}
pricessell = {
'penP' : round(2.0,2),
'usbP' : round(5.0,2),
'keyboardP' : round(70.0,2),
'harddriveP' : round(130.0,2),
'computerP' : round(250.0,2),
'carsP' : round(500.0,2),
}
def Event():
    global money
    os.system('Cls')
    if money > 0:
        charge = float()
        charge = random.choice([0.2 * money,0.25 * money,0.15*money,0.5*money,0.3*money,0.4*money,0.35*money,0.02 * money,0.05*money,0.09*money])
        text1 = "placisz mandat wynoszacy :" + str(charge)
        text2 = "zrobiles wspaniale zakupy,placisz " + str(charge)
        text3 = "za przejazd placisz " + str(charge)
        text4 = "kupiles po drodze pamiatki, placisz " + str(charge)
        text5 = "odwiedziles okoliczne atrakcje turystyczne,\n placisz "+str(charge)
        text6 = "za nocleg w hotelu placisz "+str(charge)
        text7 = "dostales spadek od babci,\n otrzymujesz "+str(charge)
        text8 = "nocowales u rodziny, zaoszczedziles pieniadze,\n otrzymujesz "+str(charge)
        text9 = "kolega oferuje ci darmowy przejazd samolotem w zamian \n w zamian za pomoc dawno temu \n nic nie tracisz"
        textt = random.choice([text1,text2,text3,text4,text5,text6,text7,text8,text9])
        if textt == 7 or textt == 8:
            print(textt)
            money += charge
            time.sleep(2)
            Play()
        elif textt == text9:
            print(text9)
            time.sleep(2)
            Play()
        elif textt == text1 or textt == text2 or textt == text3 or textt == text4 or textt == text5 or textt == text6:
            print(textt)
            money -= charge
            time.sleep(2)
            Play()


        
def IncPrice():
    global increasebuy, increasesell
   
    increasesell = random.choice([1.0,1.25,1.20,1.5,0.5,0.8,0.9])
    increasebuy  = random.choice([1.0,1.25,1.20,1.5,0.5,0.8,0.9])
    pricessell['penP'] *= increasesell
    pricessell['usbP'] *= increasesell
    pricessell['keyboardP'] *= increasesell
    pricessell['harddriveP'] *= increasesell
    pricessell['computerP'] *= increasesell
    pricessell['carsP'] *= increasesell

    pricesbuy['penP'] *= increasebuy
    pricesbuy['usbP'] *= increasebuy
    pricesbuy['keyboardP'] *= increasebuy
    pricesbuy['harddriveP'] *= increasebuy
    pricesbuy['computerP'] *= increasebuy
    pricesbuy['carsP'] *= increasebuy





        
def Keyy():
    guichoice = int(input("Wpisz wartosc 1 - 7\n"))
    if guichoice == 1:
        Info()
    elif guichoice == 2:
        Bank()
    elif guichoice == 3:
        Buy()
    elif guichoice == 4:
        Sell()
    elif guichoice == 5:
        sys.exit()
    elif guichoice == 6:
        Equipment()
    elif guichoice == 7:
        IncPrice()
        Event()
        Play()
    elif guichoice >= 8:
        Keyy
   
   
def Owned():
    print("posiadane "+str(properties["pen"])+"  dlugopisy               "+str(properties["usb"])+"  USB")
    print("posiadane "+str(properties["harddrive"])+" dysk                  "+str(properties["keyboard"])+" klawiatury")
    print("posiadane "+str(properties["computer"])+" komputery           "+str(properties["cars"])+"  samochody")
    
def Play():
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    
    print("            ██████╗░██╗░░░██╗░██████╗██╗███╗░░██╗███████╗░██████╗░██████╗")
    print("            ██╔══██╗██║░░░██║██╔════╝██║████╗░██║██╔════╝██╔════╝██╔════╝")
    print("            ██████╦╝██║░░░██║╚█████╗░██║██╔██╗██║█████╗░░╚█████╗░╚█████╗░")
    print("            ██╔══██╗██║░░░██║░╚═══██╗██║██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗")
    print("            ██████╦╝╚██████╔╝██████╔╝██║██║░╚███║███████╗██████╔╝██████╔╝")
    print("            ╚═════╝░░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░")                                                                        
    print("    money    -- ",round(money,2))
    print("    bank account -- ",round(bankacc,2))
    print("                  [1] - INFO               ")
    print("                  [2] - BANK               ")
    print("                  [3] - KUP                ")
    print("                  [4] - SPRZEDAJ           ")
    print("                  [5] - WYJDZ              ")
    print("                  [6] - EKWIPUNEK          ")
    print("                  [7] - WYLOT              ")
    print("                                                                                      ")
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░")
    Keyy()

def Info():
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")     
    print("            ██╗███╗░░██╗███████╗░█████╗░")
    print("            ██║████╗░██║██╔════╝██╔══██╗")
    print("            ██║██╔██╗██║█████╗░░██║░░██║")
    print("            ██║██║╚████║██╔══╝░░██║░░██║")
    print("            ██║██║░╚███║██║░░░░░╚█████╔╝")
    print("            ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░")  
    print("                                                                                     ")
    print("    wpisz liczby w nawiasach kwadratowych aby dostac sie do okreslonych miejsc       ")
    print("                       kupuj i sprzedawaj produkty aby sie wzbogacic                 ")
    print("               wplacaj pieniadze do banku aby nie straci ich w czasie gry            ")
    print("                                                                                     ")
    print("                            [1] - POWROT DO MENU GLOWNEGO                            ")
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")  
    infochoice = int(input())
    if infochoice == 1:
        Play()


def Bank():
    global bankacc,money
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")     
   
    print("            ██████╗░░█████╗░███╗░░██╗██╗░░██╗")
    print("            ██╔══██╗██╔══██╗████╗░██║██║░██╔╝")
    print("            ██████╦╝███████║██╔██╗██║█████═╝░")
    print("            ██╔══██╗██╔══██║██║╚████║██╔═██╗░")
    print("            ██████╦╝██║░░██║██║░╚███║██║░╚██╗")
    print("            ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝")
    print("                                                                                     ")
    print("    money    -- ",round(money,2))
    print("bank account -- ",round(bankacc,2))
    print("       [1]   WPLAC   ")
    print("       [2]   WYPLAC  ")
    print("       [3]   POWROT DO MENU GLOWNEGO")
    print("                                                                                     ")
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    bankchoice = int(input("Wybierz numer\n"))
    if bankchoice == 3:
        Play()
    banknumber = float(input("Ile chcesz wplacic/wyplacic\n"))
    if bankchoice == 1:
        if money >= banknumber:
            money -= banknumber
            bankacc += banknumber
            Play()
        else: 
            print("Nie masz wystarczajaco pieniedzy")
            Play()
    elif bankchoice == 2:
        if bankacc >= banknumber:
            if bankacc >= banknumber:
                money += banknumber
                bankacc -= banknumber
                Play()
        else:  
            print("Nie masz wystarczajaco pieniedzy")
            Play()
    elif bankchoice >= 3:
        print("Podaj numer 1 - 3")
        Bank()




def Equipment():
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    print("            ██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░░░██╗")
    print("            ██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝")
    print("            ██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░")
    print("            ██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░")
    print("            ██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░")
    print("            ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░")
    print("dlugopis -- "+str(properties["pen"]))
    print("USB -- "+str(properties["usb"]))
    print("dysk -- "+str(properties["harddrive"]))
    print("klawiatura -- "+str(properties["keyboard"]))
    print("komputer -- "+str(properties["computer"]))
    print("samochody -- "+str(properties["cars"]))
    print("[1] - PRZEJDZ DO MENU GLOWNEGO")
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    equichoice = int(input())
    if equichoice == 1:
        Play()
    else: Equipment()
        
def Sell():
    global money
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ CO CHCESZ SPRZEDAC?▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    print("            ░██████╗░█████╗░██╗░░░░░███████╗")
    print("            ██╔════╝██╔══██╗██║░░░░░██╔════╝")
    print("            ╚█████╗░███████║██║░░░░░█████╗░░")
    print("            ░╚═══██╗██╔══██║██║░░░░░██╔══╝░░")
    print("            ██████╔╝██║░░██║███████╗███████╗")
    print("            ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝")
    print("money -- "+str(round(money)))
    print("bank -- "+str(round(bankacc)))
    print("                         [1]DLUGOPIS                      CENA -- "+str(round(pricessell["penP"],2))+"                ")
    print("                         [2]USB                           CENA -- "+str(round(pricessell["usbP"],2))+"                ")
    print("                         [3]DYSK                          CENA -- "+str(round(pricessell["harddriveP"],2))+"                ")
    print("                         [4]KLAWIATURA                    CENA -- "+str(round(pricessell["keyboardP"],2))+"                ")
    print("                         [5]KOMPUTER                      CENA -- "+str(round(pricessell["computerP"],2))+"                ")
    print("                         [6]SAMOCHOD                      CENA -- "+str(round(pricessell["carsP"],2))+"                ")
    print("                         [7]MENU GLOWNE")
    Owned()
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 

    thing = int(input("Podaj przedmiot\n"))
    if thing == 7:
        Play()
    if thing == 1:
        thing = 'pen'
    if thing == 2:
        thing = 'usb'
    if thing == 3:
        thing = 'harddrive'
    if thing == 4:
        thing = 'keyboard'
    if thing == 5:
        thing = 'computer'
    if thing == 6:
        thing = 'cars'
    number = int(input("Podaj ilosc ktora chcesz sprzedac"))
    print(thing)
    cost = properties[thing] * pricessell[str(thing)+"P"]
    if properties[thing] < number:
        print("Nie masz wystarczajaco przedmiotow")
        Sell()
    else :
        properties[thing] -= number
        money += cost
        thing = 0
        cost = 0
        Sell()


def Buy():
    global money
    os.system('Cls')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ CO CHCESZ KUPIC?  ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    
    print("            ██████╗░██╗░░░██╗██████╗░░█████╗░██╗░░██╗░█████╗░░██████╗███████╗")
    print("            ██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░██║██╔══██╗██╔════╝██╔════╝")
    print("            ██████╔╝██║░░░██║██████╔╝██║░░╚═╝███████║███████║╚█████╗░█████╗░░")
    print("            ██╔═══╝░██║░░░██║██╔══██╗██║░░██╗██╔══██║██╔══██║░╚═══██╗██╔══╝░░")
    print("            ██║░░░░░╚██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║██████╔╝███████╗")
    print("            ╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝")
    print("money -- "+str(money))
    print("bank -- "+str(bankacc))
    print("                         [1]DLUGOPIS                      CENA -- "+str(round(pricesbuy["penP"],2))+"                ")
    print("                         [2]USB                       CENA -- "+str(round(pricesbuy["usbP"],2))+"                ")
    print("                         [3]DYSK                        CENA -- "+str(round(pricesbuy["harddriveP"],2))+"                ")
    print("                         [4]KLAWIATURA                    CENA -- "+str(round(pricesbuy["keyboardP"],2))+"                ")
    print("                         [5]KOMPUTER                      CENA -- "+str(round(pricesbuy["computerP"],2))+"                ")
    print("                         [6]SAMOCHOD                      CENA -- "+str(round(pricesbuy["carsP"],2))+"                ")
    print("                         [7]MENU GLOWNE")
    Owned()
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ") 
    thing = int(input("Podaj przedmiot\n"))
    if thing == 7:
        Play()
    if thing == 1:
        thing = 'pen'
    if thing == 2:
        thing = 'usb'
    if thing == 3:
        thing = 'harddrive'
    if thing == 4:
        thing = 'keyboard'
    if thing == 5:
        thing = 'computer'
    if thing == 6:
        thing = 'cars'
    number = int(input("Podaj ilosc ktora chcesz kupic"))
    print(thing)
    cost =  pricesbuy[str(thing)+"P"] * number
    if money < cost:
        print("Nie masz wystarczajaco pieniedzy")
        Buy()
    else:
        properties[thing] += number
        money -= cost
        thing = 0
        cost = 0
        Buy()
Play()
        
        



    









  
