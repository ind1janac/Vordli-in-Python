from colorama import init, Fore, Back, Style
import random
init()

loop = True
word_list = ["strah", "volan", "trava", "lampa", "tepih", "hrast", "tigar", "papir", "covek", "moron", "petak", "metak"]
while loop:
    print(Back.WHITE + Fore.BLACK + "Zelis li da igras? (da/ne)" + Style.RESET_ALL)
    command = input()
    if command == "ne":
        loop = False
    elif command == "da":
        inner_loop = 0
        word = random.choice(word_list)
        print("Unesi rec, ali pazi rec mora biti 5 slova ili vise!")

        while inner_loop < 6:

            attempt = input()

            # Logika igre
            output = ""
            for i in range(word.__len__()):
                if attempt[i] == word[i]:
                    output = output + Back.RED + attempt[i] + Back.RESET
                elif attempt[i] in word:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET
                else:
                    output = output + attempt[i] + Back.RESET
            print(output)
            if word == attempt:
                print("Cestitamo domacine, vidim gleda se slagalica")