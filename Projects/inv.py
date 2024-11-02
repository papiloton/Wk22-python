import os
import platform
import psutil


# if 'Windows' in platform.platform():
#     os.system("clear")
#     cpu_count = os.cpu_count()
#     mem_info = psutil.virtual_memory() .total
#     os_version = platform.platform()
#     python_version = platform.python_version()
#     print(f"""
#           number of cpu: {cpu_count} 
#           Total Memory: {mem_info/(1024**3): .2f} GB 
#           Os version: {os_version}
#           Python version: {python_version}""")
    
# else:
#     print("this is a linux system")

os.system("clear")
cpu_count = os.cpu_count()
mem_info = psutil.virtual_memory() .total
os_version = platform.platform()
python_version = platform.python_version()
print(f"""
     number of cpu: {cpu_count} 
     Total Memory: {mem_info/(1024**3): .2f} GB 
     Os version: {os_version}
     Python version: {python_version}""")
    
