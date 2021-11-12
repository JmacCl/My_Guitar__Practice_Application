import random

'''
This application is a collection of methods to help with my guitar practice. The functions are mostly designed around helping
me practice musical sequences, however I am working on making functions that produce a chord harmony chart and a function to help me
practice the nashville system for a given key.

If you are reading this an are interested in using application, here is a following guide on how to use the methods:

- There is a function called start that should explain how to use some of the more functional methods

In terms of future implementations, I would like to ensure that the methods are more efficient in terms of time complexity,
I would like to add functionality to the methods so that they can work with more complicated musical sequences and I would like to 
make all the methods generally more clear.
'''

'''
Start works by asking for 4 inputs:
 - The key you want to use
 - The selection of the musical sequence(scale/arpeggio)
 - The function you would like to use
 - How many times you want that function to be called

For function use there are 4 commands

1: stringModeOne for scales print out random selection of notes in a given sequence
2. stringModeTwo, prints out a random order of notes in a given sequence with intervals
3. Generates a chord harmony chart of a given key
4. Generates a list of arpeggios for a given key. 
'''
#This function starts the application
def start():
    selectionOfKey = input('What Key?: ')
    selectionOfScale = input('What type of scale/arpeggio?: ')
    userInput = input('What mode do you want?: ')
    howManyTimes: int = int(input('How many times do you want the function be printed: '))
    userInput = convertWordsForStart(userInput)

    while howManyTimes > 0:
        if userInput == '1':
            choiceOfSequence = convertWordsForStart(input('Arpeggio or scale practice?: '))
            if choiceOfSequence == 'scale':
                stringModeOne(selectionOfKey, selectionOfScale)
            elif choiceOfSequence == 'arpeggio':
                stringModeOneArp(selectionOfKey)
        elif userInput == '2':
            stringModeTwo(selectionOfKey, selectionOfScale)
        elif userInput == '3':
            chordHarmonyGenerator(selectionOfKey)
            keyChordPractice(selectionOfKey)
        elif userInput == '4':
            arpeggioList = getArpeggio(selectionOfKey, selectionOfScale)
            random.shuffle(intervalList)
            random.shuffle(arpeggioList)
            print(intervalList.pop())
            print(arpeggioList)
        howManyTimes -= 1
        print('\n')

''' 
Below are dictionaries or lists used to hold data for the functions of the 
code
'''

'''
The interval list below is used to play in between notes in a musical scale
'''
intervalList = ['m2', 'M2', 'm3', 'M3',
                'P4', 'A4', 'P5', 'm6',
                'M6', 'm7', 'M7', 'P8']

'''
The two dictionaries below are used to generate scales depending on the given input key and scale type
'''

pentatonicList = {'F': ['F', 'G', 'A', 'C', 'D'],
                  'C': ['C', 'D', 'E', 'G', 'A'],
                  'G': ['G', 'A', 'B', 'D', 'E']}

majorList = {'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
             'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
             'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#']}

'''
The dictionary below is used for the chord harmony chart generator to indicate the what chords in the scale are present,
and the positions of the secondary dominant and diminished chords.
'''
chordNumbers = {'simple': ['1', '2', '3', '4', '5', '6', '7'],
                'diminished': ['dim2', 'dim3', 'dim4', 'dim5', 'dim6'],
                'dominant': ['dom2', 'dom3', 'dom4', 'dom5', 'dom6']}

arpeggiosDict = {'M': [4, 7], 'm': [3, 7], '+': [4, 8], 'o': [3, 6],
                 'M7': [4, 7, 11], 'm7': [3, 7, 10], '7': [4, 7, 11], 'ø7': [3, 6, 10], 'o7': [3, 6, 9]}

scaleDict = {'Major': [2, 4, 5, 7, 9, 11],
             'Minor': [2, 3, 5, 7, 8, 10]}

scaleComplexityDict = {'Major': [{0: 'M', 1: 'm', 2: 'm', 3: 'M', 4: 'M', 5: 'm', 6: 'o'},
                                 {0: 'M7', 1: 'm7', 2: 'm7', 3: 'M7', 4: '7', 5: 'm7', 6: 'ø7'}]}
