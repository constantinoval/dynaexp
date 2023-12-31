import os.path
from typing import List, Any
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import LargeBinary
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import enum
from sqlalchemy.types import Enum, PickleType
from math import pi
from datetime import datetime
from PIL import Image as Pilimage
import io


class Base(DeclarativeBase):
    creation_datetime: Mapped[Optional[datetime]]
    notes: Mapped[Optional[str]]

    def set_creation_time(self):
        self.creation_datetime = datetime.now()

    @classmethod
    def data_record_columns(cls) -> int:
        return len(cls.data_record_header())


class ElasticProperties(Base):
    """
    Таблицы с упругими моделями для компонент установки (стержней, ударников, обойм):
    модуль Юнга, плотность, скорость звука
    """
    __tablename__ = "elasticproperties"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    E: Mapped[float]
    c: Mapped[float]

    # rho: Mapped[float]

    @property
    def rho(self) -> float:
        if self.c:
            return self.E / self.c ** 2 * 1e6
        else:
            return 0

    def __repr__(self) -> str:
        return f"#{self.id}-{self.name}: E={self.E:g}, c={self.c:g}"

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "название", "Е, МПа", "c, м/c", "плотность, кг/м^3", "имя", "дата создания", "комментарий"]

    # @staticmethod
    # def data_record_columns() -> int:
    #     return len(ElasticProperties.data_record_header())

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id), self.name]
        result += [f"{r:g}" for r in [self.E, self.c, self.rho]]
        result += [repr(self), "", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result


class Striker(Base):
    """
    Таблицы с ударниками: сечение, длина, упругий материал
    """
    __tablename__ = "strikers"
    id: Mapped[int] = mapped_column(primary_key=True)
    D: Mapped[float]
    D0: Mapped[Optional[float]] = mapped_column(default=0.0)
    L: Mapped[float]
    material_id: Mapped[int] = mapped_column(ForeignKey('elasticproperties.id'))
    material: Mapped[ElasticProperties] = relationship()

    def __repr__(self):
        size = f"{self.D:.0f}x"
        if self.D0:
            size += f"{self.D0:.0f}x"
        size += f"{self.L:.0f}"
        return (f"#{self.id}-{self.material.name}-{self.geom_type}-{size}")

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "D, мм", "D0, мм", "L, мм", "материал", "тип", "имя", "дата создания", "комментарий"]

    # @staticmethod
    # def data_record_columns() -> int:
    #     return len(Striker.data_record_header())

    @property
    def geom_type(self) -> str:
        return "сплошной" if self.D0 == 0.0 else "трубка"

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result += [f"{r:g}" for r in [self.D, self.D0, self.L]]
        result.append(repr(self.material))
        result.append(self.geom_type)
        result.append(repr(self))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result


#
#
class MeasureBar(Base):
    """
    Таблицы с мерными стержнями: сечение, упругий материал, длина, словарь с данными для
    коррекции дисперсии
    """
    __tablename__ = "measurebars"
    id: Mapped[int] = mapped_column(primary_key=True)
    D: Mapped[float]
    D0: Mapped[Optional[float]] = mapped_column(default=0.0)
    L: Mapped[float]
    material_id: Mapped[int] = mapped_column(ForeignKey('elasticproperties.id'))
    material: Mapped[ElasticProperties] = relationship()

    def __repr__(self):
        size = f"{self.D:.0f}x"
        if self.D0:
            size += f"{self.D0:.0f}x"
        size += f"{self.L:.0f}"
        return (f"#{self.id}-{self.material.name}-{self.geom_type}-{size}")

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "D, мм", "D0, мм", "L, мм", "материал", "тип", "имя", "дата создания", "комментарий"]

    # @staticmethod
    # def data_record_columns() -> int:
    #     return len(MeasureBar.data_record_header())

    @property
    def geom_type(self) -> str:
        return "сплошной" if self.D0 == 0.0 else "трубка"

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result += [f"{r:g}" for r in [self.D, self.D0, self.L]]
        result.append(repr(self.material))
        result.append(self.geom_type)
        result.append(repr(self))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result


