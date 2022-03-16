# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:13:30 2022

@author: EMORENO
"""

import pandas as pd  # pandas
import numpy as np
import datetime
from datetime import date
from datetime import datetime

base = pd.read_excel(r'C:\Users\emoreno\Downloads\S123_97dbfd66b8ab4bc1b54e876660777451_EXCEL.xlsx')
base_prueba=base['28. ¿Qué hace para evitar que los zancudos lo piquen?'].str.extractall(r'([^,]+)(?:\s*,\s*|$)')[0].unstack()

columnas=pd.Series(base_prueba.columns)
columnas[0]='Columna 1'
columnas[1]='Columna 2'
columnas[2]='Columna 3'

base_prueba.columns=columnas

base_prueba.reset_index(drop=True, inplace=True)
base_prueba=base_prueba.replace(np.nan,0)
base_prueba["Validación"]=""

base_prueba["Validación"]=np.where((((base_prueba['Columna 2']==0)) & (base_prueba['Columna 3']==0) ), base_prueba['Columna 1'], "Mas de un Metodo")
base_prueba["Validación"]=np.where(((base_prueba['Validación']=="otro9")) , "Eliminar", base_prueba["Validación"])
base_prueba.reset_index(level=0, inplace=True)
base.reset_index(level=0, inplace=True)
base=  pd.merge(base, base_prueba, on='index', how='left')
base = base[['ObjectID',
 'Municipio',
 'Barrio',
 'Número de Vivienda',
 'Ahora le preguntaremos sobre algunas experiencias previas con la enfermedad',
 '17. ¿Alguna vez un médico le ha dicho que tuvo dengue?',
 '18. ¿Cuándo fue?',
 '19. ¿Recuerda que tipo de dengue le dio?',
 '20. ¿Cuántas personas con las que vive han estado enfermas de dengue en los últimos 3 años?',
 'Acciones por iniciativa familiar',
 '28. ¿Qué hace para evitar que los zancudos lo piquen?',
 '¿Cuál?',
 'x',
 'y','Validación']]

base = base.loc[~(base['Validación']=="Eliminar")]

base.to_excel(r'C:\Users\emoreno\Downloads\Base Final Zancudos.xlsx',sheet_name = 'Base', index=False)