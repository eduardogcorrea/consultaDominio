#!/usr/bin/env python3
import sys
import time
import subprocess

def verifica_instalacao():
    try:
        import dns.resolver
        return True
    except ImportError:
        print("Instalando biblioteca dnspython...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "dnspython"])
            import dns.resolver
            return True
        except:
            print("\nErro: Não foi possível instalar dnspython automaticamente")
            print("Por favor instale manualmente com:")
            print("pip3 install dnspython")
            return False

def verifica_dns(dominio):
    try:
        import dns.resolver
        dominio = dominio.strip().lower()
        if not dominio.endswith('.br'):
            dominio += '.br'
        
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']  # DNS do Google
        resolver.timeout = 2
        
        try:
            resolver.resolve(dominio, 'A')
            return None
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return dominio
        except dns.resolver.Timeout:
            return f"{dominio} # Timeout"
            
    except Exception as e:
        return f"{dominio} # Erro: {str(e)}"

def main():
    if not verifica_instalacao():
        sys.exit(1)
        
    if len(sys.argv) != 3:
        print("Uso: ./filtra_disponiveis.py entrada.txt saida.txt")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as f:
            dominios = [d.strip() for d in f.readlines() if d.strip()]
        
        disponiveis = []
        for dominio in dominios:
            resultado = verifica_dns(dominio)
            if resultado and "#" not in resultado:
                disponiveis.append(resultado)
            elif resultado:
                print(f"[!] {resultado}")
            time.sleep(0.5)
                
        with open(sys.argv[2], 'w') as f:
            f.write('\n'.join(disponiveis))
        
        print(f"\n✓ {len(disponiveis)} domínios potencialmente disponíveis")
        print(f"Salvo em: {sys.argv[2]}")
    
    except FileNotFoundError:
        print("Erro: Arquivo de entrada não encontrado")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    main()