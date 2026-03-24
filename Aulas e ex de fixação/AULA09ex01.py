frase = 'Curso em Vídeo Python'

# --- 1. [início → incluso : fim → excluso (vai até fim - 1) : passo] | A seguir, temos regras de fatiamento:
frase[9]
frase[9:14] # Pega índices 9,10,11,12,13 -> "Video" # O segundo índice (14) é exclusivo, o que significa que a posição 14 não é incluída no resultado — paramos um índice antes dela.
frase[9:20] # O trecho frase[9:20] retorna os caracteres dos índices 9 a 19 (pois o 20 é exclusivo).
frase[9:21]
frase[9:21:2] # O fatiamento 'frase[9:21:2]' pega os caracteres do índice 9 até o 20 (pois 21 é exclusivo), saltando de 2 em 2. Os índices selecionados são: 9, 11, 13, 15, 17, 19, que correspondem a: 9: 'V'; 11: 'd'; 13: 'o'; 15: 'P'; 17: 't'; 19: 'o'; Resultado: 'VdoPto'.
frase[:5] # Ele vai do '0' até o '5' e citua o '5'. Citua espaço em '5'.
frase[15:] # Eu indico o início, mas não o final. Portanto, o Python vai ate o final da String.
frase[9::3] # Vai começar em '9', mas eu não caracterizei o final (logo, vai até o final da String) porque está '::' (imagine aqui '[9:]' + [9:NUM:3]); e aqui temos algo como [9:NUM:3], o mesmo que ocorre em 'frase[9:21:2]'.

# --- 2. Análise (Perguntas ao dado) ---

tamanho = len(frase) # Retorna: 21

contagem_o = frase.count('o') # Retorna: 3 (CURSo, VIDEo, PYTHoN)

frase.count('o',0,13) # ['o item que quer encontrar' : início : fim (lembrando, que este NUM não será incluído!)] # Exemplo: em '('o',0,13)' há só 1 'o' (foi até o 12; LEMBRE-SE sempre que no fatiamento o Python sempre ignora o último valor. Neste caso o '13', o qual engana muitos, fazendo acreditar ter 2 'o'!).

frase.find('Android') # Como não há essa palavra, o Python retorna "-1"; e você sabe que ele não começa na posição -1, mas sim, na posição 0, assim sendo, quando aparece -1, é o sinal que não há essa palavra ou/e não encontrou essa palavra!

posicao_py = frase.find('deo') # Retorna: 11 (Onde começa)

existe_curso = 'Curso' in frase # Retorna: True # Isso não é uma funcionalidade, mas um operador. Muito bom para fazer análise.

# --- 3. Transformação e Imutabilidade (A Fotocópia) ---

frase.replace("Python", "Android") # Agora frase_nova é "Curso em Video Android"

# A frase original NÃO muda aqui:
print(frase.upper())              # Imprime "CURSO EM VIDEO PYTHON"
print(frase)                      # Imprime "Curso em Video Python" (Original intacta)

# Para mudar, preciso sobrescrever ou criar nova variável:
frase.replace("Python", "Android") # Agora frase_nova é "Curso em Video Android"

frase.capitalize() # Vou explicar o que o método faz de forma genérica: ele coloca o primeiro caractere em maiúsculo e o restante em minúsculo. Logo, 1º: Identificar o primeiro caractere (neste caso é 'C') e garantir que esteja maiúsculo (já está); 2º: Converter todo o restante da string para minúsculo, e assim, a função cumpre com seu objetivo. Resultado: 'Curso em vídeo python'.


frase.title() # Preciso explicar o title() de forma clara: que ele coloca a primeira letra de cada palavra em maiúscula e as demais em minúscula. Na sua string 'Curso em Vídeo Python', o método identifica as palavras e aplica a capitalização em cada uma: "Curso" → já está com 'C' maiúsculo, resto minúsculo → "Curso"; "em" → 'e' vira maiúsculo → "Em"; "Vídeo" → 'V' maiúsculo (já está), 'í' minúsculo, etc. → "Vídeo" (mantém o acento); "Python" → 'P' maiúsculo, resto minúsculo → "Python". Resultado: 'Curso Em Vídeo Python'.


nova_frase = '   Aprenda Python  '
nova_frase.strip() # O método strip() remove espaços em branco do início e do fim da string. Portanto, '   Aprenda Python  ' se torna 'Aprenda Python' (sem os espaços iniciais e finais).


nova_frase.rstrip()
# Primeiro, entender o que é `rstrip()`: Esta função remove espaços em branco (ou outros caracteres especificados) do lado direito (final) da string.

# A analogia: imagine que a string é um tapete. O método `strip()` limpa as bordas (esquerda e direita). O `lstrip()` limpa só a borda esquerda (left). O `rstrip()` limpa só a borda direita (right). Vamos usar cores ou algo visual para destacar. Também explicar os significados:

# - "strip" em inglês significa "tirar a roupa", "despir", "remover". Em português, podemos pensar em "despir" a string dos espaços extras.
# - "r" é abreviação de "right" (direita).

# nova_frase = '   Aprenda Python  ' >> nova_frase.rstrip() >>> O resultado é: '   Aprenda Python'


nova_frase.lstrip()
# Primeiro, entender o que é `lstrip()`: Esta função remove espaços em branco (ou outros caracteres especificados) do lado esquerdo (início) da string.

# A analogia: imagine que a string é um tapete. O método `strip()` limpa as bordas (esquerda e direita). O `lstrip()` limpa só a borda esquerda (left). O `rstrip()` limpa só a borda direita (right). Também explicar os significados:

# - "strip" em inglês significa "tirar a roupa", "despir", "remover". Em português, podemos pensar em "despir" a string dos espaços extras.
# - "l" é abreviação de "left" (esquerda).

# nova_frase = '   Aprenda Python  ' >> nova_frase.rstrip() >>> O resultado é: 'Aprenda Python  '


# --- 4. Manipulação Estrutural (Split & Join) ---
lista_palavras = frase.split()    # Vira lista: ['Curso', 'em', 'Video', 'Python'] # O `split()` é como um descoplador que solta as conexões nos espaços, deixando cada palavra separada em sua própria caixinha (uma lista). [Curso]--(espaço)--[em]--(espaço)--[Vídeo]--(espaço)--[Python]

# Split (inglês) = dividir, partir, separar. Em português, podemos pensar que o método "fatiou" a frase em pedaços.


junto_dnv = '-'.join(lista_palavras) # Vira string: "Curso-em-Video-Python"

# O comando '-'.join(frase) usa o método join() para concatenar os elementos de um iterável, inserindo o separador '-' entre eles. Aqui, frase é a string 'Curso em Vídeo Python'. Em Python, strings são iteráveis, então ao iterar sobre frase, obtemos cada caractere individualmente (incluindo espaços). O join() vai colocar um hífen entre cada caractere. | Resultado: C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n | (Note que os espaços também são separados por hífens, então aparece - - onde há espaços.) (Note que os espaços também são separados por hífens, então aparece - - onde há espaços.) Se você fizesse frase.split() (sem argumentos), obteria ['Curso', 'em', 'Vídeo', 'Python']. Depois, se fizesse '-'.join(['Curso', 'em', 'Vídeo', 'Python']), o resultado seria 'Curso-em-Vídeo-Python'. Mas como aplicamos join() diretamente na string, o comportamento é diferente: ele age sobre cada caractere, não sobre palavras.
