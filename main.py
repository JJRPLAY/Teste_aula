import datetime
import datetime import date

print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
print(f"Vamos aprender Python juntos! {nome}!")
print("Qual area de programacao voce vai seguir?")
area: str = input("Digite a area de programacao: ")
print(f"Que legal, {nome}! Programar em {area} é muito interessante!")
print("Muito bem vamos fazer algumas atividades envolvidas com Python!\n")
print("Atividade 1: Crie um programa que peça para introduzir o seu ano de nascimento e diga a sua idade.\n")

def calcular_idade ():
    try:
        ano_atual = datetime.date.today().year
        ano_nascimento = int(input("Insira o seu ano de nascimento: "))
        idade = ano_atual - ano_nascimento
        print(f"Você tem {idade} anos.")
    except ValueError:
        print("Insira o ano em valores inteiros!")
while True:
    calcular_idade()
    continuar = input("Deseja calcular a idade novamente? (s/n): ").lower()
    if continuar != 's':
        print("Obrigado por participar!")
        break