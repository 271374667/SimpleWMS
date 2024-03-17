from pathlib import Path

import loguru
import yagmail

from src.config import cfg


class SendEmail:
    def __init__(self) -> None:
        loguru.logger.info("正在准备链接到服务器")
        self.email_title = "当前没有设置标题"

        self.email = yagmail.SMTP(
            user={cfg.get(cfg.email_account): "secret"},
            password=cfg.get(cfg.email_secret_key),
            host="smtp.qq.com",
            port=465,
        )
        self._content: list[str] = []
        self._pic_content: list[yagmail.inline] = []

    def set_content(self, content: list[str]) -> None:
        self._content = content

    def set_email_title(self, email_title: str) -> None:
        self.email_title = email_title

    def add_content(self, content: str) -> None:
        self._content.append(content)

    def add_pic(self, pic_path: Path) -> None:
        self._pic_content.append(yagmail.inline(pic_path))

    def send(self) -> None:
        self.email.send(
            to=[cfg.get(cfg.email_account)],
            subject=self.email_title,
            contents=[*self._content, *self._pic_content],
        )
        loguru.logger.success("邮件发送成功")


if __name__ == "__main__":
    email = SendEmail()
    email.set_content(["测试邮件"])
    email.add_pic(
        Path(r"E:\load\python\Project\Left4DeadLogAnalysis\data\most_popular_map.png")
    )
    email.send()
