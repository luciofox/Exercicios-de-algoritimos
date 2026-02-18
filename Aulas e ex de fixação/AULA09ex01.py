# --- 1. Definição da String na Memória ---
# Índices: 0123456789...
frase =   "Curso em Video Python"

# --- 2. Análise (Perguntas ao dado) ---
tamanho = len(frase)              # Retorna: 21
contagem_o = frase.count('o')     # Retorna: 3 (Video, Python)
posicao_py = frase.find('Python') # Retorna: 15 (Onde começa)
existe_curso = 'Curso' in frase   # Retorna: True

# --- 3. Fatiamento (A Régua de Corte) ---
# [inicio : fim (exclusivo) : passo]
fatia_video = frase[9:14]         # Pega índices 9,10,11,12,13 -> "Video"
fatia_pulo = frase[9:21:2]        # "VdoPto" (Pula de 2 em 2)

# --- 4. Transformação e Imutabilidade (A Fotocópia) ---
# A frase original NÃO muda aqui:
print(frase.upper())              # Imprime "CURSO EM VIDEO PYTHON"
print(frase)                      # Imprime "Curso em Video Python" (Original intacta)

# Para mudar, preciso sobrescrever ou criar nova variável:
frase_nova = frase.replace("Python", "Android")
# Agora frase_nova é "Curso em Video Android"

# --- 5. Manipulação Estrutural (Split & Join) ---
lista_palavras = frase.split()    # Vira lista: ['Curso', 'em', 'Video', 'Python']
junto_dnv = '-'.join(lista_palavras) # Vira string: "Curso-em-Video-Python"

print(f"Original: {frase}")
print(f"Fatia: {fatia_video}")
print(f"Juntado: {junto_dnv}")
