term = 'Romeo AND Juliet OR Tybalt'
import os


# Funktion zum Aufteilen des Suchterms in ein logisches Dictionary
def termSplit(term):
    # Funktion zum sotrieren der Begriffe nach Operatoren in ein Dictionary
    def sort(i):

        # Der Begriff links und rechts vom OR
        if i == 'OR':
            termdict['OR'].append(termlist[termlist.index(i) - 1])
            ignore.append(termlist[termlist.index(i) - 1])
            termdict['OR'].append(termlist[termlist.index(i) + 1])
            ignore.append(termlist[termlist.index(i) + 1])

        # Der Begrif links und rechts vom XOR
        if i == 'XOR':
            termdict['XOR'].append(termlist[termlist.index(i) - 1])
            ignore.append(termlist[termlist.index(i) - 1])
            termdict['XOR'].append(termlist[termlist.index(i) + 1])
            ignore.append(termlist[termlist.index(i) + 1])
        
        # NOT Begriffe
        elif i == 'NOT':
            termdict['NOT'].append(termlist[termlist.index(i) + 1])
            ignore.append(termlist[termlist.index(i) + 1])

        # AND Begriffe
        elif i not in ignore:
            termdict['AND'].append(termlist[termlist.index(i)])

    # Erstellen des Ausgabe Dictionarys
    termdict = {}
    termdict['NOT'] = []  # Liste für NOT Begriffe
    termdict['OR'] = []  # Liste für OR Begriffe
    termdict['XOR'] = []  # Liste für XOR Begriffe
    termdict['AND'] = []  # Liste für AND Begriffe

    # Term Aufteilen
    termlist = term.split(' ')

    # Terme die schon sortiert sind oder ignoriert werden sollen
    ignore = ['NOT', 'XOR', 'OR', 'AND']

    # Ausführen der sortierfunktion
    for i in termlist[1:]:  # Startet bei Index 1 da der erste Begriff Teil eines OR/XOR Operators sein kann
        sort(i)
    sort(termlist[0])  # Prüft den ersten Begriff

    return termdict


# Funktion zum Abgleich des Suchterms mit den Dokumenten
def match(termdict):
    files = {}  # Dictionary für die Dokumente

    # Öffnet die zu durchsuchenden Dokumente
    for filename in os.listdir(os.getcwd() + '/../Shakespeare'):
        if not filename.startswith('.'):  # sortiert unsichtbare Dateien aus
            files[filename] = {}

        # Abgleich mit den Suchtermen
        for i in files:
            with open(os.getcwd() + '/../Shakespeare/' + i) as file:
                text = file.read()

            for term in termdict['NOT']:
                if term in text:
                    files[i][term] = 0
                else:
                    files[i][term] = 1

            for term in termdict['AND']:
                if term in text:
                    files[i][term] = 1
                else:
                    files[i][term] = 0

            ORlist = []
            for term in termdict['OR']:
                if term in text:
                    ORlist.append(1)
                else:
                    files[i][term] = 0

            if sum(ORlist) == 1:
                files[i]['OR'] = 1
            else:
                files[i]['OR'] = 0
    return files


def result(files):
    resultList = []

    for texte in files:
        count = 0
        for key in files[texte]:
            count = count + files[texte].get(key)
        if count == 2:
            resultList.append(texte)

    return resultList


termdict = termSplit(term)
erg = match(termSplit(term))
print(result(match(termSplit(term))))