import random

boards = [""",
>>>>>>>>>>>FORCA>>>>>>>>>>
+-----+
|  |
   | 
   |
   |
========""","""
+-----+
|  |
0  | 
   |
   |
========""","""

+-----+
|  |
0  | 
|  |
   |
========""","""
+-----+
|  |
0  | 
|  |
   |
========""","""
 +-----+
 |  |
 0  | 
/|  |
    |
========""","""
+-----+
 |  |
 0  | 
/|\ |
    |
========""","""
+-----+
 |  |
 0  | 
/|\ |
|   |
========""","""
+-----+
 |  |
 0  | 
/|\ |
| |  |
========""",""""
"""]
class Hangaman():
    def __init__(self,world): # construtor
        pass

    def guess(self,letra): # para advinhar a letra
        digitada= input("informe uma letra :  ")
        print(digitada)
        for letra in rand_word():
         if letra == rand_word():
          print(" muito bom continue assim",digitada)
        else:
          print("continue tentando",digitada)


    def hangman_over(self,letra): #  verificar se o jogo termino
        if letra == rand_word():
            print("jogo finalizado")
        else:
            print("jogo ativo")

    def hangman_won(self): # verificar se o jogador venceu
        pass
    def hide_word(self): # metodo para nao mostra letra no tabuleiro
        pass
    def print_game_status(self): # checar status do game e mostra o tabuleiro
        pass
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
  game = Hangaman(rand_word(),boards)
  game.guess('b')
  game.hangman_over()