import sys
import os
from alive_progress import alive_bar
from colorama import Fore,Back,Style
usage = r"""
                            █
                     █      █            █
███ ███ ███ █ █ ███ ███     ███ ███ █ █ ███ ███
█   █   █   █ █ █ █  █  ███ █ █ █   █ █  █  ███
█   █   █   █ █ █ █  █      █ █ █   █ █  █  █
███ ███ █   ███ ███  ██     ███ █   ███  ██ ███
              █ █
            ███ █
                Bruteforce .cpt files
                Made by 0xsweat
usage : python3 ccrypt-brute.py [WORDLIST] [FILE]
"""
try:
    wordlist = sys.argv[1]
except:
    print(Fore.RED + "ERROR : No wordlist specified")
    print(Fore.BLUE + usage)
    quit()
try:
    encfile = sys.argv[2]
except:
    print(Fore.RED + "ERROR : No encrypted file specified")
    print(Fore.BLUE + usage)
    quit()
cvstep0 = open(wordlist, "r")
cvstep1 = cvstep0.read()
cvstep2 = cvstep1.split("\n")
cvstep0.close()
if str(encfile[-4:]) != ".cpt" and os.path.isfile(encfile) == True or os.path.isfile(encfile) == False:
    print(Fore.RED + "Invalid file type")
    quit() 
print(Fore.BLUE + "")
with alive_bar(len(cvstep2)) as bar:
    for z in range(len(cvstep2)):
        os.system("ccrypt -d -K '" + cvstep2[z] + "' " + encfile + " 2>/dev/null")
        fc = os.path.isfile(encfile)
        if fc == False:
            print(Fore.GREEN + "Cracked! password : " + cvstep2[z])
            quit()
        bar()
