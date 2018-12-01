# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_PATH = "C:/Users/bryan/Documents/Python y R/Datasets/2014_DataSet_PlayersStart_PlayOffs.csv"


columnas_lanzamiento = ['Rank','PLAYER','TEAM','POS',
                       'AGE','2PA',
                       '2P%','3PA',
                        '3P%']

data_frame_completo = pd.read_csv(
        CSV_PATH, 
        index_col= 'Rank',
        usecols = columnas_lanzamiento)
data_frame_mas_intentos_tresPuntos = data_frame_completo.sort_values(by=['3PA'], ascending=False)
data_frame_mas_intentos_dosPuntos = data_frame_completo.sort_values(by=['2PA'], ascending=False)
data_frame_mas_aciertos_tresPuntos = data_frame_completo.sort_values(by=['3P%'], ascending=False)
data_frame_mas_aciertos_dosPuntos = data_frame_completo.sort_values(by=['2P%'], ascending=False)

array_diez_lanzadores_tresPuntos = np.array((data_frame_mas_intentos_tresPuntos['PLAYER'],data_frame_mas_intentos_tresPuntos['3PA'],data_frame_mas_intentos_tresPuntos['3P%']))
array_diez_lanzadores_tresPuntos = np.stack(array_diez_lanzadores_tresPuntos,axis=1)
array_diez_lanzadores_tresPuntos = array_diez_lanzadores_tresPuntos[:10]
#print(array_diez_lanzadores_tresPuntos)

array_diez_lanzadores_dosPuntos = np.array((data_frame_mas_intentos_dosPuntos['PLAYER'],data_frame_mas_intentos_dosPuntos['2PA'],data_frame_mas_intentos_dosPuntos['2P%']))
array_diez_lanzadores_dosPuntos = np.stack(array_diez_lanzadores_dosPuntos,axis=1)
array_diez_lanzadores_dosPuntos = array_diez_lanzadores_dosPuntos[:10]
#print(array_diez_lanzadores_dosPuntos)

array_diez_encestadores_tresPuntos = np.array((data_frame_mas_aciertos_tresPuntos['PLAYER'],data_frame_mas_aciertos_tresPuntos['3PA'],data_frame_mas_aciertos_tresPuntos['3P%']))
array_diez_encestadores_tresPuntos = np.stack(array_diez_encestadores_tresPuntos,axis=1)
array_diez_encestadores_tresPuntos = array_diez_encestadores_tresPuntos[:10]
#print(array_diez_lanzadores_tresPuntos)

array_diez_encestadores_dosPuntos = np.array((data_frame_mas_aciertos_dosPuntos['PLAYER'],data_frame_mas_aciertos_dosPuntos['2PA'],data_frame_mas_aciertos_dosPuntos['2P%']))
array_diez_encestadores_dosPuntos = np.stack(array_diez_encestadores_dosPuntos,axis=1)
array_diez_encestadores_dosPuntos = array_diez_encestadores_dosPuntos[:10]

aux = []
aux2 = []
aux3 = []
for lanzadores_tresPuntos in array_diez_lanzadores_tresPuntos:
    aux.append(lanzadores_tresPuntos[...][0])
    aux2.append(lanzadores_tresPuntos[...][1])
    aux3.append(lanzadores_tresPuntos[...][2])
    
nombres = np.array(aux)
lanzamientos = np.array(aux2)
realizados = np.array(aux2)* np.array(aux3)
porcentaje_realizados = np.array(aux3)*100
n_groups = 10
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
fig, axs = plt.subplots(1, 1)
axs.bar(index, lanzamientos, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='Lanzamientos')

