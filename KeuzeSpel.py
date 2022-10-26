import time
import random
import os





def intro():
    zak = []
    print("je maakt een wandeling in een bos\n")
    time.sleep(2)
    print("je hoort een raar geluid en ziet een lichtflits\n")
    time.sleep(2)
    print("na een paar seconde is alles weg en ben je niet meer in het bos\n")
    time.sleep(2)
    print("je bevind jezelf in een verlaten stad\n")
    time.sleep(2)
    print("de stad is helemaal mistig.\n")
    time.sleep(4)
    os.system('cls')
    print("Wat je kan zien zijn allemaal borden met 'GA WEG MONSTERS'\n")
    time.sleep(2)
    print( "Je wordt bang en vraagt je af waar die monsters zijn.\n")
    time.sleep(2)
    print("Je staat voor een huis.\n")
    time.sleep(2)
    print("Rechts van je is een steeg \n")
    time.sleep(2)
    print("Waar je iets van een radio hoort.\n")
    time.sleep(4)
    os.system('cls')
    begin(zak)


def begin(zak):
    if 'inhuis' in zak and 'insteeg' in zak:
        if 'medicijn' not in zak and 'verwond' in zak:
            print("je hebt beide monsters verslagen \n")
            time.sleep(2)
            print("je kan niet weg als je verwond bent\n")
            time.sleep(2)
            waar(zak)
        else:
            print("je hebt beide monsters verslagen\n")
            time.sleep(2)
            print("je hoort het geluid weer en ziet weer een lichtflits\n")
            time.sleep(2)
            print("je bent weer terug in het bos waar je eerst was\n")
            time.sleep(2)
            opnieuw()
    else:
        waar(zak)


def waar(zak):
    if 'pistool' in zak:
        print("je hebt een pistool en een mes in je zak\n")
        time.sleep(2)
    else:
        print("Je hebt een mes in je zak.\n")
        time.sleep(2)
    choice1 = input("1) ga in het huis.\n2) ga naar de steeg\n")
    if choice1 == '1':
        os.system('cls')
        huis(zak)
    elif choice1 == '2':
        os.system('cls')
        naarsteeg(zak)



def huis(zak):
    if 'inhuis' in zak:
        print("het monster ligt bewusteloos op de grond.\n")
        time.sleep(2)
        naarboven(zak)
    else:
        if 'pistool' in zak:
            print("Je hebt het huis betreden\n")
            time.sleep(2)
            print("Je komt in aanraking met het andere monster\n")
            time.sleep(2)
            print("het monster is klaar om je aan te vallen\n")
            time.sleep(2)
            choice2 = input("1) gebruik je mes \n2) gebuik het pistool\n")
            if choice2 == '2':
                print("je hebt met het moster gevochten en hebt het gedood\n")
                time.sleep(2)
                print(" met je pistool\n")
                time.sleep(2)
                print("je hebt je wel verwond in het gevecht\n")
                time.sleep(2)
                zak.append('verwond')
                zak.append('inhuis')
                naarboven(zak)
            elif choice2 == '1':
                mesinhuis(zak)
        elif 'pistool' not in zak:
            print("Je hebt het huis betreden\n")
            time.sleep(2)
            print("Je komt in aanraking met het andere monster\n")
            time.sleep(2)
            print("het monster is klaar om je aan te vallen\n")
            time.sleep(2)
            mesinhuis(zak)

def mesinhuis(zak):
    if 'pistool' not in zak:
        print("je hebt alleen een mes in dit gevecht\n")
        time.sleep(2)
    elif 'pistool' in zak:
        print("je kiest om te vechten met het mes\n")
        time.sleep(2)
    rand1 = ["0", "1"]
    rand1 = random.choice(rand1)
    if rand1 == '0':
        print("Jou mes had geen effect in dit gevecht\n")
        time.sleep(2)
        print("GAME OVER")
        opnieuw()
    elif rand1 == '1':
        print("je hebt gevochten met het monster\n")
        time.sleep(2)
        print("je hebt het net overleeft, maar je hebt het monster gedood\n")
        time.sleep(2)
        print("je hebt je wel verwond in het gevecht\n")
        time.sleep(2)
        zak.append('verwond')
        zak.append('inhuis')
        naarboven(zak)





