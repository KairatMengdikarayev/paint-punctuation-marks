from sys import stdout
from time import sleep

from colorama import init, Fore, Style


init()
print(Fore.GREEN, Style.BRIGHT)

PUNCTUATION_MARKS = (
	".", 
	",", 
	"!", 
	"?", 
	"-",
	"—",
	":",
)

JOKE = (
"""Сорвались в пропасть два альпиниста — оптимист и пессимист. 
Пессимист: — Падаю... 
Оптимист: — Лечу!
"""
)

for i in JOKE:

	if i in PUNCTUATION_MARKS:
		print(Fore.RED + i, end="")
	
	else:
		print(Fore.GREEN + i, end="")
		
	stdout.flush()
	sleep(0.1)
