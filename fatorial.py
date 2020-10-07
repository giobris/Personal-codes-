
class Fatorial:

    def __init__(self, valor):
        self.valor = valor

    def factorial(self):
        if self.valor < 0:
            print('Por favor, insira um valor maior ou igual a zero!')

        elif self.valor == 0:
            self.valor = 1

        else: 
            res = 1
            for i in range(0,valor):
                res *= i+1
                self.valor = res
        
        return self.valor


print('Olá, insira um número no qual você queira recebeu seu valor em fatorial:')
valor = input()
valor = int(valor)
fatorial = Fatorial(valor)

if valor > 0:
    print('O resultado é: {}'.format(fatorial.factorial()))


