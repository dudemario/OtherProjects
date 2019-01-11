#Caesar Cipher
#Victor Sun
#May 30, 2016

plain = "abcdefghijklmnopqrstuvwxyz"        #alphabet
cap_plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    #capital letters
numbers = "0123456789"                      #numbers

def encript(word, key):
    ''' (string, number) -> string

    Returns the word encripted with the caeser cypher shifted "key" times

    >>> encript("Hi", 3)
    Kl
    
    >>> encript("yes sir 7", 66)
    msg gwf 3
    
    '''
    encripted = ""                          #output string
    for char in word:
        if char in plain:                   #checks if the character is a lower-case letter
            place = plain.index(char)       #takes the index of each letter
            place += key                    #changes index to match shift
            while place >= 26:              #checks if the index is larger than the alphabet
                place -= 26                 #starts the alphabet all over
            encripted += plain[place]       #stores the changed letter into the output string
        elif char in cap_plain:             #checks if the character is a capital letter
            place = cap_plain.index(char)   #
            place += key                    #
            while place >= 26:              #IBID
                place -= 26                 #
            encripted += cap_plain[place]   #
        elif char in numbers:               #checks if the character is a number
            place = numbers.index(char)     #
            place += key                    #
            while place >= 10:              #IBID
                place -= 10                 #
            encripted += numbers[place]     #
        else:
            encripted += " "                #prints a space if the character is a space or an unknown symbol
    print(encripted)                        #prints out the encripted word
encript("Yes sir 7", 66)                    #test

def decript (word, key):
    ''' (string, number) -> string

    Returns the word decripted with the caeser cypher shifted "key" times

    >>> decript("Kl", 3)
    Hi
    
    >>> decript("msg gwf 7", 66)
    yes sir 7
    '''
    decripted = ""                          #output string
    for char in word:
        if char in plain:                   #checks if the character is a letter of the alphabet
            place = plain.index(char)       #takes the index of each letter
            place -= key                    #changes index to match shift
            while place < 0:                #checks if the index is larger than the alphabet
                place += 26                 #starts the alphabet all over
            decripted += plain[place]       #stores the changed letter into the output string
        elif char in cap_plain:             #checks if the character is a capital letter
            place = cap_plain.index(char)   #
            place -= key                    #
            while place < 0:                #IBID
                place += 26                 #
            decripted += cap_plain[place]   #
        elif char in numbers:               #checks if the character is a number
            place = numbers.index(char)     #
            place -= key                    #
            while place < 0:                #IBID
                place += 10                 #
            decripted += numbers[place]     #
        else:                           
            decripted += " "                #prints a space if the character is a space
    print(decripted)                        #prints out the encripted word
decript("Msg gwf 3", 66)                      #test