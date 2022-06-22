import forca
import adivinhacao


print("Olá, usuário(a).")

jogo= int(input("Escolha o jogo que deseja rodar: [1] Forca [2] Adivinhação: "))
if(jogo == 1):
 print("Jogo da forca selecionado")
 forca.jogo_forca()

elif (jogo==2):
    print("Jogo da adivinhação selecionado")
    adivinhacao.jogo_adivinhacao()