#!/usr/bin/env python3
import sys
import socket
import datetime

def consulta_whois(dominio):
    try:
        # Conecta-se ao servidor WHOIS do Registro.br
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('whois.registro.br', 43))
        
        # Envia a consulta
        s.send((dominio + '\r\n').encode())
        
        # Recebe a resposta
        resposta = b''
        while True:
            data = s.recv(4096)
            if not data:
                break
            resposta += data
        
        s.close()
        
        # Decodifica e analisa
        resposta = resposta.decode('utf-8', errors='ignore')
        
        if 'No match for' in resposta or 'NOT FOUND' in resposta:
            print(f"🟢 Domínio {dominio} está disponível!")
        else:
            print(f"🔴 Domínio {dominio} já registrado!")
            # Extrai informações relevantes
            for linha in resposta.split('\n'):
                if 'created:' in linha.lower():
                    print(f"   📅 Data de registro: {linha.split(':')[1].strip()}")
                if 'owner:' in linha.lower():
                    print(f"   👤 Titular: {linha.split(':')[1].strip()}")
    
    except Exception as e:
        print(f"⚠️ Erro na consulta: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dominio = sys.argv[1].lower()
        if not dominio.endswith('.br'):
            dominio += '.br'
    else:
        dominio = input("Digite o domínio (.com.br): ").strip().lower()
        if not dominio.endswith('.br'):
            dominio += '.br'
    
    consulta_whois(dominio)