from sys import argv, stdout
from collections import Counter
import numpy as np
from random import choice


class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)

    def index(self, value):
        return np.where(self == value)


class searchTheWords:
    def __init__(self, punctuation):
        self.punctuation = punctuation


    def GetIndexes(self, str, word, punctofff=False):
        def stringToList(string, punct, punctoff):
            wordList = string.split()
            if punctoff:
                i = 0
                for word in wordList:
                    if word in punct:
                        wordList.pop(i)
                    elif word[-1] in punct:
                        wordList[i] = word[:-1]
                        word = wordList[i]
                    elif word[0] in punct:
                        wordList[i] = word[1:]
                    i += 1
            return wordList


        words = stringToList(str, self.punctuation, punctofff)
        nparray = np.array(words)
        SearchWordsInx = myarray(nparray)
        indexes = SearchWordsInx.index(word)

        self.indexes = indexes
        self.words = words


    def createTexts(self, textlthbef, textlthaft):
        outstring = ""
        for index in self.indexes[0]:
            outstring += "\n"
            indexbefore = int(int(index)-textlthbef)
            indexafter = int(index+textlthaft)
            for i in range(indexbefore, indexafter):
                if i == index:
                    outstring += ((self.words[i]).upper())
                    outstring += "  "
                    continue
                outstring += (self.words[i])
                outstring += "  "
            outstring += "\n"
        return outstring


print('\n----------------------------\nTikhonSystems\n----------------------------')

script, filename, word, textlenthbefore, textlenthafter = argv
textlenthbefore = int(textlenthbefore)
textlenthafter = int(textlenthafter)

print('Открытие файла ...\n')
str = ((open(filename)).read()).lower()
punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '-', '--', '\"', '{', '}']

print('\nЗапуск\n')
WordSeacher = searchTheWords(punctuation)

print('Поиск слов ...')
WordSeacher.GetIndexes(str, word)

print('\n\nГенерация абзацев ...')
predictedString = WordSeacher.createTexts(textlenthbefore, textlenthafter)

print('\nЗапись сгенерированного текста в файл ...\n')
outputfile = open('output.txt', 'w')
outputfile.write(predictedString)
outputfile.close()

print('Сгенерированный текст:\n')
print(predictedString, '\n')
