import sys
import wordfreq
import urllib.request


def main():
    # Öppna stoppordsfilen och lägg in dem i stopWords
    file1 = open(sys.argv[1], encoding="utf-8")
    stopWordsList = []

    for line in file1:
        line = line.strip('\n')
        stopWordsList.append(line)

    file1.close()
    # Läser in textfilen som ska användas
    arg2 = sys.argv[2]

    if arg2.startswith("http://") or arg2.startswith("https://"):
        file2 = urllib.request.urlopen(arg2)
        lines = file2.read().decode("utf8").splitlines()
        words = wordfreq.tokenize(lines)
    else:
        file2 = open(sys.argv[2], encoding="utf-8")
        words = wordfreq.tokenize(file2)

    file2.close()

    # Antalet ord som ska dyka upp i listan
    n = int(sys.argv[3])

    # Jämför stopporden med textfilen och gör en print
    frequencies = wordfreq.countWords(words, stopWordsList)
    wordfreq.printTopMost(frequencies, n)


main()
