from despesa import Despesa
from calculo import Calculo

if __name__ == "__main__":
    desp = [Despesa('quarto', 1, 100),
            Despesa('quarto', 1, 100),
            Despesa('quarto', 2, 150),
            Despesa('quarto', 1, 170),
            Despesa('quarto', 5, 100.34),
            Despesa('quarto', 1, 130.6),
            Despesa('quarto', 1, 120.89),
            Despesa('quarto', 1, 110.12),
            Despesa('quarto', 1, 150.67),
            Despesa('quarto', 1, 100)]

    pessoas = ['maicon', 'vile', 'caju', 'joaquim', 'dudu', 'lucas', 'bb']

    calculo = Calculo()

    print(calculo.funcao(desp, pessoas))