notesDict = {0: ['B#', 'C'],
             1: ['C#', 'Db'],
             2: 'D',
             3: ['D#', 'Eb'],
             4: 'E',
             5: ['E#', 'F'],
             6: ['F#', 'Gb'],
             7: 'G',
             8: ['G#', 'Ab'],
             9: 'A',
             10: ['A#', 'Bb'],
             11: 'B'}

'''
Below are some of the main functions used to serve the purpose of practice
'''

'''
The function stringModeOne takes in two parameters:
1. The key of the scale
2. The scale which can either be a penatonic or major scale

The methods works by shuffling the list from a given key, 
depending on the scale type and then printing that shuffled scale.
'''
def stringModeOne(Key, Scale):
    if Scale == 'Pen':
        random.shuffle(pentatonicList[Key])
        print(pentatonicList[Key])
    if Scale == 'Major':
        random.shuffle(majorList[Key])
        print(majorList[Key])


'''
The function stringModeTwo takes in two parameters:
1. The key of the scale
2. The scale which can either be a pentatonic or major scale

Basically the same function as above, however it includes a interval to be played in between each note in a musical sequence
'''
def stringModeTwo(Key, Scale):
    if Scale == 'Pen':
        random.shuffle(pentatonicList[Key])
        count = len(pentatonicList[Key])
        while count > 0:
            random.shuffle(intervalList)
            print(pentatonicList[Key].pop() + ' : ' + str(intervalList))
            count -= 1
    if Scale == 'Major':
        random.shuffle(majorList[Key])
        count = len(majorList[Key])
        while count > 0:
            random.shuffle(intervalList)
            print(majorList[Key].pop() + ' : ' + str(intervalList))
            count -= 1

'''
This function below is used to pop intervals from interval list by a certain amount
'''
def printXAmountFromInterval(amount):
    copy = intervalList.copy()
    random.shuffle(copy)
    count = 0
    while count <= amount:
        if count == 12:
            amount -= 12
            copy = intervalList.copy()
            random.shuffle(copy)
            print(copy.pop())
            count = 1
        else:
            random.shuffle(copy)
            print(copy.pop())
            count -= 1


def getArpeggio(Key, Arpeggio):
    inputArpeggio = Arpeggio
    keyNumber = get_key(Key, notesDict)
    returnList = []
    returnList.append(keyNumber)
    addList = arpeggiosDict[inputArpeggio]
    for numbers in addList:
        returnList.append((keyNumber + numbers) % 12)
    for notes in returnList:
        newNotes = notesDict[notes]
        returnList[returnList.index(notes)] = newNotes
    for notes in returnList:
        if isinstance(notes,list):
            returnList[returnList.index(notes)] = random.choice(notes)
    returnList[0] = Key
    return returnList


def nashvillePractice(Key, Number, Mode):
    holderList = []
    for mode in Mode:
        holderList.extend(mode)
    random.shuffle(holderList)
    returnList = []
    while (Number > 0):
        returnList.append(holderList.pop())
        Number -= 1
    print(Key + ': ' + str(returnList))


def keyChordPractice(Key):
    returnList = []
    returnList.extend(chordNumbers['simple'])
    returnList.extend(chordNumbers['dominant'])
    returnList.extend(chordNumbers['diminished'])
    random.shuffle(returnList)
    print(Key + ': ' + str(returnList))


notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
         'F#', 'G', 'G#', 'A', 'A#', 'B']


# Take in input of key for the key, selected if you want simple, diminished, dominants,
# and the 7ths of those chords
# Also Include system to have parallel scales
# Also include mode to practice Nashville number system.

