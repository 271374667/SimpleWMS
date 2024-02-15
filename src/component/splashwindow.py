from contextlib import suppress


class SplashWindow:
    """
    SplashWindow

    使用pyinstaller打包时，可以在程序启动时显示一个启动图片，当程序启动完成后关闭启动图片
    """
    @staticmethod
    def update_text(text: str):
        with suppress(ModuleNotFoundError):
            import pyi_splash
            pyi_splash.update_text(text)

    @staticmethod
    def close_splash():
        with suppress(ModuleNotFoundError):
            import pyi_splash
            pyi_splash.close()
