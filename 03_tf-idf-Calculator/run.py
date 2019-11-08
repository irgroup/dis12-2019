import os
import math
import re

searchTerm = 'CLEOPATRA'


files = {}  # Dictionary für die Dokumente
searchTerm = searchTerm.lower() # vereinheitlichen


# Öffnet die zu durchsuchenden Dokumente
for filename in os.listdir(os.getcwd() + '/../Shakespeare'):
    if not filename.startswith('.'):  # sortiert unsichtbare Dateien aus
        files[filename] = {}    # Dictionarry für alle Dateien

for i in files:
    with open(os.getcwd() + '/../Shakespeare/' + i) as file:
        text = re.findall(r'[a-z]+', file.read().lower())  # aufteilen in Worte

    # Term Dokument Abgleich
    if searchTerm in text:
        files[i][searchTerm + '_Df'] = 1
    else:
        files[i][searchTerm + '_Df'] = 0


    # Termfrequenz zählen
    tf = 0
    for term in text:
        if term == searchTerm:
            tf = tf + 1

    files[i][searchTerm + '_Tf'] = tf


# Dokumentfrequenz errechnen
Df = 0
for file in files:
    Df = Df + files[file].get(searchTerm + '_Df')


# idf berechnen
n = len(files)
idf = math.log10(n / Df)


#Ausgabe
print('Suchterm: ' + searchTerm)
print('------------------------------------------------------------\n')

print('Df = ' + str(Df))
print('------------------------------------------------------------\n')

print('\nTF:')
for i in files:
    if files[i][searchTerm + '_Tf'] != 0:
        print(i + ' = ' + str(files[i][searchTerm + '_Tf']))
print('------------------------------------------------------------\n')

print('\ntf_idf:')
for i in files:
    if files[i][searchTerm + '_Tf'] != 0:
        print(i + ' = ' + str(round((1 + math.log10(files[i][searchTerm + '_Tf'])), 2)))
print('------------------------------------------------------------\n')