#modulos
from termcolor import colored, cprint 
import os
import random 
from datetime import date, timedelta
from tabulate import tabulate


#dados
data = []

#menu display
def menu_display():
    cprint("Seguradora Bacalhau | Menu Principal: ", "yellow") 
    print("1 - " + colored("Contratar novo seguro", "green"))
    print("2 - " + colored("Meus Contratos", "green"))
    print("3 - " + colored("Procurar Contrato", "green"))
    print("4 - " + colored("Sair", "red"))

#Formulario de Contrato
def formulario():
    cprint("Formulário de Contrato", "yellow")

    #dados do usuario
    nome_usuario = input(colored("Digite seu nome: ", "green"))
    endereco_usario = input(colored("Digite seu endereço: ", "green"))
    telefone_usuario = input(colored("Digite seu telefone: ", "green"))

    #sistema de I.A. seria implementada aqui
    foto = input(colored("Insira imagens da Bike: ", "green") + colored("ADCIONAR","red"))

    #gerar informações da apolice
    apolice_numero = str(random.randint(1000,9999))
    apolice_tipo = input(colored("Insira o tipo de apolice: ", "green"))
    data_de_inicio = date.today()
    data_de_termino = data_de_inicio + timedelta(days=5*365)
    data.append({"nome": nome_usuario, "endereco": endereco_usario, "telefone": telefone_usuario, 
                 "apolice_numero": apolice_numero, "apolice_tipo": apolice_tipo, 
                 "data_de_inicio": data_de_inicio.strftime("%d/%m/%Y"),
                 "data_de_termino": data_de_termino.strftime("%d/%m/%Y")})
    os.system("cls")
    cprint("Serviço contratado com sucesso!","yellow")
    cprint(f"Número da apólice: {apolice_numero}")
    skip = input(colored("Pressione enter para voltar", "green"))
    os.system("cls")
    
#Tabela com todos os dados cadastrados 

def todos_os_dados():
    cprint("Contratos no sistema", "yellow")
    print("")
    cabecalhos = ["Nome", "Endereço", "Telefone", "Numero da Apolice", "Tipo da Apolice", "Data de Inicio",
                  "Data de Termino"]
    tabela_data = []
    for item in data:
        tabela_data.append([item["nome"].capitalize(),item["endereco"], item["telefone"], 
                            item["apolice_numero"], item["apolice_tipo"], item["data_de_inicio"], 
                            item["data_de_termino"]])
        
    print(tabulate(tabela_data, headers=cabecalhos))
    print("")
    skip = input(colored("Pressione enter para voltar", "green"))
    os.system("cls")

#Procura
def procura():
    cprint("Procura de contrato: ", "yellow")
    procura = input(colored("Digite número da apólice: ", "green"))
    resultados = []

    for item in data:
        if procura in item["apolice_numero"]:
            resultados.append([item["nome"].capitalize(),item["endereco"], item["telefone"], 
                            item["apolice_numero"], item["apolice_tipo"], item["data_de_inicio"], 
                            item["data_de_termino"]])    
    if not resultados:
        cprint("Nao ha resultados.", "red")
    else:
        cabecalhos = ["Nome", "Endereço", "Telefone", "Numero da Apolice", "Tipo da Apolice", "Data de Inicio",
                  "Data de Termino"]
        print(tabulate(resultados, headers=cabecalhos))
        resultados =[]

    print("")
    skip = input(colored("Pressione enter para voltar", "green"))
    os.system("cls")



#main
def main():
    while True:
        menu_display()
        escolha = input(colored("Escolha uma opção: ", "green"))

        if escolha == "1":
            os.system("cls")
            formulario()
        elif escolha == "2":
            os.system("cls")
            todos_os_dados()
        elif escolha == "3":
            os.system("cls")
            procura()
        elif escolha == "4":
            os.system("cls")
            cprint("Obrigado por escolher a Bacalhau Seguradora", "blue")
            print("")
            cprint("Dados coletados", "green")
            print("")
            cabecalhos = ["Nome", "Endereço", "Telefone", "Numero da Apolice", "Tipo da Apolice", "Data de Inicio",
                  "Data de Termino"]
            resultados = []
            for item in data:
                resultados.append([item["nome"].capitalize(),item["endereco"], item["telefone"], 
                            item["apolice_numero"], item["apolice_tipo"], item["data_de_inicio"], 
                            item["data_de_termino"]])
            print(tabulate(resultados, headers=cabecalhos))
            print("")
            escolha_sair = input(colored("Deseja voltar? (S/N)", "green"))
            if escolha_sair.lower() == "s" or escolha_sair.lower() == "sim":
                os.system("cls")
            else:
                os.system("cls")
                cprint("Até a Proxima!", "magenta")
                break

        else:
            os.system("cls")
            cprint("Escolha inválida, tente novamente", "red")
if __name__ == "__main__":
    main()


