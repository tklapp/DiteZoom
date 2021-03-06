# DiteZoom
Automatiza la conexión a las clases de Zoom.

Antes que nada, saqué algunas ideas de /Kn0wn-Un/Auto-Zoom que tiene un código para abrir clases en una fecha pre-especificada, pero este código es fundamentalmente distinto porque: 
* 1. El suyo es para Windows y este para Mac OS.
* 2. Usa excel (no csv) y utiliza formato de .timetable para fechas y horarios; este código viene con un schedule y horarios semanales pre-especificados en el csv y está hecho para facilitar su uso. 
* 3. Su código se basa principalmente en screenshots y pyautogui, que funciona bastante mal en Macbooks que tienen Retina Display, por lo que yo evité al máximo realizar comandos con clicks de pyautogui y uso más el teclado. 

**Para poder correr el código necesitan**, por supuesto, Python, y tener instalado pip para poder instalar los módulos necesarios. Ambos se descargan fácil de internet. Una vez que los tienen, abren la terminal y corren "pip install [módulo]" con los siguientes módulos: time, schedule, subprocess, csv, os, pyautogui, keyboard. También tienen que tener actualizado el paquete cv2; para eso corren: "pip install opencv-python". 

Después van a "System Preferences" de su Mac OS, Security & Privacy, y en Accessibility le ponen un tick a Terminal si es que ya no lo tiene. 

Con todo lo necesario instalado, ahora pueden abrir el archivo TimeTable.csv y cargar sus horarios. Pueden cambiar los horarios de la forma que quieran: si su clase empieza 11:30 pueden cambiarlo, si quieren entrar un minuto antes pueden poner 11:39. El timetable predeterminado es el de Di Tella, pero cámbienlo a piacere. Si tienen clases más tarde también pueden agregar filas con el mismo formato (i.e. "monday" en inglés y sin mayúscula, mismo formato de horario). **Guarden el archivo como está, con formato csv.**

Abren terminal, corren "python3.8 DiteZoom.py" y ya tienen el script funcionando :) Si su Macbook **no** tiene retina display, corren "python3.8 DiteZoomNoRetina.py". 

Pueden cerrar el script y volverlo a abrir cuando quieran. No debería tener problemas para funcionar por eso. 
