import winreg

def disable_startup_program(program_name):
    try:
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, program_name, 0, winreg.REG_BINARY, b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        print(f"{program_name} 시작 프로그램 '사용 안 함' 설정 완료!")
    except FileNotFoundError:
        print("레지스트리를 찾을 수 없음.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
disable_startup_program("Riot Vanguard")
