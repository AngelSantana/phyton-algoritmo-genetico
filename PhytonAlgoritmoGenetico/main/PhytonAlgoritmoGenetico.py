# -*- coding: cp1252 -*- 
from Genetico import Genetico
from Cromossomo import Cromossomo
from Gene import Gene
import time
import os

funcGenetico = Genetico()
totalGene = 7
#Ver questões dos acentos
print(" SUGEST�O DE COMPET�NCIAS \n PARA O CARGO DE [Coordenador de Recursos Humanos]")

totalIndividuos = input("\n 1. Insira a quantidade de candidatos para serem gerados aleat�riamente: ")
valorEsperado =   input("\n 2. Insira o valor m�nimo para a sele��o de candidatos: ")
quantidadeIndividuos = input("\n 3. Insira a quantidade m�xima de candidatos que se deseja obter: ")

os.system("cls")

print("\n ===================== CONFIGURA��ES DO PROGRAMA ===================== ")
print("\n Total de candidatos: {0} ".format(totalIndividuos))
print("\n Valor m�nimo para a sele��o de candidatos: {0} ".format(valorEsperado))
print("\n Quantidade m�nima de candidatos que se deseja obter : {0}".format(quantidadeIndividuos))
print("\n [Padr�o/Programa] Total de crit�rios de avalia��o : {0} ".format(totalGene));
print("\n ===================================================================== ")

print (" \n\n Gerando candidatos ... \n\n")
time.sleep(5)
candidatos = Genetico().gerarPopulacao(int(totalIndividuos), int(totalGene))
Genetico().listarCandidatos(candidatos.listaCandidatos)

print (" \n\n Avaliando candidatos ... \n\n")
time.sleep(5)
Genetico().avaliar(candidatos.listaCandidatos)

#Descomentar e continuar fazendo ... Sen�o fica em loop infinito.
#while (Genetico().aplicarCondicao(candidatos.listaCandidatos, int(valorEsperado), int(quantidadeIndividuos))):
#       Genetico().selecionar(candidatos.listaCandidatos, int(totalIndividuos), int(totalGene), int(quantidadeIndividuos)) 
