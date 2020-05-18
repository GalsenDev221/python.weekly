# author @daoodaba975
# GalsenDev

import os

PATH = 'C:\Intel' #le Répertoire où nous devons chercher le fichier
def searchFile(fileName):
    for root, dirs, files in os.walk(PATH):
        print('Cherche dans:', root)
        for Files in files:
            try:
                found = Files.find(fileName)
                if found != 1:
                    print(fileName, 'Trouvé')
                    break
            except:
                exit()
if __name__ == '__main__':
    searchFile('logo.png') #Nom du fichier à rechercher + extension
