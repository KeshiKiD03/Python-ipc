# /usr/bin/python
#-*- coding: utf-8-*-
#
# 13-popen-sql-injectat.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
# Utilitza el docker edtasixm06/postgres
# -----------------------------------------
#commandLocal = "psql -qtA -F ';' lab_clinic -c 'select * from pacients;'"
#commandRemote = "psql -qtA -h i11 -U postgres -F ';' lab_clinic -c 'select * from pacients;'"
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse
parser = argparse.ArgumentParser(description='Consulta SQL interactiva')
parser.add_argument('sqlStatment', help='Sentència SQL a executar',metavar='sentènciaSQL')
args = parser.parse_args()
#----------------------------------------------------------
cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres  training"
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
pipeData.stdin.write("select * from oficinas;\n\q\n")
for line in pipeData.stdout:
  print(line, end="")
sys.exit(0)


# SOLUCIÓN
"""
  1. Se importa SYS y desde subproceso, Popen y PIPE.
  2. Se importa también argparse.
  3. Se inicializa el ARGPARSE con una descripción.
  4. Se añade un argumento que será una sentencia SQL, será posicional.
  5. La entrada estándar, salida estándar y salida de error será PIPE.
  6. En la entrada estándar, hacemos un WRITE hacemos una sentencia SQL. --> \n --> Salto de línea y \q es ENTER y \n salto de línea.
  7. Se recorre con un for la salida estándar de cada línea y se printa.
"""



"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**13-popen-sql-injectat.py  consulta**

  Fer que la sentència sql a fer sigui un argument tot entre cometes 
  que es passa com a argument.
  sql injectat: perills d’injectar codi d’usuari en els programes.

# ----------------------------------------------

## Explicación

**13-popen-sql-injectat.py  consulta**

  Fer que la sentència sql a fer sigui un argument tot entre cometes 
  que es passa com a argument.
  sql injectat: perills d’injectar codi d’usuari en els programes.


# ----------------------------------------------

## Metodología Y APUNTES 






################################################################################


* PROGRAMA 14 INJECTAT.

* Contexto:

	* Consulta del tipo "select * from clientes where numcli [valor]"
	
	* Le podemos.
	
	* Mostrar cada uno de los -c clientes
	
	14.py -c 3344 -c 1520 -c 1996
	
	* Construye 1 SOLO PIPE.
	
	* Realiza un bucle y le añadirá el siguiente. Escribe y leerá.
	
	* 1 linea devuelve por cada SQL. 
	
	* Python devuelve 1 linea. **READ DEVUELVE 1 LINEA**






PROBLEMA ! SQL Injectat

* Problema del SQL.

* Exemple 13.


################################################################################


# /usr/bin/pyhton3
#-*-coding: utf-8-*-
#
# 13-sql-injectat.py
#
# usage: python3 13-sql-injectat.py "select * from oficinas"
# ------------------------------------------------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# ------------------------------------------------------------------------------

import sys,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Consulta a la base de dades entrada per argument al prigrama.""")
parser.add_argument("cons",type=str,\
        help="consulta a la base de dades training")
args=parser.parse_args()

# ------------------------------------------------------------------------------

command = [f"psql -qtA -F',' -h 172.17.0.2 -U postgres training -c \"{args.cons}\""]
pipeData = Popen(command, stdout=PIPE, shell=True)


for line in pipeData.stdout:
    print(line.decode("utf-8")[:-1])

exit(0)

################################################################################


################# VERIFICACIÓN Y SOLUCIÓN ################33



isx36579183@i11:~/Documents/ipc$ python3 13-sql-injectat.py "select * from oficinas";
22,Denver,Oeste,108,300000.00,186042.00
11,New York,Este,106,575000.00,692637.00
12,Chicago,Este,104,800000.00,735042.00
13,Atlanta,Este,105,350000.00,367911.00
21,Los Angeles,Oeste,108,725000.00,835915.00
isx36579183@i11:~/Documents/ipc$ 


--------------------

isx36579183@i11:~/Documents/ipc$ python3 13-sql-injectat.py "select * from repventas";
105,Bill Adams,37,13,Rep Ventas,1988-02-12,104,350000.00,367911.00
109,Mary Jones,31,11,Rep Ventas,1989-10-12,106,300000.00,392725.00
102,Sue Smith,48,21,Rep Ventas,1986-12-10,108,350000.00,474050.00
106,Sam Clark,52,11,VP Ventas,1988-06-14,,275000.00,299912.00
104,Bob Smith,33,12,Dir Ventas,1987-05-19,106,200000.00,142594.00
101,Dan Roberts,45,12,Rep Ventas,1986-10-20,104,300000.00,305673.00
110,Tom Snyder,41,,Rep Ventas,1990-01-13,101,,75985.00
108,Larry Fitch,62,21,Dir Ventas,1989-10-12,106,350000.00,361865.00
103,Paul Cruz,29,12,Rep Ventas,1987-03-01,104,275000.00,286775.00
107,Nancy Angelli,49,22,Rep Ventas,1988-11-14,108,300000.00,186042.00
isx36579183@i11:~/Documents/ipc$ 


-------------------------------

# ERROR DE SQL INJECTAT # ERROR DE SEGURIDAD


isx36579183@i11:~/Documents/ipc$ python3 13-sql-injectat.py "drop table repventas";
isx36579183@i11:~/Documents/ipc$ python3 13-sql-injectat.py "select * from repventas";
ERROR:  relation "repventas" does not exist
LINE 1: select * from repventas
                      ^
isx36579183@i11:~/Documents/ipc$ 


--------------------------------

INTENTAR ENTRAR CON USUARIO NORMAL

POSTGRESQL ES ROOT.

####################################### # python3 13-sql-injectat.py


Fer que la sentència sql a fer sigui un argument tot entre cometes
que es passa com a argument. sql injectat: perills d’injectar codi d’usuari en els programes.



1. 

2.

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.







"""