class Jacket(Base):
    """
    Таблица с параметрами обоймы: длина, наружный и внешний диаметр, ссылка на упругий материал.
    """
    __tablename__ = "jackets"
    id: Mapped[int] = mapped_column(primary_key=True)
    D: Mapped[float]
    D0: Mapped[float]
    L: Mapped[float]
    material_id: Mapped[int] = mapped_column(ForeignKey('elasticproperties.id'))
    material: Mapped[ElasticProperties] = relationship()

    def __repr__(self):
        size = f"{self.D:.0f}x{self.D0:.0f}x{self.L:.0f}"
        return (f"#{self.id}-{self.material.name}-{size}")

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "D, мм", "D0, мм", "L, мм", "материал", "имя", "дата создания", "комментарий"]

    # @staticmethod
    # def data_record_columns() -> int:
    #     return len(Jacket.data_record_header())

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result += [f"{r:g}" for r in [self.D, self.D0, self.L]]
        result.append(repr(self.material))
        result.append(repr(self))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result


class Customer(Base):
    """
    Таблица с заказчиками.
    """
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "имя", "название", "дата создания", "комментарий"]

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result.append(self.name)
        result.append(repr(self))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result

    def __repr__(self):
        return (f"#{self.id}-{self.name}")


class Executor(Base):
    """
    Таблица с заказчиками.
    """
    __tablename__ = "executors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "имя", "название", "дата создания", "комментарий"]

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result.append(self.name)
        result.append(repr(self))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result

    def __repr__(self):
        return (f"#{self.id}-{self.name}")


class ExperimentsGroup(Base):
    """
    Таблица с группами экспериментов.
    """
    __tablename__ = "experimentsgroups"
    id: Mapped[int] = mapped_column(primary_key=True)
    short_name: Mapped[str]
    contract: Mapped[str]
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped[Customer] = relationship()
    executor_id: Mapped[int] = mapped_column(ForeignKey('executors.id'))
    executor: Mapped[Executor] = relationship()

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "краткое название", "договор", "заказчик", "исполнитель", "дата создания", "комментарий"]

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        result.append(self.short_name)
        result.append(self.contract)
        result.append(repr(self.customer))
        result.append(repr(self.executor))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result

    def __repr__(self) -> str:
        return f"#{self.id}-{self.short_name}"


class OscChannel(Base):
    """
    Измерительный канал. Может быть сигналом со стержня, обоймы или образца.
    """
    __tablename__ = "oscchannels"
    id: Mapped[int] = mapped_column(primary_key=True)
    tarir: Mapped[float]
    gauge_position: Mapped[Optional[float]]
    bar_id: Mapped[Optional[int]] = mapped_column(ForeignKey('measurebars.id'))
    bar: Mapped[Optional[MeasureBar]] = relationship()
    jacket_id: Mapped[Optional[int]] = mapped_column(ForeignKey('jackets.id'))
    jacket: Mapped[Optional[Jacket]] = relationship()

    @staticmethod
    def data_record_header() -> list[str]:
        return ["id", "имя", "тарировочный коэффициент", "положение датчика",
                "дата создания", "комментарий"]

    @property
    def channel_type(self) -> str:
        if self.bar:
            return "Датчик на стержне"
        if self.jacket:
            return "Датчик на обойме"
        return "Датчик на образце"

    @property
    def parent(self) -> str:
        if self.bar:
            return repr(self.bar)
        if self.jacket:
            return repr(self.jacket)
        return ""

    @property
    def as_data_record(self) -> list[str]:
        result = [str(self.id)]
        name = repr(self)
        if parent := self.parent:
            name += ": "+parent
        result.append(name)
        result.append("" if self.tarir is None else str(self.tarir))
        result.append("" if self.gauge_position is None else str(self.gauge_position))
        result += ["", ""]
        if self.creation_datetime:
            result[-2] = str(self.creation_datetime)[:-10]
        if self.notes:
            result[-1] = self.notes
        return result

    def __repr__(self):
        return (f"#{self.id}-{self.channel_type}")

class SetupChannels(Base):
    """
    Вспомогательная таблица для связи установок и каналов измерения.
    """
    __tablename__ = "setupchannels"
    id: Mapped[int] = mapped_column(primary_key=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey('oscchannels.id'))
    setup_id: Mapped[int] = mapped_column(ForeignKey('setups.id'))

