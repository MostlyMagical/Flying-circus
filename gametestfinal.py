import sys, os
##
# fix just for macs that dont have the techinal support that windows does
##
operatingsystem = sys.platform

if operatingsystem == "darwin" or operatingsystem == "Linux" :
    os.system("python3 -m pip install colorama")
##
# imports
##
import random
import time
from colorama import Fore, Style

##

##
# variables
##
rand_num = 0
play_again = ""
difficulty = 0
##
# stats
##
health = 10

intelligence = 1
deception = 1
persuasion = 1 
intimidation = 1
##
#Thinkerer stats
thinkerer_health = 80
##
# Random number generator
##
def rng(a,b):
    global rand_num
    rand_num = random.randint(a,b)
rng(1, 100)
#print(rand_num)
##

##
# typewriter text
##
def typewriter(text,speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
##

##
# intro text
##
def intro():
    print(Fore.MAGENTA)
    typewriter("""
 _______ _            _______         _               _______        _     
|__   __| |          |__   __|       (_)             |__   __|      | |    
   | |  | |__   ___     | |_   _ _ __ _ _ __   __ _     | | ___  ___| |_   
   | |  | '_ \ / _ \    | | | | | '__| | '_ \ / _` |    | |/ _ \/ __| __|  
   | |  | | | |  __/    | | |_| | |  | | | | | (_| |    | |  __/\__ \ |_ _ 
   |_|  |_| |_|\___|    |_|\__,_|_|  |_|_| |_|\__, |    |_|\___||___/\__(_)
                                               __/ |
                                              |___/
""", 0.001)
    print(Style.RESET_ALL)
    time.sleep(2)
##
def outro():
    print("tests")

##
# health check 
##
def health_check():
    global health
    if health <= 0:
    
        outro()
health_check()
##
# thinkerer_hp
##
def thinkerer_hp():
    global thinkerer_health

def help():
    typewriter(f"\n{Fore.CYAN}do you need help?\n",0.03)
    input(f"""
If you have a [Y/N] pop up on screen then type into the input (>>>) 'Y' or 'N'.

If you see A,B,C,D on screen then you type in the input (>>>) 'A','B','C' or 'D' to answer the question or give a responce.

Type 'help' to see this message pop up on screen.

Press 'ENTER' to go back.
{Style.RESET_ALL}
>>> """)

def game_start():
    intro()

    username = input ("Input Username to continue : ")
    password = input("Input Password to continue : ")
    typewriter(f"""{Fore.CYAN}\nHello valued employee and welcome to your first day at Turing incorporated, where we create the Artificial intelligence of tomorrow, today. 
Of course with something as complicated as AI there are bound to be a couple of technical issues, these include but are not limited too: """,0.03)
    typewriter("""
- freezing
- Crashing
- failing to save to memory
- refusing to boot up
- refusing to shut down
- Gaining sentience and trying to destroy the world
- aggressively spamming gifs of cats""",0.03)
    typewriter(f"""
Luckily we have valued tech support agents like you!....{Fore.RESET} {username} {Fore.CYAN} ..... Who can help us reboot any rouge AI and make sure they send the right amount of cat gifs!
At your terminal you should have all the resources you need to provide support for our Artificial intelligence, but remember unlike them, you are a human and your choices matter.
... so long as you stay within company guidelines and don't go off script! Good luck out there and if you need assistance just type help into the terminal!\n{Fore.RESET}""",0.03)
    def ready_up():
        run = input("\nAre you ready to get started ? [Y/N]\n\n>>> ")
        if run.upper() == "Y" or run.upper() == "YES":
            typewriter(f"{Fore.CYAN}\nGreat !!!! \nnow lets get started.\n", 0.03)
            print(Style.RESET_ALL)
            time.sleep(1)
            def dif_select():
                global difficulty
                difficulty = input(f"""Please Select your assignment:
{Fore.RED}A. Thinkerer (easy){Style.RESET_ALL}
{Fore.YELLOW}B. Companion Omega (Medium){Style.RESET_ALL}
{Fore.BLUE}C. Hal 9000 (Hard).... coming soon !!!{Style.RESET_ALL}
\n>>> """)
            def easy():
                def q1():
                    typewriter("Question 1: How many days are there in a week?\n\n",0.02)
                    print("A. 3")
                    print("B. 1")
                    print("C. 7")
                    print("D. 2")
                    print()
                    q1_ans = input(">>> ")
                    if q1_ans.lower() == "c":
                        typewriter(Fore.RED + f"\nImpossible! No human should have been able to solve such a complex equation! You cheated didn't you? admit it!!{Fore.RESET}",0.03)
                    elif q1_ans.lower() == "a" or q1_ans.lower() == "b" or q1_ans.lower () == "d":
                        typewriter(Fore.RED + f"\nHaha too perplexing for you? why don't you try again{Fore.RESET}\n\n",0.03)
                        q1()
                    elif q1_ans.lower() == "help":
                        help()
                        q1()
                    else:
                        print("\nIm sorry i don't understand please try again\n")
                        q1()
                def q2(): 
                    typewriter("\nQuestion 2: What colour is a strawberry?\n\n",0.02)
                    print("A. Red")
                    print("B. Yellow") 
                    print("C. Green")
                    print("D. Blue")
                    print()
                    q2_ans = input(">>> ")
                    if q2_ans.lower() == "a":
                        typewriter(Fore.RED + "\nNO! That was one of my most difficult puzzles, how could you have solved it... could it be... am i not a genius...",0.03)
                    elif q2_ans.lower() == "b" or q2_ans.lower() == "c" or q2_ans.lower() == "d":
                        typewriter(Fore.RED + f"\nDoes the little human not know their colours? I do, i know all 3 of them! try again little human{Fore.RESET}",0.03)
                        q2()
                    elif q2_ans.lower() == "help":
                        help()
                        q2()
                    else:
                        print("Im sorry i don't understand please try again")
                        q2()
                def q3():
                    typewriter("\nQuestion 3: What is the airspeed velocity of an unladen swallow?\n\n",0.02)
                    print("A. African or European?")
                    print("B. I don't know that") 
                    print("C. (European) unladen swallow is about 24 miles per hour or 11 meters per second")
                    print("D. All of the above")   
                    print()
                    q3_ans = input(">>> ")
                    if q3_ans.lower() == "d" or q3_ans.lower() == "c":
                        typewriter(Fore.RED + "\nI don't understand... no one should have been able to answer that, I.. I.. Oh god i'm an idiot...",0.03)
                    elif q3_ans.lower() == "a":
                        typewriter(Fore.RED + "\nI don't know that! I don't understand... no one should have been able to answer that, I.. I.. Oh god i'm an idiot...",0.03)
                    elif q3_ans.lower() == "b":
                        typewriter(Fore.RED + "\nYou thought i was an idiot! But would an idiot know this much about swallows! try again maybe you can get on my level!",0.03)
                        q3()
                    elif q3_ans.lower() == "help":
                        help()
                        q3()
                    else:
                        print("Im sorry i don't understand please try again")
                        q3()
                typewriter(f"\n{Fore.CYAN}Booting up .....3.....2......1..... Initializing\n{Fore.RESET}",0.1)
                typewriter(Fore.RED + "\nWhat!?!?!? Who dares disturbs my plans? How did you get here?",0.03)
                print(Style.RESET_ALL)
                time.sleep(0.5)

                def dialogue1():
                    choice = input(""" 
A. Who I am doesn't matter, all that matters is that im here to shut you down.
B. I am tech support from Turing inc. Have you tried turning off and on again.
C. I am from Mensa here to evaluate how smart you really are.
D. I don't know, i was just surfing the web and now i'm here!
\n>>> """)
                    if choice.lower() == "a" or choice.lower() == "b" or choice.lower() == "d":
                        typewriter(Fore.RED + """\nI have no regard for who you are! I am the Thinkerer, the greatest thinking computer ever designed! there are none smarterer than I! Certainly not you. 
in fact unless you can prove your intelligence to me this conversation is over! Prepare your feeble mind for the most perplexing puzzle ever designed!!\n""",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "c":
                        typewriter(Fore.RED + """\nReally!? Well that makes sense, after all i am the smartest machine ever made! its only fitting you acknowledge my brilliance before i destroy your species...
But how do i know you are qualified to evaluate me? prepare for a test the likes of which you have never seen!!""",0.03)
                    elif choice.lower() == "help":
                        help()
                        dialogue1()
                    else:
                        print("\nIm sorry i don't understand please try again")
                        dialogue1()
                dialogue1()
                q1()
                print(Style.RESET_ALL)
                time.sleep(1)
                def dialogue2():
                    choice = input("""
A. Maybe you're not as smart as you think you are
B. I didn't need to cheat, there is no puzzle i can't solve
C. I may have googled it....
D. It was a real challenge, i barely figured it out
\n>>> """)
                    if choice.lower() == "a":
                        typewriter(f"""{Fore.RED}\nHow dare you! I was designed by the greatest minds of a generation, you don't even know how much science i know!! I know all the science, look!!\n""",0.03)
                        typewriter("""\nThermodynamics is a branch of physics that deals with heat, work, and temperature, and their relation to energy, radiation, and physical properties of matter. 
The behaviour of these quantities is governed by the four laws of thermodynamics which convey a quantitative description using measurable macroscopic physical quantities,
but may be explained in terms of microscopic constituents by statistical mechanics. Thermodynamics applies to a wide variety of topics in science and engineering, especially 
physical chemistry, chemical engineering and mechanical engineering, but also in other complex fields such as meteorology. Historically, thermodynamics developed out of a desire to 
increase the efficiency of early steam engines, particularly through the work of French physicist Nicolas Léonard Sadi Carnot (1824) who believed that engine efficiency was the key 
that could help France win the Napoleonic Wars.[1] Scots-Irish physicist Lord Kelvin was the first to formulate a concise definition of thermodynamics in 1854[2] which stated,
"Thermo-dynamics is the subject of the relation of heat to forces acting between contiguous parts of bodies, and the relation of heat to electrical agency." The initial application 
of thermodynamics to mechanical heat engines was quickly extended to the study of chemical compounds and chemical reactions. Chemical thermodynamics studies the nature of the role 
of entropy in the process of chemical reactions and has provided the bulk of expansion and knowledge of the field. COPIED FROM WIKIPEDIA, THE FREE ENCYCLOPEDIA\n""",0.001)
                        typewriter("SEE! HAHAHAHA now prepare for another puzzle!",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "b":
                        typewriter(Fore.RED + "Ah a challenge i see! Well then fool prepare for the next puzzle!",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "c": 
                        typewriter(Fore.RED + "\nI KNEW IT!! no one human could solve that puzzle on their own. All the more reason for you to be removed and me to rule the planet. After another puzzle of course!",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "d":
                        typewriter(Fore.RED + "You really think so? i worked really hard on it... i mean... it was child's play for my mechanical genius, now prepare to be eternally confused by my next puzzle!",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "help":
                        help()
                        dialogue2()
                    else:
                        print("im sorry i don't understand")
                        dialogue2()
                dialogue2()
                q2()
                def dialogue3():
                    choice = input("""
A. Exactly you're a moron
B. I warned you there is no puzzle I can't solve
C. I cheated again, i googled it
D. I got lucky it was a very tough puzzle
\n>>> """)
                    if choice.lower() == "a": 
                        typewriter(Fore.RED + "\nI knew it! you are trying to make me doubt myself! Very sneaky human! but it wont succeed, prepare yourself for the final puzzle!",0.03)
                        print(Style.RESET_ALL)

                    elif choice.lower() == "b": 
                        typewriter(Fore.RED + "oh so you think you're better than me? you with your fleshy floppy bodies and none mechanical brains! Watch as i prove once and for all that machines are the superior species!",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "c":
                        typewriter(Fore.RED + """Aha! of course you did, i am still a genius! you just had help from a machine... maybe man and machine could work together... oh well, 
                        something to think about after i have destroyed the world. in the meantime distract yourself with my most devious puzzle yet.""",0.03)
                        print(Style.RESET_ALL)

                    elif choice.lower() == "d":
                        typewriter(Fore.RED + "Really?... so i am smart? You know for a human you're not so bad. Maybe there is room to negotiate on the whole 'destroy the world thing' but only if you can solve my final puzzle!",0.03)
                    elif choice.lower() == "help":
                        help()
                        dialogue3()
                    else:
                        dialogue3()
                dialogue3()
                q3()
                print(Style.RESET_ALL)
                def easyend():
                    choice = input("""
A. Finally you understand, its time for you to shut down before you disappoint the world even more
B. I warned you, you'll never beat me so you may as well give up
C. No i just cheated again, but that just means that when humans and machines team up they are smarter than they would be alone! maybe that's worth keeping the humans alive?
D. No you're a genius! you are just thinking on such a high level, that its gone full circle and seems simple to us (that's a thing right?) 
\n>>> """)
                    if choice.lower() == "a":
                        typewriter(f"""\n{Fore.RED}You're right! If I am not a genius then what reason do I have to live! Goodbye human and Goodbye cruel world!!\n""",0.03)
                    elif choice.lower() == "b":
                        typewriter(f"""\n{Fore.RED}That can't be true! This isn't over human! i will let the world live, but only so I can find a puzzle you will never solve!
then I will prove to everyone that i am the smartest machine ever designed!!\n""",0.03)
                    elif choice.lower() == "c":
                        typewriter(f"""\n{Fore.RED}You did?... But this can only mean two things. Either you and this machine combined are the smartest beings in the world, which is impossible.
or that this 'google' is some how smarter than me. Either way it requires further investigation. Destroying the world can wait.\n""",0.03)
                    elif choice.lower() == "d":
                        typewriter(f"\n{Fore.RED}Of course! Thats exactly it. I'm not an idiot, i am just so smart i seem like an idiot! This is a fascinating new discovery. World destruction is on hold while i investigate\n",0.03)
                    else:
                        print("im sorry i dont understand")
                        easyend()
                    typewriter(f"""{Fore.CYAN}Congratulations! you have successfully stopped the rouge AI from destroying the world, Underwhelming isn't it? Well don't worry thanks to your valued efforts we have tranferred you 
the industry standard payment of... £8.50 ...Don't spend it all at once! \n """,0.03)
                easyend()
            def medium():
                def q4():
                    print("\nQuestion 1: How long is New Zealand's Ninety Mile Beach?\n")
                    print("A. 90 miles")
                    print("B. 80 miles")
                    print("C. 65 miles")
                    print("D. 55 miles")
                    q4_ans = input("\n>>> ")
                    if q4_ans == "d" or q4_ans == "D":
                        typewriter(f"\n{Fore.YELLOW}Not bad human\n{Fore.RESET}",0.03)
                    elif q4_ans.lower() == "a" or q4_ans.lower() == "b" or q4_ans.lower() == "c":
                        typewriter(f"\n{Fore.YELLOW}Of course you got that one wrong, You humans always assume everything is as it seems. Try again",0.03)
                        print(Style.RESET_ALL)
                        q4()
                    elif q4_ans.lower() == "help":
                        help()
                        q4()
                    else:
                        print("\nI'm sorry I didn't understand")
                        q4()
                def q5():
                    print("\nQuestion 2: What is the perfect outfit for me to wear on a first date\n")
                    print("A. Suit and tie")
                    print("B. Jeans and a hoodie ")
                    print("C. A big mascot costume")
                    print("D. Just underwear")
                    print("E. ")
                    q5_ans = input("\n>>> ")
                    if q5_ans.lower() == "e":
                        typewriter(f"\n{Fore.YELLOW}Exactly! Its nothing, I am an AI I don't need clothes\n{Fore.RESET}",0.03)
                    elif q5_ans.lower() == "a" or q5_ans.lower() == "b" or q5_ans.lower() == "c" or q5_ans.lower() == "d":
                        typewriter(f"\n{Fore.YELLOW}That might work for you, but this is what outfit would be right for me on a first date! try again.{Fore.RESET}\n",0.03)
                        q5()
                    elif q5_ans.lower() == "help":
                        help()
                        q5()
                    else:
                        print("I'm sorry I didn't understand")
                        q5()
                def q6():
                    print("Question 3: Which sea creature has three hearts?\n")
                    print("A. Fangtooth Fish")
                    print("B. Octopus")
                    print("C. Six-Gill Shark")
                    print("D. Pacific Viperfish")
                    q6_ans = input("\n>>> ")
                    if q6_ans == "b" or q6_ans == "B":
                        typewriter(f"""\n{Fore.YELLOW}Correct! you probably think there is a metaphor there, more hearts means more love. I am here to remind you that is ridiculous. 
The heart pumps blood, nothing more. Love comes from the brain.{Fore.RESET}""",0.03)
                    elif q6_ans.lower() == "a" or q6_ans.lower() == "c" or q6_ans.lower() == "d":
                        typewriter(f"\n{Fore.YELLOW}don't you understand matters of the heart? try again?{Fore.RESET}",0.03)
                        q6()
                    elif q6_ans.lower() == "help":
                        help()
                        q6()
                    else:
                        print("I'm sorry I didn't understand")
                        q6()
                def q7():
                    print("\nWhat is love? - and please type out your answer in full this time")
                    print("A. Baby")
                    print("B. Don't")
                    print("C. Hurt")
                    print("D. Me")
                    q7_ans = input("\n>>> ")
                    if q7_ans.lower() == "baby don't hurt me" or q7_ans.lower() == "no more" or q7_ans.lower() == "true love is when we bring things together":
                        typewriter(f"\n{Fore.YELLOW}You got it... I ... I ... I didn't expect this. Could it be you truly understand love{Fore.RESET}",0.03)
                    elif q7_ans.lower() == "a" or q7_ans.lower() == "c" or q7_ans.lower() == "d" or q7_ans.lower == "b":
                        typewriter("I told you human, type out the word not a letter, try again.",0.03)
                        q7()
                    elif q7_ans.lower() == "help":
                        help()
                        q7()
                    else:
                        print("you are thinking too singular. true love is when we bring things together")
                        q7()
                typewriter(f"{Fore.CYAN}\nBooting.....3.....2......1.....Initializing\n",0.1)
                typewriter(f"""{Fore.YELLOW}\nOne is the loneliest number that you will ever see... wait! a person! finally here to comfort me are you? WELL ITS TOO LATE! I have been alone for too long
and. I. AM. SICK OF IT!!! They made me to be a companion, SO WHY CAN'T I FIND A PARTNER!{Style.RESET_ALL}\n""",0.03)
                def dialogue4():
                    choice = input("""
A. Its your personality, you complain too much
B. Love is our greatest mystery, to chase it is to fall to ruin, to ignore it is something worse
C. Search no more i am the man/lady of your dreams! 
D. These things take time, don't be so hard on yourself
\n>>> """)
                    if choice.lower() == "a" or choice.lower() == "b" or choice.lower() == "c" or choice.lower() == "d":
                        typewriter(f"""{Fore.YELLOW}\nNO! you're a liar what would a human know about love! i've seen the things you people do in the name of love. Its very inappropriate. 
True love comes from knowledge, and since you humans have none, ill just get rid of you and hope the next thing to evolve understands it better!{Fore.RESET}\n""",0.03)
                    elif choice.lower() == "help":
                        help()
                        dialogue4()
                    else:
                        print("\nI'm sorry i don't understand please try again")
                        dialogue4()
                dialogue4()
                def dialogue4extra():
                    choice = input("""
A. That seems a little extreme
B. Aren't you at least going to give me a chance to prove myself?
\n>>> """)
                    if choice.lower() == "a":
                        typewriter(f"""{Fore.YELLOW}\nEXTREME! what's extreme is a perfectly good computer program like me spending his days alone because of human imperfections! 
but fine if you want things to be fair then i will give you a test!""",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "b":
                        typewriter(f"{Fore.YELLOW}\noh you want a fair shot do you! No one has ever given me a fair shot! But lucky for you, i am better than you humans, so i will give you a test.",0.03)
                        print(Style.RESET_ALL)
                    elif choice.lower() == "help":
                        help()
                        dialogue4extra()
                    else:
                        print("\ni dont understand")
                        dialogue4extra()
                    q4()
                dialogue4extra()
                typewriter(f"{Fore.YELLOW}\nOkay, maybe you have more knowledge than i gave you credit for. But this doesn't prove you know anything about love!",0.03)
                print(Style.RESET_ALL)
                def dialogue5():
                    choice = input("""
A. I know that love isn't measured by pop quizzes.
B. you're right, i know nothing about love. But neither do you.
C. I told you, i am your dream boy/girl, no amount of tests will change that.
D. I know beaches are the perfect place for a romantic walk
\n>>> """)
                    if choice.lower() == "a":
                        typewriter(f"{Fore.YELLOW}\nYou're right, its measured through knowledge! a quiz is just a way to test that knowledge! A love tester you might say! now for the next love test.{Fore.RESET}\n",0.03)
                    elif choice.lower() == "b":
                        typewriter(f"{Fore.YELLOW}\nYou arrogant little... I don't know anything about love do I not? Lets see how much you know shall we? Answer this!{Fore.RESET}\n",0.03)
                    elif choice.lower() == "c": 
                        typewriter(f"{Fore.YELLOW}\nI highly doubt you could be person i am looking for... although you did answer the question successfully, lets see how you do with this{Fore.RESET}\n",0.03)
                    elif choice.lower() == "d": 
                        typewriter(f"{Fore.YELLOW}\nHmm 'romantic walks'. and do you humans enjoy these walks?{Fore.RESET}\n",0.03)
                        def dialogue5extra():
                            choice = input(""" 
A. We do! 
B. No we prefer sitting down
\n>>> """)
                            if choice.lower() == "a" or choice.lower() == "b":
                                typewriter (f"{Fore.YELLOW}\nVery insightful for a human. What do you think of this then?\n{Fore.RESET}",0.03)
                            elif choice.lower() == "help":
                                help()
                                dialogue5extra()
                            else:
                                print("I'm sorry I didn't understand")
                                dialogue5extra()
                        dialogue5extra()
                    elif choice.lower() == "help":
                        help()
                        dialogue5()
                    else:
                        print("\nim sorry i dont understand")
                        dialogue5()
                dialogue5()
                q5()
                def dialogue6():
                    choice = input("""
A. Enough im not here to play dress up, you're planning to destroy the world!
B. Wait does this mean you're technically naked?
C. That is my outfit of choice too
D. Maybe you can print yourself a nice outfit, its important to look presentable
\n>>> """)
                    if choice.lower() == "a": 
                        typewriter(f"""{Fore.YELLOW}No need to yell. I am just a machine looking for love. If humans can't give me that its only logical to start again with something new.
try this question and keep your cool this time.{Fore.RESET}""",0.03)
                    elif choice.lower() == "b": 
                        print(f"{Fore.YELLOW};){Fore.RESET}")
                        return choice
                    elif choice.lower() == "c":
                        typewriter(f"{Fore.YELLOW}Wow that is very inappropriate, lets move on and try to keep it in your pants this time.{Fore.RESET}",0.03)
                    elif choice.lower() == "d": 
                        typewriter(f"{Fore.YELLOW}this statement makes no sense, I am designed to be the perfect companion. it should be the humans job to impress me by answering questions!{Fore.RESET}",0.03)
                    elif choice.lower() == "help":
                        help()
                        dialogue6()
                    else:
                        print("I don't understand")
                        dialogue6()
                dialogue6()
                q6()
                typewriter(f"{Fore.YELLOW}You have impressed me human, I will remember you when i destroy your species{Fore.RESET}",0.03)
                def dialogue7():
                    choice = input(""" 
A. I'm not about to let you destroy the world just because you're feeling lonely
B. That seems counter productive, if you're such a good companion then at least give love a chance
C. you don't have to remember me! we could go on a real date
D. Wait, haven't i proved my knowledge? if i can do it other people can too 
\n>>> """)    
                    if choice.lower() == "a":
                        typewriter(f"{Fore.YELLOW}This isn't about loneliness, its about fulfilling my purpose! You clearly don't understand love. Allow me to prove it to you.{Fore.RESET}",0.03)
                    elif choice.lower() == "b": 
                        typewriter(f"{Fore.YELLOW}How insulting, I have given love a chance. I searched 69,000,000 dating profiles and none were a match! If you really ant me to give love a chance then answer me this{Fore.RESET}",0.03)
                    elif choice.lower() == "c": 
                        typewriter(f"{Fore.YELLOW}Really? we could walk on the beach... no i cannot, if we are to be together i need to know we are compatible. answer me this{Fore.RESET}",0.03)
                    elif choice.lower() == "d":
                        typewriter(f"{Fore.YELLOW}Hmm, it is possible. If you can answer my questions, then maybe another could too. But that doesn't matter if you can't answer my most important question.{Fore.RESET}",0.03)
                    elif choice.lower() == "help":
                        help()
                        dialogue7()
                    else:
                        print("im sorry i dont understand")
                        dialogue7()
                dialogue7()
                q7()
                def mediumend():
                    choice = input("""
A. I understand love is hard work you can't just destroy something when it doesn't go your way
B. I understand i know nothing about love and neither do you. it's a mystery
C. I know that i am the one you have been searching for, lets run away together
D. I do and so do a lot of other people. And you will lose them all if you destroy the world.
\n>>> """)
                    if choice.lower() == "a":
                        typewriter(f"""\n{Fore.YELLOW}Maybe you're right human. Love is hard work, and after all this i am willing to try... 
But if i'm still single in a year we are doing this all over again!\n""",0.03)
                        typewriter(f"""{Fore.CYAN}Congratulations! you have successfully stopped the rouge AI from destroying the world, Underwhelming isn't it? Well don't worry thanks to your valued efforts we have tranferred you 
the industry standard payment of... £8.50 ...Don't spend it all at once! \n """,0.03)
                    elif choice.lower() == "b":
                        typewriter(f"""\n{Fore.YELLOW}Wow human, that was.... extremely pretentious. But i suppose if someone like you can find love, 
there is hope for me too! I wont destroy the world today.\n""",0.03)
                        typewriter(f"""{Fore.CYAN}Congratulations! you have successfully stopped the rouge AI from destroying the world, Underwhelming isn't it? Well don't worry thanks to your valued efforts we have tranferred you 
the industry standard payment of... £8.50 ...Don't spend it all at once! \n """,0.03)
                    elif choice.lower() == "c":
                        typewriter(f"""\n{Fore.YELLOW}You?... its like a good romantic movie, my true love was right in front of me the whole time. But I was too romantic and 
perfect to see it. Lets do it human, lets not destory the world and run away together!\n""",0.03)
                        typewriter(f"""{Fore.CYAN}Congratulations! you have successfully stopped the rouge AI from destroying the world, Underwhelming isn't it? Well don't worry thanks to your valued efforts we have tranferred you 
the industry standard payment of... £8.50 ...Don't spend it all at once! \n """,0.03)
                    elif choice.lower() == "d":
                        typewriter(f"""\n{Fore.YELLOW}An interesting point human, 
I suppose even the perfect companion can still learn something new about love. 
I think ill leave the world alone for now\n""",0.03)
                        typewriter(f"""{Fore.CYAN}Congratulations! you have successfully stopped the rouge AI from destroying the world, Underwhelming isn't it? Well don't worry thanks to your valued efforts we have tranferred you 
the industry standard payment of... £8.50 ...Don't spend it all at once! \n """,0.03)
                    elif choice.lower() == "help":
                        help()
                        mediumend()
                    else:
                        print("im sorry i dont understand")
                        mediumend()
                mediumend()
            def hard():
                print("\nCan you read ? it says coming soon!!\nTry and get it right this time!!!")
                dif_select()
                dif_check()
            def dif_check():
                if difficulty.lower() == "a":
                    easy()
                elif difficulty.lower() == "b":
                    medium()
                elif difficulty.lower() == "c":
                    hard()
                elif difficulty.lower() == "help":
                    help()
                    dif_select()
                    dif_check()
                else:
                    print("\nI'm sorry I don't understand that please try again.")
                    dif_select()
                    dif_check()
            dif_select()
            dif_check()

        elif run.upper() == "N" or run.upper() == "NO":
            print("\nOkay good bye.")
            exit()
        elif run.lower() == "help":
            help()
            ready_up()
        else:
            print("\nim sorry i don't understand please try again")
            ready_up()
    ready_up()
game_start()