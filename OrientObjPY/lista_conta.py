# -*- coding: utf-8 -*-
"""lista_conta

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ul9f2VSnprhd2UayjYJ_1Z3Cw-TGPGDh
"""

class ContaCorrente:
    def __init__(self,nome, codigo, saldo):
        self.nome = nome
        self.codigo = codigo
        self.saldo = saldo

    def deposita(self,valor):
        self.saldo += valor
        print(self.saldo)

    def __str__(self):
        return "[Nome: {} - Código: {} - Saldo: {}]".format(self.nome, self.codigo,self.saldo)

    def adiciona_100(contas):
        for conta in contas:
            conta.deposita(100)

def adiciona_100(contas):
        for conta in contas:
            conta.deposita(100)

conta_apeiron = ContaCorrente("Apeiron",40,150)
conta_vini = ContaCorrente("Vini",27,2000)
contas = [conta_apeiron, conta_vini]

print(contas[1])
print(contas[0])

adiciona_100(contas)
print(contas[1])
print(contas[0])


contas.insert(2,54)

print(contas[0], contas[1], contas[2])

contas.insert(0,27)

print(contas[0], contas[1], contas[2])

adiciona_100(contas)

"""**Listas e polimorfismo**"""

class Conta:
    def __init__(self, codigo, saldo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor
        print(self._saldo)

    def __str__(self):
        return "[ - Código:{} - Saldo: {:.2f}]".format(self._codigo, self._saldo)

    def printe(self):
        return "[ - Saldo: {:.2f}]".format(self._saldo)

class ContaCorrente(Conta):
    def vira_mes(self):
      self._saldo -= 2

class ContaPoupanca(Conta):
    def vira_mes(self):
      self._saldo *= 1.01
      self._saldo -=3

conta2 = ContaCorrente(2,0)

conta2.deposita(100)

conta2.vira_mes()

conta2.deposita(5)

conta5 = ContaPoupanca(5,0)

conta5.deposita(500)

conta5.vira_mes()

conta5.deposita(5)

conta_valor = [conta2, conta5]

for conta in conta_valor:
  conta.vira_mes()
  print(conta)

"""#array aula



"""

import array as arr

arr.array("d",[127,3.5])

!pip install numpy
import numpy as np
numeros = np.array([127,3.5])
numeros
numeros*2

"""Enumerando as idades"""

idades = [29,43,65,73,32,8,12,46]

for a in range(len(idades)):
  print(a,idades[a])

type(enumerate(idades))

list(range(len(idades)))

list()

idades = [29,43,65,73,32,8,12,46]

for a in range(len(idades)):
  print(a,idades[a])

type(enumerate(idades))

list(range(len(idades)))

list()

idades = [29,43,65,73,32,8,12,46]

for a in range(len(idades)):
  print(a,idades[a])

type(enumerate(idades))

list(range(len(idades)))

idades = [29,43,65,73,32,8,12,46]

for a in range(len(idades)):
  print(a,idades[a])

type(enumerate(idades))

list(range(len(idades)))

idades = [29,43,65,73,32,8,12,46]

for a in range(len(idades)):
  print(a,idades[a])


for numero, idade in enumerate(idades):
    print(numero,"x",idade)

