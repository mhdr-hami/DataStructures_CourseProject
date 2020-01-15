# from Faze4 import *
#
# for person in personDictionary:
#     if personDictionary[person].job == "قاچاقچی":
print("I'm a matrix")
print("You can ask me to show you the facts I found from your dataset.")
print("Besides, I have 4 phase to run.")
print("Ask me questions or command me about them.")
print("----------------------------")
while True:
    x = input()
    x = x.lower()
    x = x.replace("faz", "faze")
    x = x.replace("phase", "faze")
    x = x.replace("phaze", "faze")
    x = x.replace("phaz", "faze")
    x = x.replace("please", "")
    x = x.replace("to", "")
    x = x.replace("and", "")
    # print(x)
    if x.__contains__("help") or (x.__contains__("what") and x.__contains__("you") and (not x.__contains__("fact")) or x == "?") or (x.__contains__("how") and x.__contains__("work")):
        print("I'm a matrix")
        print("You can ask me to show you the facts I found from your dataset.")
        print("Besides, I have 4 phase to run.")
        print("Ask me questions or command me about them.")
        print("----------------------------")
    elif x.__contains__("what") and x.__contains__("fact"):
        print("Ask me one to show you .")
        print("----------------------------")
    elif (x.__contains__("1") or x.__contains__("one") or x.__contains__("first")) and (x.__contains__("2") or x.__contains__("two") or x.__contains__("second")):
        print("you can ask for one phase at the time")
        print("----------------------------")
        continue
    elif x == "faze1" or x == "faze 1" or x == "faze one" or x == "first faze" or x == "one":
        print("you asked for shomare yek")
        print("----------------------------")
    elif x == "faze2" or x == "faze 2" or x == "faze two" or x == "second faze":
        print("you asked for shomare do")
        print("----------------------------")
    elif x.__contains__("show") or x.__contains__("print") or x.__contains__("do") or x.__contains__("start") or x.__contains__("run"):
        if x.__contains__("faze"):
            if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                print("you asked for shomare yek")
                print("----------------------------")
            elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                print("you asked for shomare do")
                print("----------------------------")
            else:
                print("which phase do you want?")
                x = input()
                if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                    print("you asked for shomare yek")
                    print("----------------------------")
                elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                    print("you asked for shomare do")
                    print("----------------------------")
                else:
                    print("that phase does not exist :)")
                    print("----------------------------")
        else:
            print("are you asking for showing phases?")
            y = input()
            if y.__contains__("ye"):
                if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                    print("you asked for shomare yek")
                    print("----------------------------")
                elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                    print("you asked for shomare do")
                    print("----------------------------")
                else:
                    print("I cant help you :)")
                    print("----------------------------")
            else:
                print("I cant help you :)")
                print("----------------------------")
    elif x.__contains__("hi") or x.__contains__("hello") and (not x.__contains__("bye")):
        print("hey there!")
        print("----------------------------")
    elif x.__contains__("bye"):
        print("ok!")
        print("Good bye!")
        print("----------------------------")
    elif x.__contains__("?"):
        y = x.split(" ")
        if y[0] == "can" or y[0] == "will" or y[0] == "would" or y[0] == "could" or y[0] == "do":
            if y[1] == "you":
                z = y[2].split("?")
                print("I can not", z[0], ":)")
                print("----------------------------")
            else:
                if x.__contains__("faze"):
                    print("are you asking for showing phases?")
                    y = input()
                    if y.__contains__("ye") and (not x.__contains__("no")):
                        if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                            print("you asked for shomare yek")
                            print("----------------------------")
                        elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                            print("you asked for shomare do")
                            print("----------------------------")
                    else:
                        print("I cant help you :)")
                        print("----------------------------")
                else:
                    print("are you asking for showing phases?")
                    y = input()
                    if y.__contains__("ye") and (not x.__contains__("no")):
                        if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                            print("you asked for shomare yek")
                            print("----------------------------")
                        elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                            print("you asked for shomare do")
                            print("----------------------------")
                        else:
                            print("what phase do you want me to show?")
                            x = input()
                            if x.__contains__("1") or x.__contains__("one") or x.__contains__("first"):
                                print("you asked for shomare yek")
                                print("----------------------------")
                            elif x.__contains__("2") or x.__contains__("two") or x.__contains__("second"):
                                print("you asked for shomare do")
                                print("----------------------------")
                            else:
                                print("that phase does not exist :)")
                                print("----------------------------")
                    else:
                        print("I cant help you :))")
                        print("----------------------------")
        else:
            print("I did not understand  you :)")
            print("----------------------------")
    else:
        y = x.split(" ")
        print("I can not", y[0], ":)")
        print("----------------------------")

