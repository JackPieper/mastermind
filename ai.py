import itertools
import spel


def simple():
    # Bron: Theorie van het artikel van de Universiteit Groningen en uitleg van student Jason Griffioen
    print('Simple algoritme wordt nu gespeeld')
    secret = spel.makecode()
    print(f'Code {secret} wordt nu geraden')
    colors = ['A', 'B', 'C', 'D', 'E', 'F']
    list1 = list(itertools.product(colors, repeat=4))
    list2 = []
    for i in range(10):
        guess = list1[0]
        turn(guess, secret, list1, list2, i)
        list1, list2 = list2, []
        if len(list1) <= 1:
            return None
    print('De ai heeft de code niet geraden.')


def worstcase():
    # Bron: Theorie van het artikel van de Universiteit Groningen
    print('Worstcase algoritme wordt nu gespeeld')
    secret = spel.makecode()
    print(f'Code {secret} wordt nu geraden')
    colors = ['A', 'B', 'C', 'D', 'E', 'F']
    list1 = list(itertools.product(colors, repeat=4))
    list2 = []
    for i in range(10):
        if i == 0:
            guess = ['A', 'A', 'B', 'B']
        else:
            possibilities = answers(list1)
            if possibilities:
                guess = min(possibilities, key=possibilities.get)
            else:
                return None
        turn(guess, secret, list1, list2, i)
        list1, list2 = list2, []
    print('De ai heeft de code niet geraden.')

def newAlgorithm():
    # Deze methode werkt door het gemiddelde te pakken ipv laagste
    print('Worstcase algoritme wordt nu gespeeld')
    secret = spel.makecode()
    print(f'Code {secret} wordt nu geraden')
    colors = ['A', 'B', 'C', 'D', 'E', 'F']
    list1 = list(itertools.product(colors, repeat=4))
    list2 = []
    for i in range(10):
        if i == 0:
            guess = ['A', 'A', 'B', 'B']
        else:
            possibilities = answers(list1)
            if possibilities:
                guess = list(j for j in possibilities if possibilities[j] == sorted(list(possibilities.values()))[int(len(possibilities) / 2)])[0]
            else:
                return None
        turn(guess, secret, list1, list2, i)
        list1, list2 = list2, []
    print('De ai heeft de code niet geraden.')

def answers(lijst):
    responses = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0]]
    possibilities = {}
    for j in lijst:
        possibilities[j] = 0
        for k in responses:
            count = 0
            for l in lijst:
                if spel.comp(j, l) == k:
                    count += 1
            if count > possibilities[j]:
                possibilities[j] = count
    return possibilities

def turn(guess, secret, list1, list2, i):
    print(f'Poging {i + 1}/10: {guess}')
    response = spel.comp(guess, secret)
    if response[0] == 4:
        print('De ai heeft de code geraden.')
        return None
    print(f'Correct: {response[0]}\nVerkeerde positie: {response[1]}\n----------')
    for j in list1:
        if response == spel.comp(j, guess):
            list2.append(j)
