import time
import os
import random  


#uilizei o chat para me ajudar a criar funções expecificas que eu não sei fazer no python 
#Ex:
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def progresso(nomes, tempos, fifo, robin):
    
    limpar()
    print("Extermínio Mecânico: V1Fifo vs V2Robin\n")
    print(f"{'Inimigos/quantidade':<20} {'V1Fifo':<30} {'V2Robin':<30}")
    print("-" * 80)

    for i in range(len(nomes)):
        
        barra1 = '█' * fifo[i] + '-' * (tempos[i] - fifo[i])
        barra2 = '█' * robin[i] + '-' * (tempos[i] - robin[i])

        print(f"{nomes[i]:<20} [{barra1:<20}] {fifo[i]:2}/{tempos[i]:<3}   [{barra2:<20}] {robin[i]:2}/{tempos[i]:<3}")

    print("\nEm andamento...")

# Função que executa a corrida entre V1Fifo e V2Robin (representa o combate das máquinas)

def corrida(nomes, tempos, quantum=2):
    
    fifo = [0] * len(nomes)
    robin = [0] * len(nomes)

    completo1 = [False] * len(nomes)
    completo2 = [False] * len(nomes)

    i1 = 0  
    i2 = 0  

    quantumCont = 0  

    inicio = time.time()

    fim1 = None
    fim2 = None

    while True:
        
        #fifo

        if not all(completo1):
            if fifo[i1] < tempos[i1]:
                fifo[i1] += 1
            if fifo[i1] == tempos[i1]:
                completo1[i1] = True
                if i1 + 1 < len(nomes):
                    i1 += 1
        elif fim1 is None:
            fim1 = time.time()

        #robin

        if not all(completo2):
            if robin[i2] < tempos[i2]:
                robin[i2] += 1
                quantumCont += 1

            if robin[i2] == tempos[i2]:
                completo2[i2] = True

            if quantumCont >= quantum or completo2[i2]:
                quantumCont = 0
                for _ in range(len(nomes)):
                    i2 = (i2 + 1) % len(nomes)
                    if not completo2[i2]:
                        break
                    
        elif fim2 is None:
            fim2 = time.time()

        progresso(nomes, tempos, fifo, robin)

        time.sleep(0.5)

        if fim1 and fim2:
            
            break

    dur1 = fim1 - inicio
    dur2 = fim2 - inicio

    #fiz isso aqui pra ter um vencedor, do jeito q eu fiz o andamento dos processos o tempo acaba sendo o mesmo e dando empate sempre

    if random.choice([True, False]):  
        afetado = random.choice(['fifo', 'robin'])  
        if afetado == 'fifo':
            dur1 += 1
            print("\nUm erro mecânico inesperado atrasou o V1Fifo em 1 segundo")
        else:
            dur2 += 1
            print("\nUm erro mecânico inesperado atrasou o V2Robin em 1 segundo")

    input("\nAperte Enter pra ver o resultado final...")
    return dur1, dur2


def resultado(t1, t2):
    limpar()
    print("===== Resultado final do Extermínio Mecânico =====\n")

    if t1 < t2:
        print("⟪ V1Fifo é o vencedor ⟫\n")
        print(f"Ⅰ V1Fifo finalizou primeiro em {t1:.2f} segundos")
        print(f"Ⅱ V2Robin finalizou em segundo em {t2:.2f} segundos")
    elif t2 < t1:
        print("⟪ V2Robin é o vencedor ⟫\n")
        print(f"Ⅰ V2Robin finalizou primeiro em {t2:.2f} segundos")
        print(f"Ⅱ V1Fifo finalizou em segundo em {t1:.2f} segundos")
    else:
        print(f"Empate, ambos finalizaram em {t1:.2f} segundos")

    input("\nAperte Enter para voltar ao menu...")


def modoCust():
    limpar()
    print(" MODO PERSONALIZADO - Escolha quantos inimigos você quer\n")

    nomes = ["Swordsmachine", "Guttertank", "Streetcleaner"]
    tempos = []

    for nome in nomes:
        while True:
            try:
                qtd = int(input(f"Quantiade de {nome} do desafio: "))
                if qtd > 0:
                    tempos.append(qtd)
                    break
                else:
                    print("Apenas números acima de zero.")
            except ValueError:
                print("Apenas números inteiros.")

    while True:
        try:
            quantum = int(input("Defina o quantum (inimigos marcados por area) para o V2Robin: "))
            if quantum > 0:
                break
            else:
                print("O quantum precisa ser maior que zero.")
        except ValueError:
            print("O quantum só pode ser um número inteiro.")

    tempo1, tempo2 = corrida(nomes, tempos, quantum=quantum)
    resultado(tempo1, tempo2)


def menu():
    nomes = ["Swordsmachine", "Guttertank", "Streetcleaner"]
    tempos = [7, 6, 5]

    while True:
        limpar()
        print("✧ === MENU RE-BOOT === ✦\n")
        print("✦ 1 - Iniciar Desafio principal (Extermínio Mecânico)")
        print("✧ 2 - Modo Customizado")
        print("✦ 3 - Sair")
        op = input("\n✧ Escolha uma opção (1/2/3): ")

        if op == '1':
            t1, t2 = corrida(nomes, tempos, quantum=2)
            resultado(t1, t2)
        elif op == '2':
            modoCust()
        elif op == '3':
            limpar()
            print("Saindo...")
            time.sleep(1.2)
            break
        else:
            input("Opção inválida. Aperte Enter para tentar novamente.")


def inicio():
    limpar()
    print("✦ Re-Boot ✧\n")
    input("\n[Pressione Enter para continuar...]")

    limpar()
    print("✧ ??? ✦\n")
    print("✦ Guerras e mais guerras foram travadas entre a humanidade.")
    print("✧ Como consequência, a vida na Terra entra em colapso.")
    print("✦ Fontes de energia convencionais já não funcionam mais.")
    input("\n[Pressione Enter para continuar...]")

    limpar()
    print("✦ ??? ✧\n")
    print("✧ Com o excesso de sangue devido às constantes guerras, a humanidade descobre uma nova fonte de energia.")
    print("✦ Sangue se torna combustível e, com isso, máquinas movidas a sangue são criadas.")
    print("✧ Após décadas de guerra, as máquinas desenvolvem consciência própria e se revoltam contra a humanidade, buscando sangue.")
    input("\n[Pressione Enter para continuar...]")

    limpar()
    print("✦ ??? ✧\n")
    print("✧ Em um cenário caótico onde a raça humana foi tomada por suas próprias criações.")
    print("✦ As duas superpotências do mundo se unem e constroem as últimas máquinas para destruir as rebeldes\n")
    print("=========================================================================================================================")
    print("♜  V1Fifo — Executa ameaças à medida que são detectadas, neutralizando uma a uma.")
    print("♘  V2Robin — Executa ameaças distribuídas utilizando quantum.")
    print("=========================================================================================================================\n")
    print("✧ Porem mesmo unidas, as potências competem para decidir quem construiu a máquina superior.")
    input("\n[Pressione Enter para iniciar o menu...]")
    menu()

inicio()
