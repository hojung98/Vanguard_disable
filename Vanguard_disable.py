import winreg

def disable_startup_program(program_name):
    try:
        # ✅ "StartupApproved\Run"에서 비활성화 값 설정 (네가 올린 값 반영)
        key_path_approved = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        disabled_value = bytes([0x03, 0x00, 0x00, 0x00, 0x2d, 0x10, 0x37, 0x34, 0x86, 0x94, 0xdb, 0x01])  # 올린 값 그대로 적용

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_approved, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, program_name, 0, winreg.REG_BINARY, disabled_value)

        print(f"✅ {program_name}을(를) 작업 관리자에서 '사용 안 함' 상태로 변경 완료! 재부팅하면 적용됨 🎉")

    except FileNotFoundError:
        print("❌ 레지스트리를 찾을 수 없어요! 대상 프로그램이 존재하는지 확인해 주세요.")
    except PermissionError:
        print("⚠️ 관리자 권한이 필요합니다! 'cmd'를 관리자 권한으로 실행한 후 다시 시도해 주세요.")
    except Exception as e:
        print(f"오류 발생! 관리자 권한으로 실행하셨나요? 오류 코드: {e}")

    input("\n엔터를 누르면 종료됩니다.")  # 결과 확인 후 종료

# 실행
disable_startup_program("Riot Vanguard")



