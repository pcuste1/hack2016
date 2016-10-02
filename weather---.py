def main():
    myFile = open("text.txt", 'r')
    for line in myFile:
        data = line.split('\t')
        print data[0]
        nw = data[2].split(' ')[1]
        #print nw
        if nw == 'N':
            print data[1] + '.' + data[2].split(' ')[0]
        else:
            print '-' + data[1] + '.' + data[2].split(' ')[0]
        es = data[4].split(' ')[1]
        #print es
        if es == 'W':
            print '-' + data[3] + '.' + data[4].split(' ')[0]
        else:
            print data[3] + '.' + data[4].split(' ')[0]
        #print data[1] + '.' + data[2].split(' ')[0]
        #print '-' + data[3] + '.' + data[4].split(' ')[0]
    cities = {}
main()
