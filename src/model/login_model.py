import hashlib
import json

import loguru

from src.core.constant import ACCOUNT_FILE
from src.core.enums import AccountPermissionEnum
from src.core.wms_dataclass import Account


class LoginModel:
    def __init__(self):
        self._account_dict = self._load_account()
        self._accounts: list[Account] = [
            Account.from_dict(account) for account in self._account_dict.values()
        ]

    def add_user(
        self,
        username: str,
        password: str,
        permission: AccountPermissionEnum = AccountPermissionEnum.Admin,
    ) -> None:
        account = Account(
            username, self._password_hash(password), permissions=permission
        )
        self._accounts.append(account)
        self._account_dict[account.username] = account.to_dict()
        self._save_account()

    def get_user(self, username: str) -> Account:
        return next(
            (account for account in self._accounts if account.username == username),
            None,
        )

    def _password_hash(self, password: str) -> str:
        """Hash the password"""
        return hashlib.md5(password.encode()).hexdigest()

    def check_password(self, username: str, password: str) -> bool:
        account = self.get_user(username)
        if account is None:
            return False
        return account.password == self._password_hash(password)

    def _save_account(self):
        with open(ACCOUNT_FILE, "w") as f:
            json.dump(self._account_dict, f)

    def _load_account(self) -> dict:
        try:
            with open(ACCOUNT_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            loguru.logger.error("账号文件格式错误")
            ACCOUNT_FILE.unlink(missing_ok=True)
            return {}
        except Exception as e:
            loguru.logger.error(f"读取账号文件出现错误: {e}")
            ACCOUNT_FILE.unlink(missing_ok=True)
            return {}


if __name__ == "__main__":
    login_model = LoginModel()
    login_model.add_user("admin", "123")
    print(login_model.get_user("超级管理员"))
    print(login_model.get_user("admin1"))
    print(login_model.get_user("admin"))
    print(login_model.get_user("admin1"))
