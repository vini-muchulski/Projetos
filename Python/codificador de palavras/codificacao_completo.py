#unicode
import tkinter as tk



def codificar():

    palavra = entrada_palavra.get()

    lista = []

    for i in range (len(palavra)):
        lista.append(ord(palavra[i]))


    palavra_codificada = lista

    lb_valor_palavra_cod.config(text=palavra_codificada)


tela = tk.Tk()
tela.title("Codificação em Python")



lb_palavra = tk.Label(tela,text='palavra para ser codificada --', font = 'Helvetica, 16')
lb_palavra.grid(row=0,column=0,pady=5,padx=5)

lb_palavra_cod = tk.Label(tela,text='palavra codificada', font = 'Helvetica, 16')
lb_palavra_cod.grid(row=0,column=1,pady=5,padx=5)

lb_valor_palavra_cod = tk.Label(tela,text='----', font = 'Helvetica, 16')
lb_valor_palavra_cod.grid(row=1,column=1,pady=5,padx=5)

entrada_palavra = tk.Entry(tela, relief='solid', borderwidth=2,font='Helvetica, 10')
entrada_palavra.grid(row=1, column=0,sticky="we",pady=5,padx=5)

botao_codificar= tk.Button(tela, text="CODIFICAR", relief="raised", font = 'Helvetica, 16', bg='#0bf555',command=codificar)
botao_codificar.grid(row=2, column=0,sticky="we",pady=5,padx=5)



tela.mainloop()