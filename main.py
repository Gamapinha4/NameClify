import os;
import re

print(chr(27) + "[2J")

directory_list = list()
mont_size = list()

def getItens(src):
    for root, dirs, files in os.walk(src, topdown=False):
      for indice, name in enumerate(files, start=1):
          if name.endswith(".SLDPRT"):
              
            nomeArquivoAntigo = str(root.split('_')[1][0] + root.split('_')[2][0])
            resultado = ''.join(x for x in src if x.isdigit()).zfill(2)
            
            pathNew = nomeArquivoAntigo + "." + resultado + "." + str(os.path.dirname(os.path.join(root,name)).split("\\")[::-1][0].split("_")[1]).zfill(2)  + "." + str(indice).zfill(2)
            text = pathNew + '  -  ' + str(os.path.join(root, name).split('\\')[::-1][0]) + '\n'
            
            if not name.startswith('subm_') & name.endswith('.SLDPRT'):
              mont_size.append(text)

def save_file(NDN, text):

    count = "01"
    f = open(NDN + '.txt', "w")

    f.write("Esse arquivo foi criado usando o NAMECLIFY! \n Criado por: Gabriel Palmieri \n \n \n \n")

    f.write('')
    f.write(' * Itens refentes a montagem 01 \n \n')

    for itens in text:
        if (itens.split('  -  ')[0].split('.')[1] != count):
            count = str(int(count) + 1).zfill(2)
            f.write('\n \n')
            f.write(' * Itens refentes a montagem ' + itens.split('  -  ')[0].split('.')[1] + '\n \n')
            f.write(itens + '\n')
            
        else:
            f.write(itens + '\n')
        
    f.close()

def getFolders(caminho):
    try:
        if os.path.exists(caminho):
            pastas = [f for f in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, f))]
            return pastas
        else:
            print("O caminho especificado não existe.")
            return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    
print("  _   _              __  __   ______    _____   _        _____   ______  __     __")
print(" | \ | |     /\     |  \/  | |  ____|  / ____| | |      |_   _| |  ____| \ \   / /")
print(" |  \| |    /  \    | \  / | | |__    | |      | |        | |   | |__     \ \_/ / ")
print(" | . ` |   / /\ \   | |\/| | |  __|   | |      | |        | |   |  __|     \   /  ")
print(" | |\  |  / ____ \  | |  | | | |____  | |____  | |____   _| |_  | |         | |   ")
print(" |_| \_| /_/    \_\ |_|  |_| |______|  \_____| |______| |_____| |_|         |_|   ")                                                                                 
print("\n                                                      Criado por: Gabriel Palmieri")  
print("                                                      Contato: https://github.com/Gamapinha4 \n \n")  

                      
print(" ╱╲      __  __   ___    ___     _       ")
print("╱  ╲    |  \/  | | __|  / __|   / \    ")
print("╲  ╱    | |\/| | | _|  | (__   / ᐱ \   ")
print(" ╲╱     |_|  |_| |___|  \___| /_/ \_\ Engenharia")
print("")
print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
print("║    IMPORTANTE:                                                                                                    ║▓")
print("║    ◦ Para que funcione corretamente, a base de arquivos deve seguir o padrão especificado no documento a seguir:  ║▓")
print("║                                                                                                                   ║▓")
print("║    https://drive.google.com/file/d/1khpeWpJX23K_hiRf8nay4L_ECBcTcZLG/view?usp=sharing                             ║▓")
print("║                                                                                                                   ║▓")
print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝▓")
print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

caminho = input('\n \n [CAMINHO] =>  INFORME O CAMINHO DA PASTA: \nR:') 

pastas = getFolders(caminho)

for pasta in pastas:
    caminho_completo = os.path.join(caminho, pasta)
    itens = getItens(caminho_completo)

if pastas is None:
    input('[ERRO] => Pasta não encontrada, pressione qualquer tecla para continuar.')

if pastas is not None:
    print("")
    print(f"As pastas em {caminho} são: {pastas}")
    print("")

response = input('[INFO] => Pressione qualquer tecla para continuar.')

count = "01"    

print("##############################################################")
print('')
print(' * Itens refentes a montagem 01' )
print('')

for itens in mont_size:
    if (itens.split('  -  ')[0].split('.')[1] != count):
        count = str(int(count) + 1).zfill(2)
        print('')
        print(' * Itens refentes a montagem ' + itens.split('  -  ')[0].split('.')[1])
        print('')
        print(itens)
    else:
        print(itens)

print("############################################################## \n \n")

response = input("[INFO] => Deseja salvar em um arquivo txt? (Sim ou Nao) \nR:")

if response == "Sim" or response == "sim" or response == "s":
    NDN = input("Digite o nome do arquivo... (NÃO COLOCAR FORMATOS COMO .TXT) \nR:")
    save_file(NDN, mont_size)
    print("\n [SUCESSO] => O Arquivo foi criado com sucesso. \n")
else:
    print("\n [CONCLUIDO] => Programa encerrado. \n")

nd = input("[CONCLUIDO] => Aperte qualquer tecla para fechar.")
    