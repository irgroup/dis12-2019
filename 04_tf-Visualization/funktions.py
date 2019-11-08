import os
import re
import matplotlib.pyplot as plt
import math
import csv


# Klasse für Terme
class Term:
    def __init__(self, word, frequency, rank, c=None):
        self.word = word
        self.frequency = frequency
        self.rank = rank

        self.logF = math.log(frequency)
        self.logR = math.log(rank)
        self.p = c / rank if c is not None else None


def dataImport(path):
    files = {}
    terms = {}

    for filename in os.listdir(os.getcwd() + '/../' + path):
        if not filename.startswith('.'):
            files[filename] = {}

    for i in files:
        with open(os.getcwd() + '/../' + path + '/' + i) as file:
            text = re.findall(r'[a-z]+', file.read().lower())

            for word in text:
                if word not in terms:
                    terms[word] = 1
                else:
                    terms[word] += 1

    listofTuples = sorted(terms.items(), key=lambda x: x[1])  # Terme sortieren

    term = []
    frequency = []

    for tuples in listofTuples:
        term.append(tuples[0])
        frequency.append(tuples[1])

    return term, frequency


# Objekte erstellen
def makeObj(term, frequency, c=None):
    terms = []
    n = len(frequency)
    r = n

    for i in range(len(term)):
        terms.append(term[i])
        terms[i] = Term(term[i], frequency[i], r, c)
        r = r - 1

    return terms


# CSV Export
def exportCSV(term):
    csvData = []
    for i in range(len(term)):
        csvData.append([term[i].word, term[i].frequency])

    csv_columns = ['Term', 'Frequenz']
    with open('terme.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(csv_columns)
        writer.writerows(csvData)


def plot(termliste):
    logf = []
    logRank = []
    for i in termliste:
        logf.append(i.logF)
        logRank.append(i.logR)

    fig = plt.figure()
    plt.plot(logRank, logf)
    plt.xlabel('log(Rank)')
    plt.ylabel('log(frequency)')
    plt.title('term distribution')
    return plt.show()


def plotZipf(termliste: object, c: object) -> object:
    logfz = []

    logf = []
    logRank = []
    for i in termliste:
        logf.append(i.logF)
        logRank.append(i.logR)
        logfz.append(math.log(c) - i.logR)

    fig = plt.figure()
    plt.plot(logRank, logf)
    plt.plot(logRank, logfz)
    plt.plot()
    plt.xlabel('log(Rank)')
    plt.ylabel('log(frequency)')
    plt.title('term distribution')
    return plt.show()
