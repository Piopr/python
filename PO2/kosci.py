import random
import time

def throw():
    l1= random.randint(1,6)
    l2= random.randint(1,6)
    return l1+l2

def single_game(): 
    wynik=throw()
    if wynik==7 or wynik==11:
        return True
    elif wynik==2 or wynik==3 or wynik==12:
        return False
    else:
        while True:
            wynik_next=throw()
            if wynik_next==wynik:
                return True
            elif wynik_next==7:
                return False
            wynik=wynik_next

def get_answer(odpowiedz):
    if odpowiedz.lower()=='tak':        
        return True
    else:
        return False

def gra():
    wygrane=0
    przegrane=0
    print("Witaj w grze w kosci!")
    while True:
        time.sleep(1)
        print("Czy chcesz zagrac?")
        print("Odpowiedz tak lub cokolwiek innego, jesli nie chcesz grac")
        if get_answer(input()):
            if single_game():
                wygrane+=1
            else:
                przegrane+=1
        else:
            print("Twoj wynik:")
            print("Wygrane: ", wygrane)
            print("Przegrane: ", przegrane)
            break

gra()
    


    
        
        
