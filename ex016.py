"""
EU CONSEGUI FAZER DESSES 3 MODOS:

```python
valor = float(input('Digite o valor: '))  
print('O valor inteiro de {} é {:.0f}.'.format(valor, valor))

```

```python
from math import trunc  
valor = float(input('Digite o valor, fracionado, o qual quer somente ver o seu nº inteiro:'))  
valor_int = int(valor)
# desnecessária esta linha acima! Pois, embaixo usa-se: "trunc()".
print('O valor inteiro de {} é {}!'.format(valor, trunc(valor_int)))

```

```python
from math import trunc  
valor = float(input('Digite o valor, fracionado, o qual quer somente ver o seu nº inteiro:'))  
print('O valor inteiro de {} é {}!'.format(valor, trunc(valor)))

```
"""
valor = float(input('Digite o valor: '))
print('O valor inteiro de {} é {}!'.format(valor, int(valor)))