def naarboven(zak):
    print("wat ga je doen?\n")
    time.sleep(2)
    choice3 = input("1) het huis verlaten\n2) naar boven om meer te zoeken\n")
    if choice3 == '1':
        print("je verlaat het huis\n")
        time.sleep(2)
        begin(zak)
    elif choice3 == '2':
        if 'medicijn' not in zak:
            print("je bent naar boven gegaan en vond medicijnen\n")
            time.sleep(2)
            print("je heb je verwondingen beter gemaakt\n")
            time.sleep(2)
            zak.append('medicijn')
            begin(zak)
        elif 'medicijn' in zak:
            print("je loopt naar boven maar je kan niks vinden\n")
            time.sleep(2)
            begin(zak)


def alley_choice(zak):
    choice4 = input("1) het monster aanvallen met je mes\n2) het monster beschieten met je pistool \n")
    if choice4 == '1':
        print("je hebt het monster vermoord met je mes\n")
        time.sleep(2)
        print("je kijkt naar het pistool\n")
        time.sleep(2)
        print("je kijkt of het pistool werkt en herladen is\n")
        time.sleep(2)
        zak.append('pistool')
        print("je gaat uit de steeg\n")
        time.sleep(2)
        zak.append('insteeg')
        begin(zak)
    elif choice4 == '2':
        rand2 = ["0", "1", "2"]
        rand2 = random.choice(rand2)
        if rand2 == "0":
            print("het pistool heeft maar 1 kogel\n")
            time.sleep(2)
            print("in 1 keer raak, je hebt het monster gedood\n")
            time.sleep(2)
            print("je herlaat het pistool en kijkt of het werkt\n")
            time.sleep(2)
            zak.append('pistool')
            print("je gaat uit de steeg\n")
            time.sleep(2)
            zak.append('insteeg')
            begin(zak)
        elif rand2 == "1" or rand2 == "2":
            print("het pistool heeft maar 1 kogel\n")
            time.sleep(2)
            print("je mist het schot\n")
            time.sleep(2)
            print("het monster valt je aan en jij bent dood\n")
            time.sleep(2)
            print("GAME OVER")
            opnieuw()


def naarsteeg(zak):
    if 'insteeg' in zak:
        print("het monster lichaam ligt levenloos op de grond\n")
        time.sleep(2)
        print("er is hier niks te doen\n")
        time.sleep(2)
        print("je gaat uit de steeg\n")
        time.sleep(2)
        begin(zak)
    else:
        if 'medicijn' not in zak and 'verwond' in zak:
            print("je volgt het geluid van de radio en gaat in de steeg\n")
            time.sleep(2)
            print("je vind een pistool naast de radio\n")
            time.sleep(2)
            print("Het monster komt uit het niks op je af\n")
            time.sleep(2)
            print("door jou wonden ben je net niet snel genoeg om het pistool op te trekken\n")
            time.sleep(2)
            print("het monster valt je aan en jij bent dood\n")
            time.sleep(2)
            print("GAME OVER")
            opnieuw()
        else:
            print("je volgt het geluid van de radio en gaat in de steeg\n")
            time.sleep(2)
            print("je vind een pistool naast de radio\n")
            time.sleep(2)
            print("Het monster komt uit het niks op je af\n")
            time.sleep(2)
            print("je bent net optijd om je pistool op te trekken\n")
            time.sleep(2)
            print("wat doe je?\n")
            time.sleep(2)
            alley_choice(zak)


def opnieuw():
    choice5 = input("speel opnieuw\nj) ja\nn) nee.\n")
    if choice5 == 'j':
        intro()
    elif choice5 == 'n':
        print("doeg")
        exit(0)


intro()