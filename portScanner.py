#!/usr/bin/python3
import socket, sys
from IPy import IP
from colorama import init, Fore, Back, Style

print(Fore.YELLOW + "\n~ Welcome to PortScanner ~") 
print(Fore.YELLOW + "\nCreated By:") 
print(Fore.WHITE + " ____  _  _       ___")       
print(Fore.WHITE + "|  _ \| || | ____/ _ \ _ __") 
print(Fore.WHITE + "| |_) | || ||_  / | | | '__|")
print(Fore.WHITE + "|  _ <|__   _/ /| |_| | |   ")
print(Fore.WHITE + "|_| \_\  |_|/___|\___/|_|   ")

print(Fore.YELLOW + "\nWeb Page: https://juankaenel.com \n")
print(Fore.YELLOW + "[Info] Tool made in python to scan ports and services of a target or several \n")
print(Fore.YELLOW + "----------------------------------------------------------------------------------\n")            



def scan(target):
    """Chequea la ip llamando a la función y recorre los puertos asignados en el rango.
    """
    converted_ip = check_ip(target) #chequea la ip o dominio
    print('\n'+ Fore.YELLOW + '[*]' + Fore.RESET + ' Scanning target: ' + str(target))
    for port in range(20,81):
        scan_port(converted_ip,port)
        

def check_ip(ip):
    """Se encarga de chequear la ip o dominio
    
    En caso de ser una ip normal, solo se le pasa a la función IP que transforma a ip dicho parámetro
    En caso contrario lo atrapa la excepción returnando una función que devuelve la ip del dominio
    """
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024) # returna la información del servicio corriendo en el puerto

def scan_port(ip_address, port):
    """Escanea un objetivo o varios en busca de puertos abiertos y servicios corriendo.
        
    """
    try:
        sock = socket.socket() # descriptor socket+
        sock.settimeout(0.5) # cada 0.5 seg intenta la conexión
        sock.connect((ip_address,port)) # conexión
        try:
            banner = get_banner(sock) # variable banner que contiene información acerca del servicio corriendo en el puerto
            print(Fore.YELLOW+ '[+]' + Fore.RESET + ' Open port '+ str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print(Fore.YELLOW+ '[+]' + Fore.RESET + ' Open port '+ str(port))
    except:
        pass
    
        
if __name__ == "__main__":
    try:
        if len(sys.argv) != 1:
            print('[*] Use python3 ' + sys.argv[0])
            sys.exit(0)
        targets = input(Fore.RED+'[*] Enter target/s to scan (split multiple targets  with comma): ')
        if ',' in targets:
        # en caso que haya varios targets
            for ip_add in targets.split(','):   # devolvemos una lista separada por comas
                scan(ip_add.strip(' ')) # quitamos los espacios a la izquierda y derecha de cada ip
        else:
            # en caso que NO haya varios targets
            scan(targets)
    except KeyboardInterrupt:
        print(Fore.RED+'\n\n[*] Exiting the program... thanks for use this tool.\n')
        sys.exit(0)
