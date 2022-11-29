psutil library for local system monitoring
===============

This application makes use of the *psutil* Python library intended to monitor utilization of local system resources (CPU, storage, battery status).

# Documentation
All methods pertaining to the psutil module can be found [here](https://pypi.org/project/psutil/).

This project utilizes three psutil methods for showcasing local PC stats at the time the code is run: 
- disk_usage: returns free space on hard drive disk in relation to occupied space.
- cpu_times: returns time units of thread processing by CPU
- sensors_battery: returns voltaje sensor reading of built-in battery.


# Dependencias
At the beginning of source code, psutil library must be imported, for this purpose, the following command must be run from the CLI **inside** the project's directory: 
> pip3 install psutil

Once installed, the code should run successfully.



