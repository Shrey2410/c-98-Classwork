def CountWordsFromFile():
    fileName = input("Enter the File Name:- ")

    numberOfWords = 0
    numberOfLines = 0

    file = open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords = numberOfWords + len(words)
        numberOfLines = numberOfLines + 1
    print("Number of Words: ")
    print(numberOfWords)
    print("\n Number Of Lines: ")
    print(numberOfLines)

CountWordsFromFile()