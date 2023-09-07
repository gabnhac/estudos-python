from sys import argv
script,filename = argv

print(f"We're going to erase {filename}")
#Pressionar CTRL-C no teclado interrompe a execução do código.
print("If you don\'t want that, hit CTRL-C (^C).")
#Pressionar RETURN/ENTER continua o código.
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#Abre o arquivo digitado no início. Depois de aberto, um arquivo passa a se comportar como um objeto python. 
target = open(filename, "w")

print("Truncathing the file. GoodBye!")
#Limpa todo o conteúdo do arquivo.
target.truncate()

print("Now, I\'m going to ask you for three lines.")
#Recebe strings do usuário e as aloca nas variáveis a seguir.
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I\'m going to write this in the file.")
#Ecreve as strings recebidas do usuário no arquivo através do método/função 'write'.
target.write(line1,"\n",line2,"\n",line3,"\n")

print("And finally, we close it.")
#Fecha o arquivo.
target.close()