def main():
    count = 0
    tmpstr = ""
    mylist = []
    scorez = []
    f = open('names.txt', 'r')
    while True:
        c = f.read(1)
        if not c:
            mylist.append(tmpstr)
            tmpstr = ''
            count += 1
            break
        if c == ',':
            mylist.append(tmpstr)
            tmpstr = ''
            count += 1
        elif c != '"':
            tmpstr += c
    mylist.sort()
    pos = 1
    sumz = 0
    while mylist:
        tmpstr = mylist.pop(0)
        sumz += (pos * scoreMe(tmpstr))
        if tmpstr == 'COLIN':
            print "pos " , pos
            print "score " , scoreMe(tmpstr)
        pos += 1
    f.close()
    print sumz

def scoreMe(name):
    scorez = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F': 6, 'G' : 7, 'H': 8, 'I': 9, 'J' : 10,
              'K': 11, 'L': 12, 'M' : 13, 'N': 14, 'O' : 15, 'P' : 16, 'Q': 17, 'R': 18, 'S' : 19,
              'T' : 20, 'U' : 21, 'V' : 22, 'W': 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    score = 0
    for x in range (len(name)):
        score += scorez[name[x]]
    return score
