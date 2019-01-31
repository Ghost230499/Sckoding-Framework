from sys import *
import sys
import inspect
import os

var_list = []

def goto():
    global line
    line = inspect.currentframe().f_back.f_lineno + 1

def gotoLine(linenum):
    global line
    line = linenum

def looping(filecontents):
    a = ''.join(filecontents)
    s = a.split(' ')

    that_index = 0
    using_index = 0
    loop = ""

    try:
        s.remove('from')
    except:
        goto()

    if s[0] == "create":
        try:
            that_index = s.index("that")
            loop = ' '.join(s[that_index + 81:])
            
        except:
            goto()
    
    if "using" in s:
        using_index = s.index("using")
        loop = ' '.join(s[:using_index])

    loopa = ''.join(loop)
    loops = loopa.split(' ')

    # print(loops)

    loop_text = ""
    
    loop_text += "for(int i = "
    loop_text += loops[1]
    if loops[1] < loops[3]:
        loop_text += "; i < "
    else:
        loop_text += "; i > "
    loop_text += loops[3]
    if loops[1] < loops[3]:
        loop_text += "; i++)"
    else:
        loop_text += "; i--)"

    print(loop_text)
    print("{")

    if loops[0].lower() == "print" or loops[0].lower() == "prints" or loops[0].lower() == "display" or loops[0].lower() == "show":
        print("cout << i;")

    print("}")

def inputs(filecontents):
    a = ''.join(filecontents)
    s = a.split(',')
    st = "cin"
    i = 0
    while i < len(s):
        st += " >> " + s[i]
        i = i+1
    st += ';'
    print(st)

def open_file(filename):
    data = open(filename, "r").read()
    return data

def printit(filecontents):
    print("cout << " + ''.join(filecontents) + ";")

# def sets_return(filecontents):
#     a = ''.join(filecontents)
#     s = a.split(' ')
#     if s[1] == "to" or s[1] == "as":
#         print(s[0] + " = " + s[2] + ";")
#     elif s[1] == '=':
#         st = s[0] + " = " + s[2]
#         i = 3
#         while i < len(s):
#             st += " " + s[i]
#             i = i+1
#         return st

def sets(filecontents):
    a = ''.join(filecontents)
    s = a.split(' ')
    if s[1] == "to" or s[1] == "as":
        print(s[0] + " = " + s[2] + ";")
    elif s[1] == '=':
        st = s[0] + " = " + s[2]
        i = 3
        while i < len(s):
            st += " " + s[i]
            i = i+1
        st += ";"
        print(st)

def initialize(filecontents):
    a = ''.join(filecontents)
    s = a.split(' ')

    # print(len(filecontents))
    if len(filecontents) == 1:
        print("int " + s[0] + ";")
        sys.exit(0)

    try:
        s.remove("as")
    except:
        goto()

    try:
        s.remove("=")
    except:
        goto()

    # print(s)

    try:
        if s[1] == "num" or s[1] == "number" or s[1] == "int":
            print("int " + s[0] + ";")
            sys.exit(0)
    except:
        goto()

    flag = 0

    try:
        if s[1] == "float" or s[1] == "decimal":
            print("float " + s[0] + ";")
            flag = 1
            sys.exit(0)
    except:
        goto()

    try:
        if s[1] == "string":
            print("string " + s[0] + ";")
            flag = 1
            sys.exit(0)
    except:
        goto()    

    try:
        if isinstance(int(s[1]), int) and flag == 0:
            print("int " + s[0] + " = " + s[1] + ";")
            sys.exit(0)
    except ValueError:
        try:
            if isinstance(float(s[1]), float) and flag == 0:
                print("float " + s[0] + " = " + s[1] + ";")
                sys.exit(0)
        except ValueError:
            if flag == 0:
                print("string " + s[0] + " = " + s[1] + ";")
                sys.exit(0)
        

