from random import randrange, seed
import ai

def makecode():
    seed()
    secret = []
    for i in range(4):
        val = randrange(65, 71)
        secret.append(chr(val))
    return secret


def playgame(secret):
    print('Guess the code.')
    for i in range(10):
        guess = input(f'Poging {i + 1}/10: ')
        attempt = comp(guess.upper(), secret)
        print(f'Correct: {attempt[0]}\nVerkeerde positie: {attempt[1]}\n----------')
        if attempt[0] == 4:
            print(f'Gefeliciteerd, je hebt de code {secret} ontcijferd!')
            return None
    print(f'Helaas, het is niet gelukt de code {secret} te ontcijferen.')


def comp(guess, secret):
    corr, half = 0, 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            corr += 1
    for i in range(65, 71):
        let = chr(i)
        if let in secret:
            seccnt, guescnt = secret.count(let), guess.count(let)
            if seccnt < guescnt:
                half += seccnt
            else:
                half += guescnt
    half -= corr
    return [corr, half]


def run():
    modus = input('MasterMind, Crack the code\n1: Speel zelf\n2: Simple Algoritme\n3: Worst Case Algoritme\n'
                  '4: Zelfgemaakte Algoritme\nKies een modus: ')
    match modus:
        case '1':
            playgame(makecode())
        case '2':
            ai.simple()
        case '3':
            ai.worstcase()
        case '4':
            ai.newAlgorithm()
