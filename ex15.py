#Importa do módulo 'sys' o parâmetro argv, muito útil pois permite que esse script seja chamado com valores diferentes.
from sys import argv
#Guarda o nome do script e o nome do arquivo.txt que vai ser chamado para essa atividade.
script,filename = argv

#Abre o arquivo.txt digitado no início. Depois de aberto, o arquivo passa a se comportar como um objeto pyhton.
txt = open(filename)

#Imprime na tela a frase a seguir.
print("Here\'s your file {}:".format(filename))
#Lê o conteúdo da variável txt com a função 'read()' e imprime na tela.
print(txt.readline())
#Fecha o arquivo aberto. É importante fechar os arquivos depois de feitas as alterações.
txt.close()

#Imprime na tela a frase a seguir
print(f"Type the {filename} again:")
#Recebe uma string do usuário e a atribui à variável 'file_again'.
file_again = input("> ")

#Abre o arquivo digitado e coloca seu conteúdo na variável 'txt_again'.
txt_again = open(file_again)

#Lê o conteúdo da variável 'txt_again' e imprime na tela.
print(txt_again.read())
#Fecha o arquivo aberto.
txt_again.close()