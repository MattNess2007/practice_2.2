import psutil
import os

def get_size_gb(bytes):
    return bytes // (1024**3)


# CPU
cpu = psutil.cpu_percent(interval=1)
print(f"\nЦП: {cpu}%")

# RAM
memory = psutil.virtual_memory()
print(f"Использовано: {get_size_gb(memory.used)} ГБ / {get_size_gb(memory.total)} ГБ")

# Диск
disk_path = 'C:'
disk = psutil.disk_usage(disk_path)
print(f"Занято: {get_size_gb(disk.used)} ГБ / {get_size_gb(disk.total)} ГБ")
