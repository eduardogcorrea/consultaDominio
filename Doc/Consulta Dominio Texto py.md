
## 📌 Visão Geral
Script Python para verificar em massa a disponibilidade de domínios `.br` via WHOIS, processando uma lista de entradas e salvando os resultados em um arquivo. Ideal para consultas automatizadas com proteção contra bloqueios por excesso de requisições.

---

## ✨ Funcionalidades Principais
- **Processamento em lote** de domínios a partir de um arquivo de texto
- **Saída formatada** em arquivo e console
- **Intervalo configurável** entre consultas (evita bloqueio)
- **Tratamento robusto** de erros e arquivos

---

## 🛠️ Requisitos Técnicos
- Python 3.x
- Permissão de rede (porta 43 TCP aberta)
- Acesso ao `whois.registro.br`

---

## 🚀 Como Usar

### Sintaxe Básica
```bash
python3 consultaDominioTexto.py arquivo_entrada.txt arquivo_saida.txt
```

### Exemplo Prático
```bash
python3 consultaDominioTexto.py dominios.txt resultados.txt
```

### Estrutura do Arquivo de Entrada (`dominios.txt`)
```text
exemplo.com.br
teste123.net.br
outrodominio.org.br
```

---

## ⚙️ Parâmetros
| Argumento          | Descrição                          | Obrigatório |
|--------------------|------------------------------------|-------------|
| `arquivo_entrada`  | Caminho do arquivo com lista de domínios (1 por linha) | Sim |
| `arquivo_saida`    | Caminho onde os resultados serão salvos | Sim |

---

## 📊 Formato da Saída
### Console (log em tempo real)
```text
exemplo.com.br: Registrado
teste123.net.br: Disponível
```

### Arquivo de Saída (`resultados.txt`)
```text
exemplo.com.br: Registrado
teste123.net.br: Disponível
outrodominio.org.br: Erro na consulta (timed out)
```

---

## ⚠️ Limitações e Boas Práticas
1. **Rate Limiting**:
   - Delay padrão: 2 segundos (alterável via parâmetro `delay`)
   - Recomendado para listas grandes: ≥3s de intervalo

2. **Dados Ocultos**:
   - Informações de titular podem estar parcialmente ocultas por LGPD

3. **Erros Comuns**:
   ```text
   Erro: Arquivo 'dominios.txt' não encontrado.
   Erro inesperado: [detalhe]
   ```

---

## 🔧 Personalização Avançada
### Modificar Intervalo
Altere o valor `delay` na chamada de `processa_lista()`:
```python
processa_lista(sys.argv[1], sys.argv[2], delay=3)  # 3 segundos
```

### Adicionar Metadados
Inclua timestamps nos resultados:
```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
out.write(f"[{timestamp}] {resultado}\n")
```

---

## 📌 Exemplo Completo
**Entrada** (`dominios.txt`):
```text
google.com.br
dominiolivre123.com.br
```

**Saída** (`resultados.txt`):
```text
google.com.br: Registrado
dominiolivre123.com.br: Disponível
```

**Console**:
```text
✓ Resultados salvos em 'resultados.txt'
```

---

## ❓ Suporte
Problemas? Verifique:
1. Conexão com `whois.registro.br:43`
2. Permissões de arquivo
3. Formatação do arquivo de entrada (UTF-8 recomendado)

Para uso profissional, considere a [API oficial do Registro.br](https://registro.br/tecnologia/ferramentas/api/).