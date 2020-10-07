class FatorialInversa:

    def __init__(self,valor):
        self.valor = valor
    
    def fact_inv(self):

        if self.valor == 1:
            print('O resultado poder ser 0! ou 1!')
        
        elif self.valor <= 0: 
            print('Não é possível transformar em fatorial, pois o número disponibilizado é menor ou igual a zero!')
        
        else: 
            i = 1
            while self.valor % (i) == 0 and self.valor > 1:
                self.valor = self.valor/i 
                i += 1    
            if self.valor != 1:
                print('Não foi possível retornar um número fatorial')
            else:
                print('O número fatorial referente ao número fornecido é: {}'.format(i-1))

        return ''

valor = input()
valor = int(valor)

fat_inv = FatorialInversa(valor)

print(fat_inv.fact_inv())