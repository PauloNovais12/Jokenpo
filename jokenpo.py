import random as rd

def jogo():
    def jokenpo(ent):
        jog=[]
        if(ent==1):
            jog=str("Pedra")
        elif(ent==2):
            jog=str("Papel")
        elif(ent==3):
            jog=str("Tesoura")
        return jog
    x=[1,2,3]
    pc=rd.choice(x)
    print("Digite a numeração conforme o indicado!")
    print("1- Pedra")
    print("2- Papel")
    print("3- Tesoura")
    ent=int(input("Digite o numero que corresponde ao que você quer jogar: "))
    print("Você escolheu {}".format(jokenpo(ent)))
    print("O computador escolheu {}".format(jokenpo(pc)))
    usuario=jokenpo(ent)
    computador=jokenpo(pc)
    if(usuario==computador):
        return print("Empate, você e o computador escolheram o mesmo objeto")
    elif(usuario=="Pedra" and computador=="Tesoura"):
        return print("Você ganhou, Pedra ganha de Tesoura ")
    elif(usuario=="Tesoura" and computador=="Pedra"):
        return print("O Computador ganhou, Pedra ganha de Tesoura ")
    elif(usuario=="Papel" and computador=="Tesoura"):
        return print("O computador ganhou, Tesoura ganha de Papel")
    elif(usuario=="Tesoura" and computador=="Papel"):
        return print("Você ganhou, Tesoura ganha de Papel")
    elif(usuario=="Pedra" and computador=="Papel"):
        return print("O computador ganhou, Papel ganha de Pedra")
    elif(usuario=="Papel" and computador=="Pedra"):
        return print("Você ganhou, Papel ganha de Pedra")
#Saida da função, para criação de Loop
a=1
while a==1:
    jogo()
    print("Deseja continuar jogando? ")
    a=int(input("Digite 1-sim e 2-não: "))
    if(a!=1):
        print("Até mais")