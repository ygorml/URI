# por Ygor Moreira Lima
# Objetivo: O usuário digita dois números e uma operação a ser realizada
# -*- coding:utf-8 -*-

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacao = input("Digite o símbolo da operação: ")
if operacao == "+":
	print(numero1+numero2)
elif operacao == "-":
	print(numero1-numero2)
elif operacao == "x":
	print(numero1*numero2)
elif operacao == "\\":
	print(numero1/numero2)
else:
	print("O símbolo não representa uma operação matemática\n")