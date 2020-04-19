# author @daoodaba975
# GalsenDev

def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0
    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)
    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Char: ", numchars)

if __name__ == '__main__':
    countWords('FONT.txt')

#Ce script en Python permet de compter le nombre
#de mots, de lignes et de caractères dans un fichier.
#Toute la puissance de Python en quelques lignes de code