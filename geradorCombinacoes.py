#!/usr/bin/env python3
import itertools
import string

# Configurações
ARQUIVO_SAIDA = "dominios3.txt"
CARACTERES = string.ascii_lowercase + string.digits  # a-z + 0-9
TAMANHO = 3  # Combinações de 2 caracteres

# Gerar todas as combinações possíveis
combinacoes = [''.join(p) for p in itertools.product(CARACTERES, repeat=TAMANHO)]

# Criar domínios no formato XX.com.br
dominios = [f"{c}.com.br" for c in combinacoes]

# Salvar no arquivo (um por linha)
with open(ARQUIVO_SAIDA, 'w') as f:
    f.write('\n'.join(dominios))

print(f"✓ {len(dominios)} domínios gerados e salvos em '{ARQUIVO_SAIDA}'")
print(f"Exemplos: {dominios[0]}, {dominios[100]}, {dominios[-1]}")