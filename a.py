import logging
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

class AuthSystem:
    def __init__(self):
        self.logger = self.setup_logging()
        self.users = {
            "user1": User("user1", "correct_password"),
            "user2": User("user2", "password123")
        }

    def setup_logging(self):
        logger = logging.getLogger('AuthSystem')
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('user_activity.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def login(self, username, password):
        self.logger.debug(f'ログイン試行: ユーザー {username}')

        if username not in self.users:
            self.logger.warning(f'存在しないユーザー {username} のログイン試行')
            return False

        user = self.users[username]
        if user.password == password:
            user.is_logged_in = True
            self.logger.info(f'ユーザー {username} がログインに成功')
            return True
        else:
            self.logger.warning(f'ユーザー {username} のパスワードが不正')
            return False

    def view_profile(self, username):
        if username in self.users and self.users[username].is_logged_in:
            self.logger.info(f'ユーザー {username} がプロフィールを表示')
            return True
        else:
            self.logger.warning(f'未認証のユーザー {username} がプロフィール表示を試行')
            return False

    def change_settings(self, username, setting_name, new_value):
        if username in self.users and self.users[username].is_logged_in:
            self.logger.critical(f'ユーザー {username} が設定 {setting_name} を変更: {new_value}')
            return True
        else:
            self.logger.error(f'未認証のユーザー {username} が設定変更を試行')
            return False