#Exibição de números primos entre 1 e 200.
def achar_primos(intervalo):
    import math #Importação de biblioteca
    def is_prime(number):
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2): 
                if number % current == 0: 
                    return False
            return True
            return False
    primos = [primo for primo in list(range(intervalo)) #List comprehension.
                if is_prime(primo)] 
    return primos
if __name__ == '__main__':
    print(achar_primos(200))
