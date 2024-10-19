import os
from pyrogram import Client

api_id = xxx  # Thay bằng api_id của bạn
api_hash = 'xxx'  # Thay bằng api_hash của bạn

sessions_dir = "sessions"

if not os.path.exists(sessions_dir):
    os.makedirs(sessions_dir)

while True:
    session_name = input("Nhập tên file .session: ")
    print("--------------------\n")

    session_name = session_name.split('.')[0]
    session_path = os.path.join(sessions_dir, session_name)

    app = Client(session_path, api_id, api_hash)

    with app:
        print("\n--------------------")
        me = app.get_me()
        print(f"\033[92mĐã tạo file {session_name}.session cho tài khoản @{me.username if me.username else 'không có username'}\033[0m")

    create_another = input("Tạo thêm file .session (y/n): ").strip().lower()
    if create_another != 'y':
        break
