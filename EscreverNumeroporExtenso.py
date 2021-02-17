# Escrito por: YGOR MOREIRA LIMA
# Graduacao em Sistemas de Informacao - UFF 2019.2
# Objetivo: Ler um número entre 0 e 99 e retornar o número por extenso
# eu@ygorlima.com.br

x = int(input("Digite um numero entre 0 e 99: "))
if 0<x<99:
	print("Numero valido.\n")
	if len(str(x)) == 1 and x ==0:
		print ("Zero")
	elif len(str(x)) == 1 and x ==1:
		print ("Um")
	elif len(str(x)) == 1 and x ==2:
		print ("Dois")
	elif len(str(x)) == 1 and x ==3:
		print ("Tres")
	elif len(str(x)) == 1 and x ==4:
		print ("Quatro")
	elif len(str(x)) == 1 and x ==5:
		print ("Cinco")
	elif len(str(x)) == 1 and x ==6:
		print ("Seis")
	elif len(str(x)) == 1 and x ==7:
		print ("Sete")
	elif len(str(x)) == 1 and x ==8:
		print ("Oito")
	elif len(str(x)) == 1 and x ==9:
		print ("Nove")
	if len(str(x)) == 2:
		unidade_ext = dict({0: "Zero", 1: "Um", 2: "Dois", 3: "Tres", 4: "Quatro", 5: "Cinco", 6: "Seis", 7: "Sete", 8: "Oito", 9: "Nove"})	
		dezena_ext = dict({2: "Vinte", 3: "Trinta", 4: "Quarenta", 5: "Cinquenta", 6: "Sessenta", 7: "Setenta", 8: "Oitenta", 9: "Noventa"})
		convertedez = str(x)
		dezenai = convertedez[0]
		unidadei = convertedez[1]
		dezena = int(dezenai)
		unidade = int(unidadei)
		if dezena == 1 and unidade == 1:
			print("Onze")
		elif dezena == 1 and unidade == 2:
			print("Doze")
		elif dezena == 1 and unidade == 3:
			print("Treze")
		elif dezena == 1 and unidade == 4:
			print("Catorze")
		elif dezena == 1 and unidade == 5:
			print("Quinze")
		elif dezena == 1 and unidade == 6:
			print("Dezesseis")
		elif dezena == 1 and unidade == 7:
			print("Dezessete")
		elif dezena == 1 and unidade == 8:
			print("Dezoito")
		elif dezena == 1 and unidade == 9:
			print("Dezenove")
		elif dezena > 1 and unidade != 0:
			print(str(dezena_ext[dezena] + ' e ' + unidade_ext[unidade]))
		elif dezena > 1 and unidade == 0:
			print(str(dezena_ext[dezena]))
		