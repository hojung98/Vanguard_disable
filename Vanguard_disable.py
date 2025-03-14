import winreg

def disable_startup_program(program_name):
    try:
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, program_name, 0, winreg.REG_BINARY, b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        print(f"{program_name} 뱅가드를 사용 안 함 설정으로 바꾸는데 성공했어요!! 컴퓨터를 껐다 키시면 적용된답니당 게임이 실행될때는 실행되니 걱정마셔요!")
    except FileNotFoundError:
        print("뱅가드 레지스토리를 찾을 수 없어요 ㅠㅠㅠㅠㅠ")
    except Exception as e:
        print(f"오류가 발생했어요 혹시 관리자 권한으로 실행하셨나요? 관리자 권한으로 실행해야 되어요 ㅠㅠ 아니라면 보이는 오류코드와 같이 저에게 문의주시겠어요?: {e}")
    input("\n엔터를 누르면 종료되어요")  # 결과 확인 후 종료

# 실행
disable_startup_program("Riot Vanguard")
