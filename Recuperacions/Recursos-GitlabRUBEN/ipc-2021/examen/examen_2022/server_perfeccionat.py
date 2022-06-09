# /usr/bin/python
#-*- coding: utf-8-*-
# prog [-d|--debug] [-p|--port]
#------------------------------
# ASIX M06 Curs 2021-2022
# Exàmen Pràctic
# Enunciat:
#------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
#-------------------------------
parser = argparse.ArgumentParser(description="""Server01 Exàmen""")
# ULL L'ORDRE !! python3 -d examen.py SI,   pyton3 examen.py -d NO COLA !!!
parser.add_argument("-d","--debug",type=str, help="Descrivim tot el que està passant")
parser.add_argument("-p","--port",type=int,default=44444)
args=parser.parse_args()
#--------------------------------
llistaPeers=[]  # llista de conexions (per ara cap)
HOST = ''
PORT = args.port
def mysigusr1(signum,frame):  # 10) SIGUSR1 
  print("Signal handler called with signal:", signum)
  print(llistaPeers)
  sys.exit(0) # pleguem
def mysigusr2(signum,frame):  # 12) SIGUSR2
  print("Signal handler called with signal:", signum)
  print(len(llistaPeers))
  sys.exit(0) # pelguem
def mysigterm(signum,frame):  #15) SIGTERM
  print("Signal handler called with signal:", signum)
  print(llistaPeers, len(llistaPeers))
  sys.exit(0) # pelguem
#--------------------------------------------
pid = os.fork()
if pid !=0:
    if args.debug:
        print("Server Engegat:", pid)
    sys.exit(0)  # mor el procés pare i ens quedem amb el fill que és un dimoni en 2n pla

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid()) # new
MYEOT = bytes(chr(4), 'utf-8') # senyal de fi de transmissió de dades

while True:         # One by One 
    conn, addr = s.accept() # rebem una petició de conexió
    llistaPeers.append(addr) # guardem IP a llistaPeers per printar després
    if args.debug: # si esta el debug, printem per pantalla
        print("Connectat el host:", addr)
    while True:
        command = conn.recv(1024)  # esperem una consulta 
        #if not command:
        if command == b'\r\n':
            if args.debug:
                sys.stdout.write("Client finalitzat: %s \n" % (addr)) # new
            conn.close() # si s'envia res (un enter ?) donem per finalitzada la conexió amb client
            break  # sortim del while
        else:
            command  = command[:-1] #new, eliminem el \r\n  (cada "\algo" es 1 char !!)
            print(command)
            if command == b'processos':
                command = "ps ax"
            elif command == b'ports':
                command = "ss -plutn" # o netstat -puta
            elif command == b'whoareyou':
                command = "uname -a"    
            else:
                command = "uname -a"
                
            pipeData = Popen(command,shell=True,stdout=PIPE,stderr=PIPE) # executem l'ordre aquí en local i enviarem el resultat via pipe al client
            for line in pipeData.stderr:
                conn.send(line)
            for line in pipeData.stdout:  # L'enunciat no especifica si cal enviar els errors..
                conn.send(line)
            conn.send(MYEOT) # new, estava malament indexat
            
# respecte l'original: 
#  - S'ha afegit obtenir el PID per poder matar el dimoni (linea 46)
#  - S'ha tabulat la linea 73, ja que ha d'indicar fi de transmissió de dades desrpés d'enviar les dades no després de "no haver rebut comanda"
#  - Afegits més args.debug per cada print que escrivim per pantalla.
#  - El  #if not command: (linea 58) no funciona s'ha de dir que si arriba un enter (sense comanda) ADEU !
#  - De la linea 65 a la 73 s'han fer varies modificacions pq agafi les ordres correctament

# PROVES:
# SERVER:
# python3 <nom_programa> --> Ens dona el PID fil
#
# CLIENT:
# nc localhost 44444 --> port per defecte (ncat perquè ho possa al enunciat)
#   processos --> per ex