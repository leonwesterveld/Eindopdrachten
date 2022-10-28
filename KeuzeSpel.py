import time
import random
import os

def ts(sleeptime,txt):
    time.sleep(sleeptime)
    print(txt)




def intro():
    zak = []
    ts(2.0,"je maakt een wandeling in een bos\n")
    
    ts(2.0, "je hoort een raar geluid en ziet een lichtflits\n")
    
    ts(2.0, "na een paar seconde is alles weg en ben je niet meer in het bos\n")
    
    ts(2.0, "je bevind jezelf in een verlaten stad\n")
    
    ts(2.0, "de stad is helemaal mistig.\n")
    ts(2.0)
    os.system('cls')
    ts(2.0, "Wat je kan zien zijn allemaal borden met 'GA WEG MONSTERS'\n")
    
    ts(2.0,  "Je wordt bang en vraagt je af waar die monsters zijn.\n")
    
    ts(2.0, "Je staat voor een huis.\n")
    
    ts(2.0, "Rechts van je is een steeg \n")
    
    ts(2.0, "Waar je iets van een radio hoort.\n")
    ts(2.0)
    os.system('cls')
    begin(zak)


def begin(zak):
    if 'inhuis' in zak and 'insteeg' in zak:
        if 'medicijn' not in zak and 'verwond' in zak:
            ts(2.0, "je hebt beide monsters verslagen \n")
            
            ts(2.0, "je kan niet weg als je verwond bent\n")
            
            waar(zak)
        else:
            ts(2.0, "je hebt beide monsters verslagen\n")
            
            ts(2.0, "je hoort het geluid weer en ziet weer een lichtflits\n")
            
            ts(2.0, "je bent weer terug in het bos waar je eerst was\n")
            
            opnieuw()
    else:
        waar(zak)


def waar(zak):
    if 'pistool' in zak:
        ts(2.0, "je hebt een pistool en een mes in je zak\n")
        
    else:
        ts(2.0, "Je hebt een mes in je zak.\n")
        
    choice1 = input("1) ga in het huis.\n2) ga naar de steeg\n")
    if choice1 == '1':
        os.system('cls')
        huis(zak)
    elif choice1 == '2':
        os.system('cls')
        naarsteeg(zak)



def huis(zak):
    if 'inhuis' in zak:
        ts(2.0, "het monster ligt bewusteloos op de grond.\n")
        
        naarboven(zak)
    else:
        if 'pistool' in zak:
            ts(2.0, "Je hebt het huis betreden\n")
            
            ts(2.0, "Je komt in aanraking met het andere monster\n")
            
            ts(2.0, "het monster is klaar om je aan te vallen\n")
            
            choice2 = input("1) gebruik je mes \n2) gebuik het pistool\n")
            if choice2 == '2':
                ts(2.0, "je hebt met het moster gevochten en hebt het gedood\n")
                
                ts(2.0, " met je pistool\n")
                
                ts(2.0, "je hebt je wel verwond in het gevecht\n")
                
                zak.append('verwond')
                zak.append('inhuis')
                naarboven(zak)
            elif choice2 == '1':
                mesinhuis(zak)
        elif 'pistool' not in zak:
            ts(2.0, "Je hebt het huis betreden\n")
            
            ts(2.0, "Je komt in aanraking met het andere monster\n")
            
            ts(2.0, "het monster is klaar om je aan te vallen\n")
            
            mesinhuis(zak)

def mesinhuis(zak):
    if 'pistool' not in zak:
        ts(2.0, "je hebt alleen een mes in dit gevecht\n")
        
    elif 'pistool' in zak:
        ts(2.0, "je kiest om te vechten met het mes\n")
        
    rand1 = ["0", "1"]
    rand1 = random.choice(rand1)
    if rand1 == '0':
        ts(2.0, "Jou mes had geen effect in dit gevecht\n")
        
        ts(2.0, "GAME OVER")
        opnieuw()
    elif rand1 == '1':
        ts(2.0, "je hebt gevochten met het monster\n")
        
        ts(2.0, "je hebt het net overleeft, maar je hebt het monster gedood\n")
        
        ts(2.0, "je hebt je wel verwond in het gevecht\n")
        
        zak.append('verwond')
        zak.append('inhuis')
        naarboven(zak)





