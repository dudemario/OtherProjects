def luhn(num):
    flip = True
    total = 0
    s = ""
    for x in str(num):
        s = x + s
    print s
    for x in s:
        if flip == False:
            total += (int(x)*2)/10+(int(x)*2)%10
            flip = True
        else:
            flip = False

    print "Sum of Evens: ", total
    flip = True
    for x in s:
        if flip == True:
            total += int(x)
            flip = False
        else:
            flip = True
    print "Final Sum: ", total
    if (total % 10) == 0:
        print "Valid"
    else:
        print "Not valid"

def checkluhn(line):
    output = ""
    while line != "\n":
        print "'" + line + "'"
        flip = False
        total = 0
        s = ""
        newNum = ""
        counter = 0
        for x in line:
            if x == " ":
                line = line[counter + 1:]
                break
            else:
                newNum += x
                counter += 1
        for x in newNum:
            s = x + s
        for x in s:
            if flip == False:
                total += (int(x)*2)/10+(int(x)*2)%10
                flip = True
            else:
                flip = False

        print "Sum of Evens: ", total
        flip = False
        for x in s:
            if flip == True:
                total += int(x)
                flip = False
            else:
                flip = True
        print "Final Sum: ", total
        if total%10 == 0:
            output += "0"
        else:
            output += str(10 - (total % 10))
        print "Check Digit: ", output[-1]

    print output
    for x in xrange(5):
        print ""

def main():
    f = open('Codes.txt', 'r')
    line = f.readline()
    while line != "":
        checkluhn(line)
        line = f.readline()
    
main()