def function(filecontents):
    a = ''.join(filecontents)
    s = a.split(' ')

    try:
        s.remove('a')
    except:
        goto()

    # print(s)

    parameter_index = 0
    for i in s:
        if i == "parameters" or i == "parameter" or i == "arguments" or i == "argument":
            parameter_index = s.index(i)

    para = s[parameter_index+1].split(',')

    # print(para)

    func_str = "void " + s[2] + "("

    if parameter_index == 0:
        func_str += ")"
    else:
        i = 0
        func_str += "int " + para[i]
        i += 1
        while i < len(para):
            func_str += ", int " + para[i]
            i += 1
        
        func_str += ")"

    print(func_str)

def ifelse(filecontents):
    a = ''.join(filecontents)
    s = a.split(' ')
    countifelse = 0
    countelse = 0
    operation = 0

    try: 
        i = 0
        while i < len(s) - 1:
            if s[i] == "else" and s[i+1] == "if":
                countifelse += 1
            i += 1    
    except:
        goto() #next line    

    try: 
        countelse = filecontents.count("else")
    except:
        goto() #next line

    str = "if (" + s[0] 
    if s[2].lower() == "greater" and s[4].lower() == "equal":
        str += " >= "
        str += s[6]
        operation = 1
    elif s[2].lower() == "less" and s[4].lower() == "equal":
        str += " <= "
        str += s[6]
        operation = 2
    elif s[2].lower() == "less":
        str += " < "
        str += s[4]
        operation = 3
    elif s[2].lower() == "greater":
        str += " > "
        str += s[4]
        operation = 4
    elif s[3].lower() == "equal":
        str += " != "
        str += s[5]
        operation = 5
    elif s[2].lower() == "equal":
        str += " == "
        str += s[4]
        operation = 6

    str += ")"
    print(str)
    print('{')

    first_then_index = s.index("then")
    first_else_index = len(s) - 1
    try:
        first_else_index = len(s) - (s[::-1].index("else")) - 1
    except:
        goto() #next line
    if s[first_then_index + 1].lower() == "set":
        # print(s[(first_then_index+2):(first_else_index+1)])
        i = first_then_index+2
        newstr = ""
        while i < first_else_index+1:
            newstr += s[i] + " "
            i = i+1
        sets(newstr)
    elif s[first_then_index + 1].lower() == "print" or s[first_then_index + 1].lower() == "display":
        # print(s[(first_then_index+2):(first_else_index+1)])
        i = first_then_index+2
        newstr = ""
        while i < first_else_index+1:
            newstr += s[i] + " "
            i = i+1
        printit(newstr)
    print("}")
    
    ifelse_index = []
    if countifelse > 0:
        i = 0
        while i < len(s) - 1:
            if s[i] == "else" and s[i+1] == "if":
                ifelse_index.append(i+2)
            i += 1  

    il = 0
    while il < len(ifelse_index):
        str2 = "else if (" + s[ifelse_index[il]]
        # print(str2)
        then_pos = ifelse_index[il]
        str_set = []
        while s[then_pos].lower() != "then":
            str_set.append(s[then_pos])
            then_pos += 1
        # str2 += sets_return(str_set)

        if str_set[2].lower() == "greater" and str_set[4].lower() == "equal":
            str2 += " >= "
            str2 += str_set[6]
            operation = 1
        elif str_set[2].lower() == "less" and str_set[4].lower() == "equal":
            str2 += " <= "
            str2 += str_set[6]
            operation = 2
        elif str_set[2].lower() == "less":
            str2 += " < "
            str2 += str_set[4]
            operation = 3
        elif str_set[2].lower() == "greater":
            str2 += " > "
            str2 += str_set[4]
            operation = 4
        elif str_set[3].lower() == "equal":
            str2 += " != "
            str2 += str_set[5]
            operation = 5
        elif str_set[2].lower() == "equal":
            str2 += " == "
            str2 += str_set[4]
            operation = 6

        str2 += ")"

        print(str2)
        print("{")
        # print(s[then_pos+1])
        # if s[then_pos+1].lower == "set":
        #     sets(' '.join(s[then_pos+2: (ifelse_index[il+1] - 2)]))
        
        # elif s[then_pos+1].lower == "print":
        #     print(' '.join(s[then_pos+2: (ifelse_index[il+1] - 2)]))

        str3 = []
        then_pos += 1
        while(s[then_pos] != "else"):
            str3.append(s[then_pos])
            then_pos += 1

        # print(''.join(str3[1:]))

        if str3[0].lower() == "set":
            sets(' '.join(str3[1:]))
        elif str3[0].lower() == "print":
            printit(' '.join(str3[1:]))

        print("}")

        il += 1

    if countelse - countifelse == 1: #else exists or not
        print("else")
        print("{")
        
        if s[len(s) - (s[::-1].index("else"))].lower() == "set":
            sets(''.join(s[(len(s) - (s[::-1].index("else"))+1):]))

        elif s[len(s) - (s[::-1].index("else"))].lower() == "print" or s[len(s) - (s[::-1].index("else"))].lower() == "display":
            printit(''.join(s[(len(s) - (s[::-1].index("else"))+1):]))
        print("}")