# First just do Major
def chordHarmonyGenerator(Key):
    activateDominant = False
    activateDiminished = False
    dominantInput = convertWords(input('Include secondary dominant chords?: '))
    diminishedInput = convertWords(input('Include secondary diminished chords? '))
    extraScales = input('Any extra scales? (please separate by commas): ')
    typeInput = convertWords(input('Triads or Sevenths?: '))

    newList = extraScales.split(',')
    keyNumber = get_key(Key, notesDict)
    returnList = [keyNumber]
    initialScale = scaleDict['Major']
    for numbers in initialScale:
        returnList.append((keyNumber + numbers) % 12)
    returnList[0] = Key
    for numbers in returnList[1:]:
        note = notesDict[numbers]
        returnList[returnList.index(numbers)] = note
    getRidOfListSubSets(returnList)
    if dominantInput == 'yes':
        dominantInput = getDominantList(returnList)
        getRidOfListSubSets(dominantInput)
        addComplexity(dominantInput, '', typeInput, 'dominant')
        activateDominant = True
    if diminishedInput == 'yes':
        diminishedInput = getDiminishedList(returnList)
        getRidOfListSubSets(diminishedInput)
        addComplexity(diminishedInput, '', typeInput, 'diminished')
        activateDiminished = True
    addComplexity(returnList, 'Major', typeInput, 'normal')
    print(['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viio'])
    print(['T', 'pD', 'T', 'pD', 'D', 'T', 'D'])
    print(returnList)
    if activateDominant:
        dominantInput = ['-'] + dominantInput + ['-']
        print(dominantInput)
    if activateDiminished:
        diminishedInput = ['-'] + diminishedInput + ['-']
        print(diminishedInput)
    return [returnList, dominantInput, diminishedInput]


def stringModeOneArp(Key):
    ArepeggioType = convertWords(input('What kinds of arpeggio?: '))
    harmonyDict = []
    if ArepeggioType == 'triad':
        harmonyDict = scaleComplexityDict['Major'][0]
    elif ArepeggioType == 'seventh':
        harmonyDict = scaleComplexityDict['Major'][1]


    keyNumber = get_key(Key, notesDict)
    returnList = [keyNumber]
    initialScale = scaleDict['Major']
    for numbers in initialScale:
        returnList.append((keyNumber + numbers) % 12)
    returnList[0] = Key
    for numbers in returnList[1:]:
        note = notesDict[numbers]
        returnList[returnList.index(numbers)] = note
    getRidOfListSubSets(returnList)


    for notes in returnList:
        print(notes + ' ' + harmonyDict[returnList.index(notes)] +
              ':' + str(getArpeggio(notes, harmonyDict[returnList.index(notes)])))
    '''
    C M:
    D m:
    E m:
    F M:
    G M:
    A m:
    B o:
    '''


'''
Content below are functions that are used to 
make code above more simple
'''


# -------------------------------------------------------------------------------------------

def addComplexity(List, Scale, Input, Mode):
    if Mode == 'normal':
        if Input == 'triad':
            selectedScale = scaleComplexityDict[Scale][0]
        else:
            selectedScale = scaleComplexityDict[Scale][1]
        for notes in List:
            List[List.index(notes)] = notes + selectedScale[List.index(notes)]
    elif Mode == 'dominant':
        if Input == 'triad':
            pass
        else:
            for notes in List:
                List[List.index(notes)] = notes + '7'
    elif Mode == 'diminished':
        if Input == 'triad':
            for notes in List:
                List[List.index(notes)] = notes + 'o'
        else:
            for notes in List:
                List[List.index(notes)] = notes + 'o7'


triadList = ['triad', '3', 'Triad', 'Three', ' three']
sevenList = ['sevenths', '7', 'seven', 'seventh']
yesList = ['yes', 'Yes', 'y', 'Y']
noList = ['no', 'No', 'n', 'N']


def convertWords(input):
    if input in triadList:
        return 'triad'
    elif input in sevenList:
        return 'seventh'
    elif input in yesList:
        return 'yes'
    elif input == noList:
        return 'no'


modeOneList = ['1', 'One', 'one', 'Mode one', 'Mode One']
modeTwoList = ['2', 'Two', 'two', 'Mode two', 'Mode Two']
startArpList = ['arpeggio','Arpeggio', 'arp', 'Arp', 'a', 'A']
startScaleList = ['Scale', 'scale', 's', 'S']


def convertWordsForStart(input):
    if input in modeOneList:
        return '1'
    if input in modeTwoList:
        return '2'
    if input in startArpList:
        return 'arpeggio'
    if input in startScaleList:
        return 'scale'



def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
        elif isinstance(value, list):
            for items in value:
                if val == items:
                    return key

    return "key doesn't exist"


