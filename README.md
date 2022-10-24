psutil library for local system monitoring
===============

Esta aplicación hace uso de la librería *psutil* de Python con el objetivo de monitorear la utilización de recursos del sistema local (CPU, almacenamiento, batería).

# Documentación
El uso de las diferentes funciones del módulo psutil se puede consultar [aquí](https://pypi.org/project/psutil/).

Para este proyecto se utilizaron únicamente 3 funciones: 
- disk_usage: obtención de uso del disco duro en relación a espacio utilizado/disponible
- cpu_times: obtención de unidades de tiempo de ejecución de procesos por el CPU
- sensors_battery: lectura del sensor de voltaje de la bateria integrada


# Dependencias
Al comienzo del código fuente, se debe importar la librería psutil, para ello, dentro de la carpeta del proyecto, se debe correr de antemano el siguiente comando:
> pip3 install psutil

Una vez instalado este módulo, el programa debe correr exitosamente.



