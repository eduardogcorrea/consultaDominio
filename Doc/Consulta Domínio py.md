
## 📌 Visão Geral
Este script Python verifica a disponibilidade de domínios `.br` (como `.com.br`, `.net.br`) consultando diretamente o servidor WHOIS do **Registro.br** via protocolo TCP. Ele identifica se um domínio está registrado ou disponível e exibe informações adicionais quando registrado.

---

## 🛠️ Funcionalidades
- **Consulta WHOIS** em tempo real
- **Verificação de disponibilidade** de domínios `.br`
- **Exibição de detalhes** para domínios registrados:
  - Data de registro
  - Nome do titular (quando disponível)
- **Tratamento de erros** para conexões e formatos inválidos

---

## 📋 Requisitos
- Python 3.x
- Acesso à internet (para conexão com `whois.registro.br:43`)

---

## 🚀 Como Usar

### 1. **Execução Básica**
```bash
python3 consultaDominio.py exemplo.com.br
```

### 2. **Modo Interativo** (sem argumentos)
```bash
python3 consultaDominio.py
```
O script solicitará o domínio manualmente.

---

## 🖥️ Exemplos de Saída

### Domínio Disponível:
```
🟢 Domínio exemploteste123.com.br está disponível!
```

### Domínio Registrado:
```
🔴 Domínio google.com.br já registrado!
   📅 Data de registro: 11/01/1999
   👤 Titular: Google Brasil Internet Ltda.
```

### Erro:
```
⚠️ Erro na consulta: timed out
```

---

## ⚙️ Parâmetros
| Parâmetro         | Descrição                          | Exemplo                     |
|-------------------|------------------------------------|-----------------------------|
| `domínio`         | Domínio a ser consultado (com ou sem `.br`) | `exemplo.com.br` ou `exemplo` |

---

## 🔄 Fluxo do Script
1. **Validação do Domínio**:  
   - Adiciona `.br` automaticamente se não estiver presente.
2. **Conexão WHOIS**:  
   - Conecta-se ao servidor `whois.registro.br` na porta `43` (TCP).
3. **Análise da Resposta**:  
   - Busca por padrões como `No match for` (disponível) ou dados de registro.
4. **Exibição de Resultados**:  
   - Formata as informações de forma legível.

---

## ⚠️ Limitações
- **Bloqueio por consultas em massa**: O Registro.br pode bloquear IPs que façam muitas consultas em curto período. Recomenda-se:
  - Adicionar delays (ex.: `time.sleep(2)`) entre consultas.
  - Para listas grandes, use a [API oficial](https://registro.br/tecnologia/ferramentas/api/).
- **Dados de titular**: Podem estar ocultos devido à LGPD.

---

## 📝 Personalização
Para adaptar o script:
1. **Adicionar delays** (evitar bloqueio):
   ```python
   import time
   time.sleep(2)  # Antes de cada consulta
   ```
2. **Salvar resultados em arquivo**:
   ```python
   with open('resultados.txt', 'a') as f:
       f.write(f"{dominio}: Registrado\n")
   ```

---
## ❓ Suporte
Problemas? Abra uma *issue* no [GitHub](https://github.com/seu-usuario/repositorio) ou consulte a [documentação do Registro.br](https://registro.br/tecnologia/ferramentas/).