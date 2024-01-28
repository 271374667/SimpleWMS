import io

import PIL.Image
import cairosvg
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PySide6.QtGui import QImage
from PySide6.QtGui import QPixmap
from barcode import EAN13

from src.common.database.utils import barcode_utils


def cv2AddChineseText(img, text, position, textColor=(0, 0, 0), textSize=23):
    """给图片添加中文文字"""
    if isinstance(img, np.ndarray):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # TODO: 该字体路径需要修改
    # 字体的格式
    # fontStyle = ImageFont.truetype(
    #     cfg.get('font', 'font_path'), textSize, encoding="utf-8")
    fontStyle = ImageFont.truetype(
            r'E:\load\python\Project\SimpleWMS\assets\fonts\Alibaba-PuHuiTi-Regular.ttf', textSize, encoding="utf-8")
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


def get_image(ean13: str, batch_info: str, item_name: str) -> np.ndarray:
    """生成条形码图片"""
    if len(ean13) != 13:
        raise ValueError("The length of the input must be 13.")
    # 需要先去掉校验位
    ean13 = ean13[:12]

    # 图片的生成和svg转png
    barcode = EAN13(ean13)
    barcode_png = cairosvg.svg2png(bytestring=barcode.render(writer_options={"module_width": 0.5}))
    barcode_png = PIL.Image.open(io.BytesIO(barcode_png))
    barcode_png = np.array(barcode_png)

    # 对图片进行处理以及添加文字
    barcode_png = cv2.cvtColor(barcode_png, cv2.COLOR_RGB2BGR)
    barcode_png = cv2.resize(barcode_png, (0, 0), fx=3, fy=3)
    barcode_png = barcode_utils.remove_picture_on_y(barcode_png, 195)
    barcode_png = barcode_utils.cv2AddChineseText(barcode_png, f'名称:{item_name}', (100, 205))
    barcode_png = barcode_utils.cv2AddChineseText(barcode_png, f'批次:{batch_info}', (100, 230))
    barcode_png = barcode_utils.cv2AddChineseText(barcode_png, f'EAN13:{barcode.get_fullcode()}', (400, 230))
    return barcode_png


def get_qpixmap_image(ean13: str, batch_info: str, item_name: str) -> QPixmap:
    np_image = get_image(ean13, batch_info, item_name)
    return QPixmap.fromImage(barcode_utils.cv2_to_qimage(np_image))