def getDiminishedList(Scale):
    returnList = []
    # dominantNote = Scale[4:5].pop()
    # dominantNoteNumber = get_key(dominantNote,notesDict)
    count = 5
    scaleIndex = 1
    while (count > 0):
        diminishedNoteNumber = get_key(Scale[scaleIndex], notesDict) - 1
        returnList.append((notesDict[(diminishedNoteNumber) % 11]))
        count -= 1
        scaleIndex += 1
    return returnList


def getDominantList(Scale):
    returnList = []
    # dominantNote = Scale[4:5].pop()
    # dominantNoteNumber = get_key(dominantNote,notesDict)
    count = 5
    scaleIndex = 1
    while (count > 0):
        dominantNoteNumber = get_key(Scale[scaleIndex], notesDict) + 7
        returnList.append((notesDict[(dominantNoteNumber) % 12]))
        count -= 1
        scaleIndex += 1
    return returnList


def getElementBeforeInSequence(List, Element):
    returnNote = List[List.index[Element] - 1]
    if returnNote >= 0:
        return List[List.index[Element] - 1]
    else:
        return None


def getRidOfListSubSets(List: list):
    ignoreBool = False
    for notes in List:
        if isinstance(notes, list):
            noteBefore = List[List.index(notes) - 1]
            for note in notes:
                if noteBefore == '-':
                    pass
                elif note == '-':
                    pass
                elif notes[0][0] == noteBefore[0]:
                    newNote = notes[1]
                    List[List.index(notes)] = newNote
                    break
                else:
                    newNote = notes[0]
                    List[List.index(notes)] = newNote
                    break


# ---------------------------------------------------------------------------------

'''
Use this area to test out code
'''

# -----------------------------------------

printXAmountFromInterval(5)
stringModeOne('F','Pen')

#chordHarmonyGenerator('F')

#nashvillePractice('F',7,'NOne')
# random.shuffle(intervalList)
# print(intervalList.pop())
# print(intervalList.pop())
# print(intervalList.pop())
# print(intervalList.pop())
# print(intervalList.pop())
# print(intervalList.pop())
#
#
# stringModeOne('F', 'Major')
# #start()
# chordHarmonyGenerator('F')

# for arpeggios just return a random one of the items in sublist.


# -----------------------------------------


"""
Code that below is obsolete
"""

# pentatonicJumpList = {'G': {'2': [3, 5, 8, 10, 12, 15, 17, 20],
#                             '3': [2, 4, 7, 9, 12, 14, 16, 19, 21],
#                             '4': [2, 5, 7, 9, 12, 14, 17, 19, 21],
#                             '5': [2, 5, 7, 10, 12, 14, 17, 19],
#                             '6': [3, 5, 7, 10, 12, 15, 17, 19]},
#                       'F': {'2': [3, 6, 8, 10, 13, 15, 18, 20],
#                             '3': [2, 5, 7, 10, 12, 14, 17, 19],
#                             '4': [2, 5, 7, 10, 12, 14, 17, 19],
#                             '5': [3, 5, 8, 10, 12, 15, 17, 20],
#                             '6': [3, 5, 8, 10, 13, 16, 17, 21]}}
# majorJumpList = {'F':{'2': [3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20],
#                       '3': [2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21],
#                       '4': [2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20],
#                       '5': [3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20],
#                       '6': [3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 21]} }
#
# # Stuff below is for the old 2 string practice
# def twoString(Key, Scale):
#     userInput = input('What is the base string?: ')
#     sList = list
#     if Scale == 'Pen':
#         count = len(pentatonicList[Key])
#         while count > 0:
#             random.shuffle(pentatonicJumpList[Key][userInput])
#             random.shuffle(pentatonicList[Key])
#             print(pentatonicList[Key].pop() + ' : ' + str(pentatonicJumpList[Key][userInput]))
#             count -= 1
#     if Scale == 'Major':
#         count = len(majorList[Key])
#         while count > 0:
#             random.shuffle(majorJumpList[Key][userInput])
#             random.shuffle(majorList[Key])
#             print(majorList[Key].pop() + ' : ' + str(majorJumpList[Key][userInput]))
#             count -= 1
