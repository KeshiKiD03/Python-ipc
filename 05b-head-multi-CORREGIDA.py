# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] [-f file]...
#  10 lines, file... 
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse
fileList=[]
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks")
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin",\
        metavar="numLines",default=10,\
        choices=[5,10,15])
parser.add_argument("-f", "--file",type=str,\
        help="fitxer a processar", metavar="file",\
        dest="fileList", nargs="*")
parser.add_argument("-v", "--verbose",action="store_true",default=False)
args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin

def headFile(fitxer):
  fileIn=open(fitxer,"r")
  counter=0
  for line in fileIn:
    counter+=1
    print(line, end='')
    if counter==MAXLIN: break
  fileIn.close()

if args.fileList:
  for fileName in args.fileList:
    if args.verbose: print("\n",fileName, 40*"-")
    headFile(fileName)

exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**01-head.py [file]**
  
  Mostrar les deu primeres línies de file o stdin

# ----------------------------------------------

## Explicación

Mostrar les 10 primeres línies d'un fitxer. 
El nom del fitxer a mostrar es rep com a argument, sinó es rep, 

es mostren les deu primeres línies de  l'entrada estàndard. 

Sinpsys: $ head [file] 


# ----------------------------------------------

## Metodología

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

