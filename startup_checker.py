import os
import winreg
import subprocess

def get_startup_programs():
    programs = []

    # 1️⃣ Startup 폴더에서 가져오기
    startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    if os.path.exists(startup_folder):
        for file in os.listdir(startup_folder):
            if file.endswith(".lnk"):
                programs.append(("Startup 폴더", file.replace(".lnk", "")))

    # 2️⃣ 레지스트리에서 가져오기 (현재 사용자 & 전체 시스템)
    reg_paths = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run")
    ]
    
    for hive, path in reg_paths:
        try:
            with winreg.OpenKey(hive, path) as key:
                i = 0
                while True:
                    try:
                        name, _, _ = winreg.EnumValue(key, i)
                        programs.append((path, name))
                        i += 1
                    except OSError:
                        break
        except FileNotFoundError:
            pass

    # 3️⃣ 작업 스케줄러에서 가져오기
    result = subprocess.run(["schtasks", "/Query", "/FO", "LIST"], capture_output=True, text=True, shell=True)
    for line in result.stdout.split("\n"):
        if line.startswith("TaskName:"):
            task_name = line.split(":", 1)[1].strip()
            programs.append(("작업 스케줄러", task_name))

    return programs

# 프로그램 목록 출력
startup_programs = get_startup_programs()
for location, name in startup_programs:
    print(f"[{location}] {name}")
