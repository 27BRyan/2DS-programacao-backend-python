# For Loop com if (Condicional)
sucesso = False
for numero in range(3):
    print("Tentativa")
    if sucesso: # Dentro da variavel 'sucesso' está o valor booleano (True ou False)
        print("Sucesso!, meu jovem")
        break
else:
    print("Todas as 3 tentativas falharam!!!")