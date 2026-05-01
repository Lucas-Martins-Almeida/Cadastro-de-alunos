alunos = [] # cria uma lista vazia para armazenar todos os alunos cadastrados

def classificar(nota): # cria uma função chamada classificar que recebe a nota
    if nota >= 7: # se a nota for maior ou igual a 7
        return "Aprovado" # retorna aprovado
    elif nota >= 5: # se a nota for maior ou igual a 5
        return "Recuperação" # retorna recuperação
    else:#se nenhuma condição acima acontecer
        return "Reprovado" # retorna reprovado


def media_turma(lista): # cria função para calcular média da turma
    soma = 0 # variável soma começa em 0
    for aluno in lista: # percorre cada aluno dentro da lista
        soma += aluno["nota"] # soma todas as notas
    return soma / len(lista) # retorna soma dividida pela quantidade de alunos

while True:  # laço principal do cadastro

    while True:  # laço para validar o nome
        nome = input("Digite o nome do aluno: ").strip()  # pede o nome

        if nome.replace(" ", "").isalpha():  # verifica se tem apenas letras
            break  # sai do laço do nome se estiver correto
        else: #se nome inválido
            print("Nome inválido. Digite novamente.")  # avisa erro

    

    while True: # inicia laço para validar idade
        try: # tenta executar
            idade = int(input("Digite a idade: "))  # pede idade e converte para inteiro
            if idade > 0:# verifica se idade é maior que zero
                break# sai do laço da idade
            else:# se idade inválida
                print("Idade inválida!")# mostra mensagem
        except:# se der erro de digitação
            print("Digite apenas números inteiros!")# mostra mensagem

    
    while True:# inicia laço para validar nota
        try:# tenta executar
            nota = float(input("Digite a nota: "))# pede nota e converte para decimal
            if nota >= 0 and nota <= 10:# verifica se nota está entre 0 e 10
                break# sai do laço da nota
            else:# se nota inválida
                print("Nota deve ser entre 0 e 10. Por favor Digite novamente")# mostra mensagem
        except:# se usuário digitar errado
            print("Oops, Digite apenas números!")# mostra mensagem

    situacao = classificar(nota)# chama função classificar e guarda resultado

    aluno = { # cria dicionário com dados do aluno
        "nome": nome, # chave nome recebe nome digitado
        "idade": idade, # chave idade recebe idade digitada
        "nota": nota, # chave nota recebe nota digitada
        "situacao": situacao # chave situação recebe classificação
    }

    alunos.append(aluno) # adiciona dicionário dentro da lista alunos

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()  # aceita S/N maiúsculo e remove espaços

    if continuar == "n":# se resposta for n
        break# encerra laço principal

print("\n--- RELATÓRIO FINAL ---")# pula linha e mostra título

aprovados = 0# contador de aprovados começa em zero
recuperacao = 0# contador de recuperação começa em zero
reprovados = 0# contador de reprovados começa em zero

for aluno in alunos:# percorre cada aluno da lista
    print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} | Situação: {aluno['situacao']}") # exibe os dados do aluno em uma única linha formatada
    print("-------------------")# separador visual

    if aluno["situacao"] == "Aprovado":# se aluno aprovado
        aprovados += 1# soma 1 no contador
    elif aluno["situacao"] == "Recuperação":# se aluno em recuperação
        recuperacao += 1# soma 1 no contador
    else:# se reprovado
        reprovados += 1# soma 1 no contador

media = media_turma(alunos)# chama função média

maior = alunos[0]["nota"]# assume primeira nota como maior
menor = alunos[0]["nota"]# assume primeira nota como menor
nome_maior = alunos[0]["nome"]# guarda nome da maior nota
nome_menor = alunos[0]["nome"]# guarda nome da menor nota

for aluno in alunos:# percorre lista novamente
    if aluno["nota"] > maior:# se nota atual for maior que a anterior
        maior = aluno["nota"]# atualiza maior nota
        nome_maior = aluno["nome"]# atualiza nome

    elif aluno["nota"] < menor:# se nota atual for menor que a anterior
        menor = aluno["nota"]# atualiza menor nota
        nome_menor = aluno["nome"]# atualiza nome

print(f"Média da turma: {media:.2f}")# mostra média com 2 casas decimais
print(f"Aprovados: {aprovados}")# mostra aprovados
print(f"Recuperação: {recuperacao}")# mostra recuperação
print(f"Reprovados: {reprovados}")# mostra reprovados
print("-------------------")# separador visual
print(f"Maior nota: {nome_maior} ({maior})")# mostra aluno com maior nota
print(f"Menor nota: {nome_menor} ({menor})")# mostra aluno com menor nota