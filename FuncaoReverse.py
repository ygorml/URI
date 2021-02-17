# Escrito por YGOR MOREIRA LIMA
# O objetivo do script é retornar uma string ao contrário, sem utilizar o método reverse
# -*- coding:utf-8 -*-
def reverse(text):
	size = len(text)
	texto = ""
	for i in range(1,size+1):
		texto = texto + text[size-i]
	return texto  
    
print reverse("Nao to nem ai")