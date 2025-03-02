# Clasifica Regímenes de flujo de pruebas de presión y evalúa diversas propiedades
![image](https://github.com/user-attachments/assets/10424cb7-dc84-48e6-8a2c-9a0dbf6c8131)

Hace años empecé este proyecto con el objetivo de titularme como ingeniero petrolero con el, sin embargo por falta de datos no se llegó a completar. 
En conjunto se entrena un modelo de clasificación a partir de datos de presión y sus derivadas para clasificar regímenes de flujo y elaborar un reporte de resultados. 

## Contenido
### regimenesdeflujo.py
Toma como entrada un archivo de entrenamiento con datos de presión y sus derivadas para realizar una regresión logística y empaquetar el modelo en un archivo usable .pkl
![image](https://github.com/RubenSUArias/RegimenesFlujo/blob/main/Almacenamientodatos41.2.png)

![image](https://github.com/RubenSUArias/RegimenesFlujo/blob/main/MDHdatos41.2.png)

### Executable.py 
Toma como entrada datos de una prueba de presión datos41.2.dat y el modelo pkl para clasificar sus regímenes de flujo y evaluar permeabilidad, almacenamiento y daño a partir de datos solicitados al usuario y generando un reporte en formato pdf.

