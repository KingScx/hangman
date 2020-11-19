import random

words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")

start = input('Type "play" to play the game, "exit" to quit: ')
while start != "play" and start != "exit":
    start = input('Type "play" to play the game, "exit" to quit: ')

while start == "play" or start == "exit":
    if start == "exit":
        break
    keyword = random.choice(words)
    key_list = list(keyword[:0] + '-' * len(keyword))
    tries = 8
    used = list()
    while tries:
        print()
        for i in key_list:
            print(i, end="")
        print()
        inp = input("Input a letter: ")
        if inp.islower() and len(inp) == 1:
            if inp in key_list or inp in used:
                print("You've already guessed this letter")
            elif inp in keyword:
                for i in range(len(keyword)):
                    if inp == keyword[i]:
                        key_list[i] = keyword[i]
            else:
                if inp not in used:
                    used.append(inp)
                    tries -= 1
                print("That letter doesn't appear in the word")
            if "-" not in key_list:
                print()
                print(f"""{keyword}
        You guessed the word!
        You survived!""")
                break
        elif (inp.isupper() or not inp.isalpha()) and len(inp) == 1:
            if inp not in used:
                used.append(inp)
                print("Please enter a lowercase English letter")
            else:
                print("You've already guessed this letter")
        elif len(inp) != 1:
            print("You should input a single letter")
    if "-" in key_list:
        print("You lost!")
    print()
    start = input('Type "play" to play the game, "exit" to quit: ')
    while start != "play" and start != "exit":
        start = input('Type "play" to play the game, "exit" to quit: ')