def lex(filecontents):
    filecontents = list(filecontents)
    # print(filecontents)
    # print(filecontents)
    if (''.join(filecontents[0:7])).lower() == "display": #display 5 + 6 + 5 + 75 * 97
        printit(filecontents[8:])
        sys.exit(0)
    if (''.join(filecontents[0:4])).lower() == "show": #show 5 + 6 + 5 + 75 * 97
        printit(filecontents[5:])
        sys.exit(0)
    if (''.join(filecontents[0:3])).lower() == "set": #set asfga = asfa + avas+ fas
        sets(filecontents[4:])
        sys.exit(0)
    if (''.join(filecontents[0:7])).lower() == "comment": #comment afsfas
        print("//" + ''.join(filecontents[8:]))
        sys.exit(0)
    if (''.join(filecontents[0:10])).lower() == "initialize": # initialize a as 123
        initialize(''.join(filecontents[11:]))
        sys.exit(0)
    if (''.join(filecontents[0:7])).lower() == "declare": # declare a as 123
        initialize(''.join(filecontents[8:]))
        sys.exit(0)
    try:
        if float(filecontents[0]) < 999999999999 or float(filecontents[0]) > -999999999999: #8 + 5.6 * 45
            printit(''.join(filecontents))
            sys.exit(0)
    except:
        goto() #next line
    if (''.join(filecontents[0:5])).lower() == "input": #input a, b, c
        inputs(''.join(filecontents[6:]))
        sys.exit(0)
    if (''.join(filecontents[0:2])).lower() == "if": #if percent is greater than 90 then set grade as "A+" else if percent is greater than 80 then set grade as "A" else if percent is greater than 70 then set grade as "B+" else if percent is greater than 60 then set grade as "B" else if percent is greater than 40 then print grade as "C" else print "You are fail"
        ifelse(''.join(filecontents[3:]))
        sys.exit(0)
    
    loop_found = 0
    function_found = 0
    for i in range(len(filecontents)): #create a loop that prints from 100 to 1 or print 1 to 100 using loop
        if filecontents[i].lower() == 'l' and filecontents[i+1].lower() == 'o' and filecontents[i+2].lower() == 'o' and filecontents[i+3].lower() == 'p':
            loop_found = 1
            looping(''.join(filecontents))
            sys.exit(0)

    for i in range(len(filecontents)): #create a loop that prints from 100 to 1 or print 1 to 100 using loop
        if filecontents[i].lower() == 'f' and filecontents[i+1].lower() == 'u' and filecontents[i+2].lower() == 'n' and filecontents[i+3].lower() == 'c' and filecontents[i+4].lower() == 't' and filecontents[i+5].lower() == 'i' and filecontents[i+6].lower() == 'o' and filecontents[i+7].lower() == 'n' and (''.join(filecontents[0:6]) == "create" or ''.join(filecontents[0:4]) == "make" or ''.join(filecontents[0:6]) == "define"):
            function_found = 1
            function(''.join(filecontents))
            sys.exit(0)

    if loop_found == 0 and function_found == 0:
        if (''.join(filecontents[0:5])).lower() == "print": #print 5 + 6 + 5 + 75 * 97
            printit(filecontents[6:])
            sys.exit(0)

    if (''.join(filecontents[0:4]).lower()) == "open" or filecontents[0] == '{':
        print("{")
        sys.exit(0)

    in_function_index = 0

    for i in range(len(filecontents)):
        if filecontents[i].lower() == 'i' and filecontents[i+1].lower() == 'n' and filecontents[i+2].lower() == ' ' and filecontents[i+3].lower() == 'f' and filecontents[i+4].lower() == 'u' and filecontents[i+5].lower() == 'n' and filecontents[i+6].lower() == 'c' and filecontents[i+7].lower() == 't' and filecontents[i+8].lower() == 'i' and filecontents[i+9].lower() == 'o' and filecontents[i+10].lower() == 'n':
            in_function_index = i + 11
            sys.exit(0)

    with open('somefile.txt', 'r+') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print(lines)
        # if last_line == "{" and in_function == 1:
        if last_line == '{':
            filecontents = filecontents[in_function_index+2:]
            print(filecontents)
            if (''.join(filecontents[0:6])).lower() == "return":
                print("return " + ''.join(filecontents[7:]) + ";")
                print("}")
            else:
                if (''.join(filecontents[0:7])).lower() == "display": #display 5 + 6 + 5 + 75 * 97
                    printit(filecontents[8:])
                    sys.exit(0)
                if (''.join(filecontents[0:4])).lower() == "show": #show 5 + 6 + 5 + 75 * 97
                    printit(filecontents[5:])
                    sys.exit(0)
                if (''.join(filecontents[0:3])).lower() == "set": #set asfga = asfa + avas+ fas
                    sets(filecontents[4:])
                    sys.exit(0)
                if (''.join(filecontents[0:7])).lower() == "comment": #comment afsfas
                    print("//" + ''.join(filecontents[8:]))
                    sys.exit(0)
                if (''.join(filecontents[0:10])).lower() == "initialize": # initialize a as 123 or a as 123.3 or a as satgas
                    initialize(''.join(filecontents[11:]))
                    sys.exit(0)
                if (''.join(filecontents[0:7])).lower() == "declare": # declare a as 123
                    initialize(''.join(filecontents[8:]))
                    sys.exit(0)
                if (''.join(filecontents[0:5])).lower() == "input": #input a, b, c
                    inputs(''.join(filecontents[6:]))
                    sys.exit(0)
                if (''.join(filecontents[0:2])).lower() == "if": #if percent is greater than 90 then set grade as "A+" else if percent is greater than 80 then set grade as "A" else if percent is greater than 70 then set grade as "B+" else if percent is greater than 60 then set grade as "B" else if percent is greater than 40 then print grade as "C" else print "You are fail"
                    ifelse(''.join(filecontents[3:]))
                    sys.exit(0)
                loop_found = 0
                function_found = 0
                for i in range(len(filecontents)): #create a loop that prints from 100 to 1 or print 1 to 100 using loop
                    if filecontents[i].lower() == 'l' and filecontents[i+1].lower() == 'o' and filecontents[i+2].lower() == 'o' and filecontents[i+3].lower() == 'p':
                        loop_found = 1
                        looping(''.join(filecontents))

                for i in range(len(filecontents)): #create a loop that prints from 100 to 1 or print 1 to 100 using loop
                    if filecontents[i].lower() == 'f' and filecontents[i+1].lower() == 'u' and filecontents[i+2].lower() == 'n' and filecontents[i+3].lower() == 'c' and filecontents[i+4].lower() == 't' and filecontents[i+5].lower() == 'i' and filecontents[i+6].lower() == 'o' and filecontents[i+7].lower() == 'n' and (''.join(filecontents[0:6]) == "create" or ''.join(filecontents[0:4]) == "make" or ''.join(filecontents[0:6]) == "define"):
                        function_found = 1
                        function(''.join(filecontents))


                if loop_found == 0 and function_found == 0:
                    if (''.join(filecontents[0:5])).lower() == "print": #print 5 + 6 + 5 + 75 * 97
                        printit(filecontents[6:])
    try:
        if (''.join(filecontents[0:5]).lower()) == "close" or filecontents[0] == '}':
            print("}")
            sys.exit(0)
    except:
        goto()

    # if (''.join(filecontents[0:5]).lower()) == "create a for loop":


def run():
    data = open_file("test.schok")
    lex(data)

run()