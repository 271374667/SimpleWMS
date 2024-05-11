import loguru
from PySide6.QtWidgets import QApplication

from src.component.pyinstaller_splashwindow import SplashWindow
from src.core.constant import ACCOUNT_FILE
from src.core.enums import AccountPermissionEnum
from src.presenter.login_presenter import LoginPresenter
from src.presenter.main_presenter import MainPresenter
from src.view.splash_view import SplashView


@loguru.logger.catch(reraise=True)
def main():
    def start(permission: AccountPermissionEnum):
        splash_view = SplashView()
        splash_view.show()
        splash_view.show_message("正在加载程序...")

        main_presenter = MainPresenter(permission)
        main_window = main_presenter.get_view()
        main_window.show()

        splash_view.finish(main_window)
        splash_view.deleteLater()

        # 将主窗口放到最前面
        main_window.raise_()
        loguru.logger.success("SimpleWMS 启动!")
        loguru.logger.success("SimpleWMS 已退出!")

    # 这里是使用了一个双重启动的方式，第一次启动是pyinstaller启动的，第二次启动是我们自己启动的
    # 因为解压也需要时间
    # 关闭 pyinstaller 自带的启动图片
    SplashWindow.close_splash()

    app = QApplication([])
    if not ACCOUNT_FILE.exists():
        loguru.logger.warning("没有账户文件,将直接进入管理员模式!")
        start(AccountPermissionEnum.Admin.value)
    else:
        login_presenter = LoginPresenter()
        login_presenter.user_permission_signal.connect(start)
        login_view = login_presenter.get_view()
        login_view.show()
    app.exec()


if __name__ == "__main__":
    main()
