import os
import platform

import psutil


def format_usage(label: str, usage: float, width: int = 30) -> str:
    filled = round(width * usage / 100)
    bar = "#" * filled + "-" * (width - filled)
    return f"{label:<12} [{bar}] {usage:5.1f}%"


def main() -> None:
    disk_path = os.path.abspath(os.sep)
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage(disk_path).percent

    print(f"Uso de recursos del sistema ({platform.system()} {platform.release()})")
    print("-" * 52)
    print(format_usage("CPU", cpu_usage))
    print(format_usage("Memoria", memory_usage))
    print(format_usage(f"Disco ({disk_path})", disk_usage))


if __name__ == "__main__":
    main()
