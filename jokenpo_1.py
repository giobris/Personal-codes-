from random import randint

#Dicionário para traduzir:
comb = {'pedra': 0, 'papel': 1, 'tesoura': 2}
#Dicionario reverso:
comb_rev = {0:'pedra', 1: 'papel',2: 'tesoura'}

#Dicionario para ganhar:
vict_mac = {'0,1': 'CPU Ganhou', '0,2': 'Player 1 Ganhou', '1,0': 'Player 1 Ganhou', '1,2': 'CPU Ganhou', '2,0': 'CPU Ganhou' , '2,1': 'Player 1 Ganhou'}
vict_player = {'0,1': 'Player 2 Ganhou', '0,2': 'Player 1 Ganhou', '1,0': 'Player 1 Ganhou', '1,2': 'Player 2 Ganhou', '2,0': 'Player 2 Ganhou' , '2,1': 'Player 1 Ganhou'}


class Jokenpo:

    def jogador1(self,joga1):
        self.joga1 = comb[joga1]
        return self.joga1

    def jogador2(self, joga2):
        self.joga2 = comb[joga2]
        return self.joga2
    
    def machine(self, mac):
        self.mac = mac
        return self.mac
    

print('Olá, escolha 1 para Player vs CPU ou 2 para Player vs Player:')
n = input()
n = int(n)

lista = []

for i in range(0,n):
        print('Olá player {}, escolha: pedra, papel ou tesoura:'.format(i+1))
        lista.append(input().lower())
        
mac = randint(0,2)
if len(lista) == 1:
    joga1 = lista[0]
    jogo = Jokenpo()
    jogador1 = jogo.jogador1(joga1)
    machine = jogo.machine(mac) 
    if joga1 == comb_rev[mac]:
        print('\nJogador 1 jogou {} e CPU jogou {}'.format(joga1, comb_rev[mac]))
        print('Empatou')
    else:
        print('\nJogador 1 jogou {} e CPU jogou {}'.format(joga1, comb_rev[mac]))
        print(vict_mac['{},{}'.format(jogador1, machine)])
         
else:
    joga1 = lista[0]
    joga2 = lista[1]
    jogo = Jokenpo()
    jogador1 = jogo.jogador1(joga1)
    jogador2 = jogo.jogador2(joga2)
    if joga1 == joga2:
        print('\nJogador 1 jogou {} e Jogador 2 jogou {}'.format(joga1, joga2))
        print('Empatou')
    else:
        print('\nJogador 1 jogou {} e Jogador 2 jogou {}'.format(joga1, joga2))
        print(vict_player['{},{}'.format(jogador1, jogador2)])


