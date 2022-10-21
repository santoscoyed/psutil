import math
import psutil

def df_check():
    disk_stats = psutil.disk_usage('/')
    total_GB = math.floor(disk_stats.total/(2**30))
    size_avail = (psutil.disk_usage('/').free)/(2**30)
    GB_avail = math.floor(size_avail)
    percent_avail = (GB_avail*100)/total_GB
    rounded_percent = round(percent_avail, 2)
    print("Total disk capacity of root (/) file system is:", total_GB, "GB")
    print("Available space:", rounded_percent, "%")

def cpu_stats():
    cpu_user_minutes = round(((psutil.cpu_times().user)/60), 2)
    cpu_nice_minutes = psutil.cpu_times().nice
    cpu_system_minutes = round(((psutil.cpu_times().system)/60), 2)
    cpu_idle_hours = round(((psutil.cpu_times().idle)/1200), 2)
    print("Amount of time spent by CPU running processes in current user:", cpu_user_minutes, "minutes")
    print("Amount of time spent by CPU running high priority processes in current user:", cpu_nice_minutes, "minutes")
    print("Amount of time spent by CPU running processes in kernel:", cpu_system_minutes, "minutes")
    print("Free CPU time, no activity:", cpu_idle_hours, "hours")

def battery_health():
    battery = psutil.sensors_battery()
    pcent = battery.percent
    print("Battery:", pcent, "%")

    cargador = psutil.sensors_battery().power_plugged
    if not cargador:
        print("Please plug in power adapter")


df_check()
cpu_stats()
battery_health()



