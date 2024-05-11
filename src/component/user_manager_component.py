import loguru
from PySide6.QtWidgets import QTableWidgetItem

from src.core.enums import AccountPermissionEnum
from src.model.login_model import LoginModel
from src.view.component_view.user_manager_view import UserManagerView


class UserManagerComponent:
    def __init__(self):
        self._view = UserManagerView()
        self._login_model = LoginModel()

        self._view.get_add_user_button().clicked.connect(self.add_user)
        self._view.get_delete_user_button().clicked.connect(self.delete_user)

        # 将数据添加到表格中
        self._add_data_to_table()

    def get_view(self) -> UserManagerView:
        return self._view

    def get_model(self) -> LoginModel:
        return self._login_model

    def show(self) -> None:
        self._view.show()

    def hide(self) -> None:
        self._view.hide()

    def add_user(self) -> None:
        username = self._view.get_username_lineEdit().text()
        password = self._view.get_password_lineEdit().text()
        permission = self._view.get_permission_comboBox().currentIndex()

        if username == "" or password == "":
            self._view.show_error_infobar("错误", "用户名和密码不能为空!")
            return

        if self._login_model.get_user(username) is not None:
            self._view.show_error_infobar("错误", "用户名已存在!")
            return

        self._login_model.add_user(
            username, password, AccountPermissionEnum(permission)
        )
        loguru.logger.info(
            f"添加用户: {username}, 权限为: {AccountPermissionEnum(permission)}"
        )
        self._update_table()
        self.get_view().show_success_infobar("添加成功!", f"成功添加了{username}用户!")

    def delete_user(self) -> None:
        table = self._view.get_table()
        selected_row = table.selectedItems()
        if not selected_row:
            self._view.show_error_infobar("错误", "请选择一个用户!")
            return

        # 如果当前用户是最后一个用户，不能删除
        if len(self._login_model.get_all_users()) == 1:
            self._view.show_error_infobar("错误", "当前用户是最后一个用户，不能删除!")
            return

        if (
            self.get_view().show_mask_dialog(
                "确定删除用户吗?", "请你仔细确认是否删除该用户"
            )
            == 0
        ):
            return

        username = selected_row[0].text()
        self._login_model.delete_user(username)
        loguru.logger.info(f"删除用户: {username}")
        self._update_table()
        self.get_view().show_success_infobar("删除成功!", f"成功删除了{username}用户!")

    def _add_data_to_table(self) -> None:
        table = self._view.get_table()
        table.setRowCount(0)
        for user in self._login_model.get_all_users():
            row_position = table.rowCount()
            table.insertRow(row_position)
            table.setItem(row_position, 0, QTableWidgetItem(user.username))
            table.setItem(
                row_position,
                1,
                QTableWidgetItem(str(AccountPermissionEnum(user.permissions).name)),
            )

        # 为表格增加一些空的行
        for _ in range(5):
            table.insertRow(table.rowCount())

    def _update_table(self) -> None:
        self._view.get_table().clear()
        self._add_data_to_table()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    component = UserManagerComponent()
    component.show()
    app.exec()
