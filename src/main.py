"""
Implement User Management System
"""

import json, re
from datetime import datetime

def is_valid_password(password):
    # 정규식 사용하여 10자 이상, 특수문자 포함 확인
    pattern = r'^(?=.*[!@#$%^&*(),.?":{}|<>]).{10,}$'
    
    return re.match(pattern, password) is not None

def is_valid_birthdate(birthdate_str):
    try:
        # 입력값을 날짜로 변환
        birthdate = datetime.strptime(birthdate_str, "%Y%m%d").date()
        today = datetime.today().date()
        # 오늘보다 이후 날짜인지 확인
        return birthdate <= today
    except ValueError:
        # 날짜 형식이 잘못된 경우
        return False

users = { #초기 사용자 목록
    "adm123" : { #id
        "name": "Big boss", "birth":"19700115",
        "pw": "123123", "role": "admin"
    },
    "editor112" : {
        "name": "Tom", "birth":"19970714",
        "pw": "1q2w3e4r", "role": "editor"
    },
    "normaly" : {
        "name": "John", "birth":"20021216",
        "pw": "asdf1234", "role": "viewer"
    }
}

print("-"*10+"전체 사용자 목록"+"-"*10)
print(json.dumps(users, indent=1))

run = True
user_login = 0
while run:
    #로그인 기능 구현
    if user_login==0:
        id_chk = input("Type your ID (If you want to quit, enter q) : ")
        if id_chk in users:
            ps_chk = input("Type your password : ")
            if ps_chk==users[id_chk]["pw"]:
                print(f"Welcome, {users[id_chk]["name"]}!")
                user_login=1
            else:
                print("Wrong password. try again.")
                continue
        elif id_chk=='q': #종료
            print("program off.")
            break
        else:
            print("There is no ID.")
            continue

    work = input("Create new ID-1 / Update ID-2 / Delete ID-3 / Quit-other keys : ")
    match work:
        case "1":
            while True:
                new_id = input("Enter new ID : ")
                if new_id in users:
                    print("이미 있는 아이디입니다.")
                    continue
                else:
                    new_name = input("Enter name : ")
                    new_birth = input("Enter birth : ")
                    if len(new_birth)>8 or not is_valid_birthdate(new_birth):
                        print("유효한 생년월일이 아닙니다.")
                        continue
                    new_role = input("Enter role : ")
                    new_password = input("Enter password(특수문자가 포함된 10자 이상) : ")
                    if is_valid_password(new_password):
                        users[new_id]={"name":new_name, "birth": new_birth, "pw": new_password, "role": new_role}
                        print("새 계정이 생성되었습니다.")
                        print("-"*10+"생성 후 사용자 목록"+"-"*10)
                        print(json.dumps(users, indent=1))
                        break
                    else:
                        print("비밀번호가 조건에 맞지 않습니다.")
                        continue
        case "2":
            while True:
                upt_id = input("수정하고 싶은 ID를 입력하세요 : ")
                if not upt_id in users:
                    print("없는 아이디입니다.")
                    continue
                if upt_id!=id_chk and users[id_chk]["role"]=="viewer":
                    print("수정 권한이 없습니다.")
                    continue
                upt_name = input("Enter name : ")
                upt_birth = input("Enter birth : ")
                if len(upt_birth)>8 or not is_valid_birthdate(upt_birth):
                    print("유효한 생년월일이 아닙니다.")
                    continue
                upt_role = input("Enter role : ")
                upt_password = input("Enter password(특수문자가 포함된 10자 이상) : ")
                if is_valid_password(upt_password):
                    users[upt_id]={"name":upt_name, "birth": upt_birth, "pw": upt_password, "role": upt_role}
                    print("새 계정이 생성되었습니다.")
                    print("-"*10+"수정 후 사용자 목록"+"-"*10)
                    print(json.dumps(users, indent=1))
                    break
                else:
                    print("비밀번호가 조건에 맞지 않습니다.")
                    continue
        case "3":
            while True:
                del_id = input("삭제하고 싶은 ID를 입력하세요 : ")
                if not del_id in users:
                    print("존재하지 않는 ID입니다.")
                    continue
                if del_id!=id_chk and users[id_chk]["role"]!="admin":
                    print("삭제 권한이 없습니다.")
                    continue
                users.pop(del_id)
                print("-"*10+"삭제 후 사용자 목록"+"-"*10)
                print(json.dumps(users, indent=1))
                if del_id==id_chk:
                    user_login = 0
                break
        case _:
            print("system off.")
            break