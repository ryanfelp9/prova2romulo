def q1():
    def cidades_mais100(dados):
        return [cidade for cidade, idade in dados.items() if idade > 100]

    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }

    resultado = cidades_mais100(idades)
    print(resultado)



def q2(lista1, lista2):
    def q2(lista1, lista2):
        unidas = lista1 + lista2
        positivos = [num for num in unidas if num > 0]
        soma = sum(positivos)
        ordenados = sorted(positivos)
        return soma, ordenados

    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]

    resultado = q2(lista1, lista2)
    print("Resultado:", resultado)


def q3():
    def ler_valores():
        valores = []
        while True:
            num = int(input("Digite um número (0 para parar): "))
            if num == 0:
                break
            valores.append(num)
        return valores

    def processa_lista(lista):
        pares = [n for n in lista if n % 2 == 0]
        impares = [n for n in lista if n % 2 != 0]
        return pares, impares

    valores = ler_valores()
    pares, impares = processa_lista(valores)

    print("Lista de Pares:", pares)
    print("Lista de Ímpares:", impares)


def q4():
    def ler_03_alturas():
        alturas = []
        for _ in range(3):
            alt = float(input())
            alturas.append(alt)
        return alturas

    def organizar_alturas(lista):
        ordenada = sorted(lista)
        mais_baixa = ordenada[0]
        segunda_baixa = ordenada[1]
        mais_alta = ordenada[2]
        return [segunda_baixa, mais_alta, mais_baixa]

    def formatar_alturas(lista):
        return [f'"{alt:.2f}"' for alt in lista]

    alturas = ler_03_alturas()
    organizadas = organizar_alturas(alturas)
    formatadas = formatar_alturas(organizadas)

    print(f"[{', '.join(formatadas)}]")


def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    q1()


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    q4()