axs.bar(index + bar_width,realizados, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Aciertos')
axs.legend()
axs.set_xlim(0,9)
axs.set_xlabel('Jugador')
axs.set_ylabel('Estadísticas')
axs.grid(False)
axs.set_xticklabels(nombres, rotation=45)
axs.set_title('Estadísticas lanzadores de tres puntos')
plt.show()
aux = []
aux2 = []
aux3 = []
for lanzadores_dosPuntos in array_diez_lanzadores_dosPuntos:
    aux.append(lanzadores_dosPuntos[...][0])
    aux2.append(lanzadores_dosPuntos[...][1])
    aux3.append(lanzadores_dosPuntos[...][2])
nombres2 = np.array(aux)
lanzamientos2 = np.array(aux2)
realizados2 = np.array(aux2)* np.array(aux3)
porcentaje_realizados2 = np.array(aux3)*100
n_groups = 10
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.1'}
fig, axs = plt.subplots(1, 1)
axs.bar(index, lanzamientos2, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='Lanzamientos')

axs.bar(index + bar_width,realizados2, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Aciertos')
axs.legend()
axs.set_xlim(0,9)
axs.set_xlabel('Jugador')
axs.set_ylabel('Estadísticas')
axs.grid(False)
axs.set_xticklabels(nombres2, rotation=45)
axs.set_title('Estadísticas lanzadores de dos puntos')
plt.show()

realizados_tres = np.max(realizados*100)
realizados_dos = np.max(realizados2*100)
realizados = np.array([realizados_dos,realizados_tres])
labels = ['2P','3P']
#plt.pie(realizados, labels=nombres, autopct='%1.1f%%')
plt.pie(realizados, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title("Estadísticas de puntos realizados según lanzamiento", bbox={"facecolor":"0.8", "pad":5})
plt.legend()
plt.show()




aux = []
aux2 = []
aux3 = []
for encestadores_tresPuntos in array_diez_encestadores_tresPuntos:
    aux.append(encestadores_tresPuntos[...][0])
    aux2.append(encestadores_tresPuntos[...][1])
    aux3.append(encestadores_tresPuntos[...][2])
nombres = np.array(aux)
lanzamientos = np.array(aux2)
realizados = np.array(aux2)* np.array(aux3)
porcentaje_realizados = np.array(aux3)*100
n_groups = 10
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
fig, axs = plt.subplots(1, 1)
axs.bar(index, lanzamientos, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='Lanzamientos')

axs.bar(index + bar_width,realizados, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Aciertos')
axs.legend()
axs.set_xlim(0,9)
axs.set_xlabel('Jugador')
axs.set_ylabel('Estadísticas')
axs.grid(False)
axs.set_xticklabels(nombres, rotation=45)
axs.set_title('Estadísticas encestadores de tres puntos')
plt.show()
aux = []
aux2 = []
aux3 = []
for encestadores_dosPuntos in array_diez_encestadores_dosPuntos:
    aux.append(encestadores_dosPuntos[...][0])
    aux2.append(encestadores_dosPuntos[...][1])
    aux3.append(encestadores_dosPuntos[...][2])
nombres2 = np.array(aux)
lanzamientos2 = np.array(aux2)
realizados2 = np.array(aux2)* np.array(aux3)
porcentaje_realizados2 = np.array(aux3)*100
n_groups = 10
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
fig, axs = plt.subplots(1, 1)
axs.bar(index, lanzamientos2, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='Lanzamientos')

axs.bar(index + bar_width,realizados2, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Aciertos')
axs.legend()
axs.set_xlim(0,9)
axs.set_xlabel('Jugador')
axs.set_ylabel('Estadísticas')
axs.grid(False)
axs.set_xticklabels(nombres2, rotation=45)
axs.set_title('Estadísticas encestadores de dos puntos')
plt.show()

realizados_tres = np.max(realizados*100)
realizados_dos = np.max(realizados2*100)
realizados = np.array([realizados_dos,realizados_tres])
labels = ['2P','3P']
#plt.pie(realizados, labels=nombres, autopct='%1.1f%%')
plt.pie(realizados, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title("Estadísticas de puntos realizados según lanzamiento", bbox={"facecolor":"0.8", "pad":5})
plt.legend()
plt.show()

