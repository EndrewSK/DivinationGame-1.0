def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('asciimatics')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('random')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('time')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('art')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('emoji')

from asciimatics.effects import Print
from asciimatics.particles import RingFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from random import randint, choice
import os
import time
import random
import emoji
from art import *


cmd = 'mode 100,30'
os.system(cmd)

initial = 0
final = 100


while True:
    def welcome():
        print ("\n\n\n\n\t\t", "*"*57)
        print ("\n\t\t\t  Seja bem-vindo(a) ao jogo de adivinhacão!")
        print ("\n\t\t", "*"*57)
    
    
    def name():
        while True:
            nickname = input ("\n\n\n\n\n\tDigite seu nome:\t")
            if nickname == "":
                print ("\n\tVocê precisa digitar seu nome!")
            else:
                while True:
                    crt = input ("\n\n\tEstá correto?\n\t-> ")
                    if crt == "sim":
                        print (f"\n\n\n\n\tCerto {nickname}, vou falar as instruções para jogar! :)")
                        time.sleep(3)
                        os.system('cls')
                        
                        def instructions():
                            while True:  
                                tent = 7
                                print (f"\n\n\n\n\n\n\n\t1 - Um número aleatório será sorteado e você terá {tent} tentativas para acertá-lo.")
                                print ("\n\t2 - Ao errar terá uma dica dizendo se o número sorteado é maior ou menor.")
                                print ("\n\t3 - Cada tentativa errada você perde uma tentativa.")
                                print ("\n\t4 - Quando acabar suas tentativas é game over hahaha, mas você pode reiniciá-lo.")
                                print ("\n\t5 - Se acertar o número sorteado, o jogo acaba.")
                                print ("\n\t6 - Só será aceito números inteiros.")
                                print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 20 segundos *")
                                time.sleep(20)
                                os.system('cls')
                                break
                            
                            while True:
                                try:
                                    quest = int (input ("\n\n\n\n\n\t1 - Jogar\n\t2 - Ver as intruções novamente\n\t3 - Sair\n\t-> "))
                                except ValueError as err:
                                    print("\n\tDigíte um Número inteiro!\n\n")
                                    time.sleep(1)
                                    os.system('cls')
                                    continue
                                if quest == 1:
                                    os.system('cls')
                                    def game():
                                        sort = random.randrange(initial, final)
                                        tent = 7
                                        gaming = text2art('''\n
   Jogo  da  Adivinhacao''', font="small")
                                        print(gaming)
                                        while True:
                                            try:
                                                chute = int (input (f"\n\n\n\tChute um número de {initial} a {final}\n\t-> "))
                                            except ValueError as err:
                                                print("\n\tDigíte um Número inteiro!\n\n")
                                                time.sleep(1)
                                                os.system('cls')
                                                continue
                                            if(chute>final or chute<initial):
                                                tent -= 1
                                                print(f"\n\tVocê precisa digitar um número entre {initial} e {final}")
                                                print("\tPerdeu uma tentativa hahaha")
                                                print(f"\n\tRestantam {tent} tentativas")
                                                print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 7 segundos *")
                                                time.sleep(7)
                                                os.system('cls')
                                                print(gaming)
                                            elif(chute!=sort):
                                                tent -= 1
                                                print("\n\n\tVocê errou feio hahahah")
                                                print("\tvocê é muito ruim!")
                                                print("\tVou te dar uma dica...")
                                                if(chute<sort):
                                                    print(f"\tO número sorteado é maior que {chute}")
                                                    print(f"\n\tRestantam {tent} tentativas")
                                                    print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 7 segundos *")
                                                    time.sleep(7)
                                                    os.system('cls')
                                                    print(gaming)
                                                elif(chute>sort):
                                                    print(f"\tO número sorteado é menor que {chute}")
                                                    print(f"\n\tRestantam {tent} tentativas")
                                                    print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 7 segundos *")
                                                    time.sleep(7)
                                                    os.system('cls')
                                                    print(gaming)
                                            elif(chute==sort):
                                                    print(f"\n\n\n\tboaa, você acertou {nickname}!")
                                                    print("\tParabéns, você é demais!")
                                                    print("\tOlha, não esperava que você fosse acertar...\n\tMas me surpreendeu haha\n")
                                                    print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 7 segundos *")
                                                    time.sleep(7)
                                                    os.system('cls')
                                                    def demo(screen):
                                                        scenes = []
                                                            
                                                        effects = [Print(screen,
                                                                SpeechBubble("Aperte \"x\" para voltar ao menu"),
                                                                y=screen.height - 3,
                                                                start_frame=60)]
                                                        
                                                        for _ in range(40):
                                                            fireworks = [(PalmFirework, 25, 30), (StarFirework, 25, 35), (RingFirework, 20, 30)]
                                                            
                                                            firework, start, stop = choice(fireworks)
                                                            
                                                            effects.insert(1, firework(screen, randint(0, screen.width), randint(screen.height // 8, screen.height * 3 // 4), randint(start, stop), start_frame=randint(0, 30)))

                                                        effects.append(Print(screen, FigletText("Incrivel"), y = screen.height // 2 - 7, speed=1, start_frame=30))
                                                        
                                                        effects.append(Print(screen, FigletText("Voce  ganhou !!"), y = screen.height // 3 + 6, speed=1, start_frame=30))
                                                        
                                                        scenes.append(Scene(effects))
                                                                    
                                                        scenes.append(Scene(effects, -1))

                                                        screen.play(scenes, stop_on_resize=True,allow_int=True)
                                                        
                                                    Screen.wrapper(demo)
                                                    break
                                            
                                            if(tent==0):
                                                print("\n\n\tHahahahahahaha")
                                                print("\tVocê perdeu!!")
                                                print("\tNem tenta denovo, você não consegue")
                                                print(f"\n\t o número era {sort}")
                                                print ("\n\n\n\t* Mensagem automática, a próxima tela será exibida em 10 segundos *")
                                                loser = text2art('''\n
    Loser''', font="slant")
                                                print(loser)
                                                time.sleep(10)
                                                os.system('cls')
                                                break
                                        while True:
                                            again = int (input ("\n\n\n\t1 - Jogar novamente\n\t2 - Ver as intruções\n\t3 - Sair\n\t-> "))
                                            if again == 1:
                                                time.sleep(1)
                                                os.system('cls')
                                                return game()
                                            
                                            elif again == 2:
                                                time.sleep(1)
                                                os.system('cls')
                                                return instructions()
                                            
                                            elif again == 3:
                                                print (emoji.emojize("\n\n\tAté mais! :face_blowing_a_kiss:"))
                                                Art2 = text2art('''\n\n\n\n\n\n\n\n\n
 --- Fim ---''', font="slant")
                                                print(Art2)
                                                time.sleep(3)
                                                os.system('cls')
                                                exit()
                                                
                                            else:
                                                print ("\n\n\n\tOpção inválida!")
                                                time.sleep(2)
                                                os.system('cls')
                                                continue
                                    game()
                                    break
                                
                                elif quest == 2:
                                    os.system('cls')
                                    return instructions()
                                
                                elif quest == 3:
                                    print (emoji.emojize("\n\n\tAté mais! :face_blowing_a_kiss:"))
                                    Art = text2art('''\n\n\n\n\n\n\n\n\n
 --- Fim ---''', font="slant")
                                    print(Art)
                                    time.sleep(3)
                                    os.system('cls')
                                    exit()
                                else:
                                    print ("\n\n\n\tOpção inválida!")
                                    time.sleep(2)
                                    os.system('cls')
                                    continue
                        instructions()
                        break
                    
                    elif crt == "nao":
                        time.sleep(1)
                        os.system('cls')
                        print ("\n\n\n\n\t\t", "*"*57)
                        print ("\n\t\t\t  Seja bem-vindo(a) ao jogo de adivinhacão!")
                        print ("\n\t\t", "*"*57)
                        return name()
                                                
                    else:
                        print ("\n\n\n\n\tDesculpe, não entendi")
                        print ("\tDigite \"sim\" ou \"não\"\n")
                        time.sleep(2)
                        os.system('cls')
                        continue
    welcome()
    name()
    break