class Setup(Base):
    """
    Таблица с экспериментальными установками.
    Каждая установка хранит список каналов измерения.
    """
    __tablename__ = "setups"
    id: Mapped[int] = mapped_column(primary_key=True)
    channels: Mapped[List[OscChannel]] = relationship(secondary="setupchannels")

    # def __repr__(self) -> str:
    #     result = ""
    #     for ch in self.channels:
    #         if ch.bar:
    #             L = ch.bar.length
    #             D = ch.bar.section.par1
    #             D0 = ch.bar.section.par2
    #             mat = ch.bar.material.name
    #             section_type = {
    #                 SectionTypes.circle: "Стержень",
    #                 SectionTypes.tube: "Трубка",
    #             }[ch.bar.section.section_type]
    #             section_size = {
    #                 SectionTypes.circle: f"{D:.0f}",
    #                 SectionTypes.tube: f"{D:.0f}x{D0:.0f}",
    #             }[ch.bar.section.section_type]
    #             result += f"({section_type}:{mat}_{L:.0f}x{section_size})"
    #             continue
    #         elif ch.jacket:
    #             D0 = ch.jacket.D0
    #             D = ch.jacket.D
    #             L = ch.jacket.length
    #             mat = ch.jacket.material.name
    #             result += f"(Обойма:{mat}_{L:.0f}x{D:.0f}x{D0:.0f})"
    #             continue
    #         else:
    #             result += f"(Датчик на образце)"
    #     result += f"[{self.creation_datetime}]"
    #     return result

#
# class ExperimentType(Base):
#     """
#     Таблица с типами экспериментов: буквеный код, описание
#     """
#     __tablename__ = "experimenttypes"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     code: Mapped[str]
#     description: Mapped[str]
#
#     def __repr__(self):
#         return f"Experiment type(id={self.id!r}, description={self.description!r})"
#
#
# class Material(Base):
#     """
#     Таблица с материалами образцов: имя, цифровой код, текстовое описание.
#     """
#     __tablename__ = "materials"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     code: Mapped[int]
#     description: Mapped[Optional[str]]
#
#     def __repr__(self):
#         result = f"Material(name={self.name!r}, code={self.code!r})"
#         if self.description:
#             result = result[:-1] + f", description={self.description!r})"
#         return result
#
#

#
#

#
#
#
#
# class DBImage(Base):
#     __tablename__ = "images"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     bin_data: Mapped[bytes] = mapped_column(LargeBinary)
#     description: Mapped[Optional[str]]
#     video_id: Mapped[Optional[int]] = mapped_column(ForeignKey("videos.id"))
#     experiment_id: Mapped[Optional[int]] = mapped_column(ForeignKey("experiments.id"))
#
#     def __init__(self, image_path: str, **kwargs: Any):
#         super().__init__(**kwargs)
#         if os.path.exists(image_path):
#             print(f"Creating from {image_path}...")
#             image = Pilimage.open(image_path)
#             out = io.BytesIO()
#             image.save(out, format='PNG')
#             bin_data = out.getvalue()
#             self.bin_data = bin_data
#         else:
#             print(f"Image file {image_path} doesn't exist...")
#
#     @property
#     def image(self) -> Pilimage:
#         if self.bin_data:
#             out = io.BytesIO()
#             out.write(self.bin_data)
#             return Pilimage.open(out, formats=['PNG'])
#
#
# class DBVideo(Base):
#     __tablename__ = "videos"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     frame_rate: Mapped[int]
#     frames: Mapped[List["DBImage"]] = relationship()
#     experiment_id: Mapped[Optional[int]] = mapped_column(ForeignKey("experiments.id"))
#
#
# class Sample(Base):
#     __tablename__ = "samples"
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#
# class Experiment(Base):
#     """
#     Таблица для хранения данных индивидуальных испытаний.
#     """
#     __tablename__ = "experiments"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     videos: Mapped[Optional[List["DBVideo"]]] = relationship()
#     images: Mapped[Optional[List["DBImage"]]] = relationship()


if __name__ == "__main__":
    pass
