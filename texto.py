faturamento = 1000
custo = 600
lucro = faturamento + custo

#  texto = 'o lucro foi de ' + str (lucro) + ' e o faturamento foi de ' + str (faturamento)  'essa e uma forma de fazer'
texto = f' O Lucro foi de  R${lucro} e o Faturamento foi de R${faturamento:,.2f} '
print (texto)

email = 'email_FALSO@Gmail.coM    '

email = email.lower() # deixa todas letras minusculas  
email = email.strip() # ajustar os espaços indevidos ou intensionais do começo e do final da frase ou dois espaço em uma frase ele corrige

print (email)

#Tamanho
print (len(email)) #conta os caracteres  tem 

# Posiçao
posiçao = email.find('@') #Conta o posiçao da letra requisitada OBS. sempre começa a contando do Zero segunda OBs se tiver duas letras iguais ex (eu sou eu) tendo dois "E" o find vai identificar o apensas a primeira letra "E" que seria o numero "0"
print (posiçao)

#pedaços de um texto
print (email[0:12])       # o carateres '[]' serve para pegar o pedaço de um texto exemplo print(email[1]) eu pegaria o caracter 'U' e se fizer print(email[0:4]) ":" significa ate entao pegaria os caracter do 0 ao 4 que seria (eu sou )
#str (  vem de string vem de uma funçao que trasforma qualquer numero em forma de texto)   
novo_email = email.replace('falso', 'verdadeiro')
print(novo_email)
nome = 'jorge andre'
nome = nome.title() #deixa A primeira letra de todo texto maiuscula
#nome.capitalize() apenas a primeira letra do texto
#nome.upper() todas letras maiusculas
print(nome)
#descubra o servidor do email
posiçao = novo_email.find('@')
servidor = novo_email[posiçao+1:]
print(servidor)
#descobri o 1 nome
possiçao_do_espaço = nome.find(' ') 
primeiro_nome = nome[:possiçao_do_espaço]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)