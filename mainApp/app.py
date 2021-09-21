import random

'''
To use to learn musical sequences
and chords so that I can be a better improvising musician

#Learning sequences:

Important to:
- Be musical when learning the sequences/chords
- Learn them so that I can have dexterity for note choice
- Learn them so that I can learn to how to play the sounds I hear in my head

1: either learn sequence on one string, and or learn sequence 
going down the stings. Play intervals in between each notes, making sure that
I play each note slowly I hear whats in my head to guitar

2: Go through all intervals for each note in a scale starting from string 6,
again making sure to hear each note before I play

3: Play with arpeggios like in 1, not essential to do 2 in case of 
arpeggio spend time  play around playing a musical idea with the note

#Learning chords:

4 use harmonic creator to show chords add functionality to 
5 use nashville chord thing to practice the system. Add functionality to add
diminished and dominant chords


1. Learn scales on all strings
2. go through all intervals
3. go through triad arpeggios
4. go through all seventh arpeggios
5. go through all chords



'''


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
            random.shuffle(intervalList)
            print(intervalList.pop)
            print(intervalList.pop)
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


intervalList = ['m2', 'M2', 'm3', 'M3',
                'P4', 'A4', 'P5', 'm6',
                'M6', 'm7', 'M7', 'P8']
random.shuffle(intervalList)
print(intervalList.pop())
pentatonicList = {'F': ['F', 'G', 'A', 'C', 'D'],
                  'C': ['C', 'D', 'E', 'G', 'A'],
                  'G': ['G', 'A', 'B', 'D', 'E']}

majorList = {'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
             'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
             'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#']}

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
Below are some of the mai functions used to serve the purpose of practice
'''

def stringModeOne(Key, Scale):
    if Scale == 'Pen':
        random.shuffle(pentatonicList[Key])
        print(pentatonicList[Key])
    if Scale == 'Major':
        random.shuffle(majorList[Key])
        print(majorList[Key])


def stringModeTwo(Key, Scale):
    if Scale == 'Pen':
        count = len(pentatonicList[Key])
        while count > 0:
            random.shuffle(intervalList)
            random.shuffle(pentatonicList[Key])
            print(pentatonicList[Key].pop() + ' : ' + str(intervalList))
            count -= 1
    if Scale == 'Major':
        count = len(majorList[Key])
        while count > 0:
            random.shuffle(intervalList)
            random.shuffle(majorList[Key])
            print(majorList[Key].pop() + ' : ' + str(intervalList))
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

    print(harmonyDict)
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

    print(returnList)
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

start()
chordHarmonyGenerator('A')

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
