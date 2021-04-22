def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start+1
            if start < len(line) and line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end+1
                words.append(line[start:end].lower())
                start = end
            elif start < len(line) and line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end+1
                words.append(line[start:end])
                start = end
            else:
                if start < len(line):
                    words.append(line[start])
                    start = start+1
    return words


def countWords(words, stopWords):

    dict = {}
    for word in words:
        if word in stopWords:
            pass
        elif word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict


def printTopMost(frequencies, n):

    for item in sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:n]:
        strNumber = str(item[1])
        print(item[0].ljust(20) + strNumber.rjust(5))
