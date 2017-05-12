'''
Using names.txt ("NAME","NAME2"), a text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file? 
'''
def main():
    tmpstr = ""
    NameList = []
    f = open('names.txt', 'r')
    NameList = ParseMe(f, NameList, tmpstr)
    NameList.sort()
    NamePosition = 1
    NameScoreSum = 0
    while NameList:
        tmpstr = NameList.pop(0)
        NameScoreSum += (NamePosition * ScoreMe(tmpstr))
        NamePosition += 1
    f.close()
    print NameScoreSum

def ParseMe(NameFile, NameList, tmpstr):
    while True:
        c = NameFile.read(1)
        if not c:
            NameList.append(tmpstr)
            tmpstr = ''
            break
        if c == ',':
            NameList.append(tmpstr)
            tmpstr = ''
        elif c != '"':
            tmpstr += c
    return NameList

def ScoreMe(name):
    LetterScores = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F': 6, 'G' : 7, 'H': 8, 'I': 9, 'J' : 10,
              'K': 11, 'L': 12, 'M' : 13, 'N': 14, 'O' : 15, 'P' : 16, 'Q': 17, 'R': 18, 'S' : 19,
              'T' : 20, 'U' : 21, 'V' : 22, 'W': 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    score = 0
    for x in range (len(name)):
        score += LetterScores[name[x]]
    return score
