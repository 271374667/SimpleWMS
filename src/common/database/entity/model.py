from datetime import datetime

import loguru
from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    )
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.common.database import engine
from src.constant import DATABASE_FILE


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    is_active: Mapped[int] = mapped_column(Integer, nullable=False, default=1)


class Batch(Base):
    __tablename__ = "batch"

    def __init__(self, **kw):
        super().__init__(**kw)

    # wave_serial_number 是批次号，每个批次号对应一个批次，批次号是唯一的
    # 比如2024年1月的第一批货物，批次号就是202401001
    # 后面的 001 是批次号的序号，每个批次号的序号都是从 001 开始递增的,最大为 999
    batch_serial_number: Mapped[str] = mapped_column(String(9), nullable=False)
    batch_name: Mapped[str] = mapped_column(String(16), nullable=False)
    created_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self) -> str:
        return f"<Batch(batch_serial_number={self.batch_serial_number}, batch_name={self.batch_name}, created_time={self.created_time})>"


class Wave(Base):
    __tablename__ = "wave"

    # wave_number 是波次号，每个波次号对应一个波次，波次号是唯一的
    # 比如2024年1月1日的第一波货物，波次号就是20240101001
    # 后面的 001 是波次号的序号，每个波次号的序号都是从 001 开始递增的,最大为 999
    wave_serial_number: Mapped[str] = mapped_column(String(9), nullable=False)
    wave_name: Mapped[str] = mapped_column(String(16), nullable=False)
    created_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self) -> str:
        return f"<Wave(wave_serial_number={self.wave_serial_number}, wave_name={self.wave_name}, created_time={self.created_time})>"


class Inventory(Base):
    __tablename__ = "inventory"

    item_name: Mapped[str] = mapped_column(String(16), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    brand: Mapped[str] = mapped_column(String(16), nullable=False)
    is_sold: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    return_times: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    batch_id: Mapped[int] = mapped_column(Integer, ForeignKey("batch.id"), nullable=False)
    wave_id: Mapped[int] = mapped_column(Integer, ForeignKey("wave.id"), nullable=True)

    # 使用 backref 参数可以在 Batch 类中通过 batch.inventory 访问到 Inventory 类
    batch: Mapped[Batch] = relationship("Batch", backref="inventory")
    wave: Mapped[Wave] = relationship("Wave", backref="inventory")

    def __repr__(self) -> str:
        return f"<Inventory(item_name={self.item_name}, price={self.price}, brand={self.brand}, return_times={self.return_times} batch={self.batch}, wave={self.wave})>"


if not DATABASE_FILE.exists():
    Base.metadata.create_all(engine)
    loguru.logger.success(f"数据库不存在,创建数据库: {DATABASE_FILE}")
