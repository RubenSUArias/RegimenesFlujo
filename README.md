# Clasifica Regímenes de flujo de pruebas de presión y evalúa diversas propiedades
Hace años empecé este proyecto con el objetivo de titularme como ingeniero petrolero con el, sin embargo por falta de datos no se llegó a completar. 
En conjunto se entrena un modelo de clasificación a partir de datos de presión y sus derivadas para clasificar regímenes de flujo y elaborar un reporte de resultados. 

## Contenido
### regimenesdeflujo.py
Toma como entrada un archivo de entrenamiento con datos de presión y sus derivadas para realizar una regresión logística y empaquetar el modelo en un archivo usable .pkl


### Executable.py 
Toma como entrada datos de una prueba de presión datos41.2.dat y el modelo pkl para clasificar sus regímenes de flujo y evaluar permeabilidad, almacenamiento y daño a partir de datos solicitados al usuario y generando un reporte en formato pdf.

