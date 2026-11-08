faturamento = 1100 #numero inteiro (int)
custo = 600
novas_vendas = 1000

faturamento = faturamento + novas_vendas
imposto = 0.15 * faturamento # float (numero casa decimal) (0.15 = a 15% exempemplo 0.20 igual a 20% )
lucro = faturamento - custo - imposto

print( 'imposto', imposto)
print('faturamento', faturamento)
print('custo',custo)
print('lucro',lucro)

mensagem = "o faturamento da loja foi de 2100" #string
teve_lucro = True #boolean

margem_lucro = lucro / faturamento

print('margem', margem_lucro )

anos = ( 310 // 12 ) # ou int (310 / 12)
print(anos,'anos' )

meses = 310 % 12

print( meses, "meses")


#print()= exiba na tela
# int = numero inteiros (exemplo 12,5 ele so pega o inteiro 12)
#round (arendodamento matematico exemplo se tiver 12,5 ele aredonda para 13)
# strings= texto
# boolean = valores boleanos que pode ser (True False)

# OPERADORES ESPECIAL
#mode-> % (EXEMPLO 310%12 ele so vai pegar o resto da divisao  tipo o int deu 25 anos ele vai pegar o resto que ficou pras tras os 10 mes)

#floor diivision -> // (igual ao int ele pega hmeros inteiros)
