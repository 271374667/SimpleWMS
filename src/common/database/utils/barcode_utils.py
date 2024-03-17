import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from PySide6.QtGui import QImage


def cv2AddChineseText(img, text, position, textColor=(0, 0, 0), textSize=23):
    """给图片添加中文文字"""
    if isinstance(img, np.ndarray):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    # fontStyle = ImageFont.truetype(
    #     cfg.get('font', 'font_path'), textSize, encoding="utf-8")
    fontStyle = ImageFont.truetype(
        r"E:\load\python\Project\SimpleWMS\assets\fonts\Alibaba-PuHuiTi-Regular.ttf",
        textSize,
        encoding="utf-8",
    )
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def remove_picture_on_y(img: np.ndarray, y: int) -> np.ndarray:
    """将图片y轴大于y的部分设置为255（白色）"""
    if y < img.shape[0]:  # 检查y是否在图片的范围内
        img[y:, :, :] = 255  # 将y轴大于y的部分设置为255（白色）
    return img


def cv2_to_qimage(cv_img):
    """将cv2图片转换为QImage"""
    height, width, channel = cv_img.shape
    bytesPerLine = 3 * width
    return QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
