import winreg

def disable_startup_program(program_name):
    try:
        # 사용자별(Explorer\StartupApproved\Run) 비활성화
        key_path_user = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_user, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, program_name, 0, winreg.REG_BINARY, b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        
        # 모든 사용자 대상(Windows\CurrentVersion\Run) 비활성화
        key_path_all_users = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_all_users, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, program_name)  # 등록된 실행 값을 삭제
                print(f"{program_name}의 모든 사용자 자동 실행을 사용 안 함으로 설정했어요!!")
        except FileNotFoundError:
            print(f"{program_name}이 모든 사용자 대상 자동 실행 목록에 존재하지 않아요.")

        print(f"{program_name}을(를) 비활성화했어요! 컴퓨터를 껐다 켜시면 적용될 거예요. 게임 실행 시에는 자동으로 다시 실행될 수도 있어요!")
    except FileNotFoundError:
        print("뱅가드 레지스트리를 찾을 수 없어요 ㅠㅠㅠㅠㅠ")
    except Exception as e:
        print(f"오류가 발생했어요! 혹시 관리자 권한으로 실행하셨나요? 관리자 권한으로 실행해야 돼요 ㅠㅠ 아니면 보이는 오류 코드와 함께 저에게 문의해 주세요!: {e}")

    input("\n엔터를 누르면 종료됩니다.")  # 결과 확인 후 종료

# 실행
disable_startup_program("Riot Vanguard")