def naarboven(zak):
    ts(2.0, "wat ga je doen?\n")
    
    choice3 = input("1) het huis verlaten\n2) naar boven om meer te zoeken\n")
    if choice3 == '1':
        ts(2.0, "je verlaat het huis\n")
        
        begin(zak)
    elif choice3 == '2':
        if 'medicijn' not in zak:
            ts(2.0, "je bent naar boven gegaan en vond medicijnen\n")
            
            ts(2.0, "je heb je verwondingen beter gemaakt\n")
            
            zak.append('medicijn')
            begin(zak)
        elif 'medicijn' in zak:
            ts(2.0, "je loopt naar boven maar je kan niks vinden\n")
            
            begin(zak)


def alley_choice(zak):
    choice4 = input("1) het monster aanvallen met je mes\n2) het monster beschieten met je pistool \n")
    if choice4 == '1':
        ts(2.0, "je hebt het monster vermoord met je mes\n")
        
        ts(2.0, "je kijkt naar het pistool\n")
        
        ts(2.0, "je kijkt of het pistool werkt en herladen is\n")
        
        zak.append('pistool')
        ts(2.0, "je gaat uit de steeg\n")
        
        zak.append('insteeg')
        begin(zak)
    elif choice4 == '2':
        rand2 = ["0", "1", "2"]
        rand2 = random.choice(rand2)
        if rand2 == "0":
            ts(2.0, "het pistool heeft maar 1 kogel\n")
            
            ts(2.0, "in 1 keer raak, je hebt het monster gedood\n")
            
            ts(2.0, "je herlaat het pistool en kijkt of het werkt\n")
            
            zak.append('pistool')
            ts(2.0, "je gaat uit de steeg\n")
            
            zak.append('insteeg')
            begin(zak)
        elif rand2 == "1" or rand2 == "2":
            ts(2.0, "het pistool heeft maar 1 kogel\n")
            
            ts(2.0, "je mist het schot\n")
            
            ts(2.0, "het monster valt je aan en jij bent dood\n")
            
            ts(2.0, "GAME OVER")
            opnieuw()


def naarsteeg(zak):
    if 'insteeg' in zak:
        ts(2.0, "het monster lichaam ligt levenloos op de grond\n")
        
        ts(2.0, "er is hier niks te doen\n")
        
        ts(2.0, "je gaat uit de steeg\n")
        
        begin(zak)
    else:
        if 'medicijn' not in zak and 'verwond' in zak:
            ts(2.0, "je volgt het geluid van de radio en gaat in de steeg\n")
            
            ts(2.0, "je vind een pistool naast de radio\n")
            
            ts(2.0, "Het monster komt uit het niks op je af\n")
            
            ts(2.0, "door jou wonden ben je net niet snel genoeg om het pistool op te trekken\n")
            
            ts(2.0, "het monster valt je aan en jij bent dood\n")
            
            ts(2.0, "GAME OVER")
            opnieuw()
        else:
            ts(2.0, "je volgt het geluid van de radio en gaat in de steeg\n")
            
            ts(2.0, "je vind een pistool naast de radio\n")
            
            ts(2.0, "Het monster komt uit het niks op je af\n")
            
            ts(2.0, "je bent net optijd om je pistool op te pakken\n")
            
            ts(2.0, "wat doe je?\n")
            
            alley_choice(zak)


def opnieuw():
    choice5 = input("speel opnieuw\nj) ja\nn) nee.\n")
    if choice5 == 'j':
        intro()
    elif choice5 == 'n':
        ts(2.0, "doeg")
        exit(0)


intro()