#-*- coding: utf-8 -*-
import os
import os.path
import sys
import shutil

with open('/home/paulo/Downloads/caminhos.txt') as file:
    for line in file:
        print(str(line))
        caminho = os.path.dirname(str(line))
        arquivo = os.path.basename(str(line.rstrip()))
    os.link(str(caminho)+'/'+str(arquivo), '/home/paulo/movido.log')

        
       
#caminho = os.path.dirname('/home/paulo/Downloads/o.log')
#arquivo = os.path.basename('/home/paulo/Downloads/o.log')

#print(caminho)
#print(arquivo)
