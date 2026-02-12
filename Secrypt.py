
import random
import time
import os
from colorama import Fore, Style, init

TABLA = {
    'a': '¶', 'b': '‡', 'c': '©', 'd': 'Ð', 'e': '€', 
    'f': 'ƒ', 'g': '∞', 'h': '╫', 'i': '‼', 'j': '∫', 
    'k': '₭', 'l': '£', 'm': 'µ', 'n': 'ñ', 'o': 'ø', 
    'p': 'π', 'q': 'θ', 'r': '®', 's': '§', 't': '†', 
    'u': 'μ', 'v': '√', 'w': 'ω', 'x': '×', 'y': '¥', 
    'z': 'ζ', ' ': '░', '0': 'Ø', '1': '±', '2': '²', 
    '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', 
    '8': '⁸', '9': '⁹'
}

TABLA_REV = {v: k for k, v in TABLA.items()}

def cifrar(texto):
    texto = texto.lower()
    resultado = ""
    for letra in texto:
        resultado += TABLA.get(letra, letra)
    return resultado

def descifrar(codigo):
    resultado = ""
    for simbolo in codigo:
        resultado += TABLA_REV.get(simbolo, simbolo)
    return resultado

logo1 = Fore.RED + r""" ____  _____ ____ ____ ___  _ ____ _____ 
/ ___\/  __//   _Y  __\\  \///  __Y__ __\
|    \|  \  |  / |  \/| \  / |  \/| / \  
\___ ||  /_ |  \_|    / / /  |  __/ | |  
\____/\____\\____|_/\_\/_/   \_/    \_/  
                                         """
logo2 = Fore.MAGENTA + r"""   _____                            _   
  / ____|                          | |  
 | (___   ___  ___ _ __ _   _ _ __ | |_ 
  \___ \ / _ \/ __| '__| | | | '_ \| __|
  ____) |  __/ (__| |  | |_| | |_) | |_ 
 |_____/ \___|\___|_|   \__, | .__/ \__|
                         __/ | |        
                        |___/|_|        """
logo3 = Fore.CYAN + r"""  _____   ___    __  ____   __ __  ____  ______ 
 / ___/  /  _]  /  ]|    \ |  |  ||    \|      |
(   \_  /  [_  /  / |  D  )|  |  ||  o  )      |
 \__  ||    _]/  /  |    / |  ~  ||   _/|_|  |_|
 /  \ ||   [_/   \_ |    \ |___, ||  |    |  |  
 \    ||     \     ||  .  \|     ||  |    |  |  
  \___||_____|\____||__|\_||____/ |__|    |__|  
                                                """
logos = [logo1, logo2, logo3]
while True:
   os.system('cls')
   print(random.choice(logos) + Style.RESET_ALL)
   print(Fore.RED + "Made By Codetiz")

   print(Fore.GREEN + "1. Encrypt" + Style.RESET_ALL)
   print(Fore.CYAN + "2. Decrypt" + Style.RESET_ALL)
   print(Fore.RED + "3. Exit" + Style.RESET_ALL)
   opcion = input( Fore.YELLOW +">" + Style.RESET_ALL)

   if opcion == "1":
       os.system('cls')
       efecto1 = Fore.GREEN + "*" + Style.RESET_ALL
       msg = input("Message to encrypt:")
       print(efecto1 + "Encrypting" + Style.RESET_ALL)
       time.sleep(1)
       os.system('cls')
       print(f"Result: {cifrar(msg)}")
       input("Press Enter To Go Back")
   elif opcion == "2":
       os.system('cls')
       efecto2 = Fore.BLUE + "*" + Style.RESET_ALL
       cod = input("Received message:")
       os.system('cls')
       print(efecto2 + "Decrypting")
       time.sleep(1)
       os.system('cls')
       print(f"Result: {descifrar(cod)}")
       input("Press Enter To Go Back")

   if opcion == "3":
       os.system('cls')
       print(Fore.RED + "Closing" + Style.RESET_ALL)
       time.sleep(1)
       break