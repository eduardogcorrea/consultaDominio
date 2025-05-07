#!/usr/bin/env python3
import socket
import time
import sys

def consulta_whois(dominio):
    try:
        dominio = dominio.strip().lower()
        if not dominio.endswith('.br'):
            dominio += '.br'
            
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('whois.registro.br', 43))
            s.send((dominio + '\r\n').encode())
            resposta = s.recv(4096).decode('utf-8', errors='ignore')
            
        if 'No match for' in resposta or 'NOT FOUND' in resposta:
            return f"{dominio}: Disponível"
        else:
            return f"{dominio}: Registrado"
            
    except Exception as e:
        return f"{dominio}: Erro na consulta ({str(e)})"

def processa_lista(arquivo_entrada, arquivo_saida, delay=2):
    try:
        with open(arquivo_entrada, 'r') as f:
            dominios = f.readlines()
            
        with open(arquivo_saida, 'w') as out:
            for dominio in dominios:
                if dominio.strip():  # Ignora linhas vazias
                    resultado = consulta_whois(dominio)
                    print(resultado)  # Mostra no console
                    out.write(resultado + '\n')  # Escreve no arquivo
                    time.sleep(delay)  # Intervalo entre consultas
                    
        print(f"\n✓ Resultados salvos em '{arquivo_saida}'")
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: ./verifica_dominios.py entrada.txt saida.txt")
        print("O arquivo de entrada deve conter um domínio por linha")
        sys.exit(1)
        
    processa_lista(sys.argv[1], sys.argv[2])