# por Ygor Moreira Lima
# Objetivo: Remover as vogais e retornar o texto

def anti_vowel(text):
	resultado = ""
	vogais = "aeiouAEIOU"
	for caractere in text:
		if caractere not in vogais:
			resultado += caractere
	return resultado

print anti_vowel("Testando")