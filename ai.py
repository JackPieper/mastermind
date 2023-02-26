import itertools
import spel


def simple():
    print('Simple algoritme wordt nu gespeeld')
    secret = spel.makecode()
    print(f'Code {secret} wordt nu geraden')
    colors = ['A', 'B', 'C', 'D', 'E', 'F']
    list1 = list(itertools.product(colors, repeat=4))
    list2 = []
    for i in range(10):
        print(f'Poging {i + 1}/10: {list1[0]}')
        response = spel.comp(list1[0], secret)
        if response[0] == 4:
            print('De ai heeft de code geraden.')
            return None
        print(f'Correct: {response[0]}\nVerkeerde positie: {response[1]}\n----------')
        for j in list1:
            if response == spel.comp(j, list1[0]):
                list2.append(j)
        list1, list2 = list2, []
    print('De ai heeft de code niet geraden.')


def worstcase():
    print('Worstcase algoritme wordt nu gespeeld')
    secret = spel.makecode()
    print(f'Code {secret} wordt nu geraden')
    colors = ['A', 'B', 'C', 'D', 'E', 'F']
    list1 = list(itertools.product(colors, repeat=4))
    list2 = []
    responses = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0]]
    for i in range(10):
        if i == 0:
            guess = ['A', 'A', 'B', 'B']
        else:
            possibilities = {}
            for j in list1:
                possibilities[j] = 0
                for k in responses:
                    count = 0
                    for l in list1:
                        if spel.comp(j, l) == k:
                            count += 1
                    if count > possibilities[j]:
                        possibilities[j] = count
            guess = min(possibilities, key=possibilities.get)

        print(f'Poging {i + 1}/10: {guess}')
        response = spel.comp(guess, secret)
        if response[0] == 4:
            print('De ai heeft de code geraden.')
            return None
        print(f'Correct: {response[0]}\nVerkeerde positie: {response[1]}\n----------')
        for j in list1:
            if response == spel.comp(j, guess):
                list2.append(j)
        list1, list2 = list2, []
    print('De ai heeft de code niet geraden.')

def newAlgorithm():
    pass