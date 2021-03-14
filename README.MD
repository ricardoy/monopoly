# Ambiente

Desenvolvido em Python 3.9, sem dependências externas.

# Sobre a simulação

O tabuleiro é composto por 20 propriedades, com preços de compra e aluguel 
definidos por um sorteio aleatório de uma distribuição uniforme discreta, de
intervalos `(min_sell, max_sell)` e `(min_rent, max_rent)`, respectivamente.
O intervalo padrão para a compra é `(50, 90)` e, para o aluguel, `(100, 250)`.

# Rodando a simulação

```shell
python run_simulation.py [--min-sell <valor>] [--max-sell <valor>] [--min-rent <valor>] [--max-rent <valor>]
```