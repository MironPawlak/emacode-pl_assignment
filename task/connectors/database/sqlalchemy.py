import datetime
from sqlalchemy import create_engine, String, Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.sql import func
from task.config import SQLITE_DATABASE, DATE_FORMAT
from task.connectors.database.database import DatabaseConnector
from task.currency_converter import ConvertedPricePLN


class Base(DeclarativeBase):
    pass


class Conversion(Base):
    __tablename__ = "conversion"
    id: Mapped[int] = mapped_column(primary_key=True)
    currency: Mapped[str] = mapped_column(String(3))
    rate: Mapped[float]
    price_in_pln: Mapped[float]
    date: Mapped[datetime.date]


class SqlFileDatabaseConnector(DatabaseConnector):
    def __init__(self) -> None:
        self.engine = self._create_engine()

    @staticmethod
    def _create_engine() -> Engine:
        engine = create_engine(f'sqlite:///{SQLITE_DATABASE}')
        Base.metadata.create_all(engine.engine)
        return engine

    def mapConvertedPriceToConversion(self, converted_price: ConvertedPricePLN) -> Conversion:
        return Conversion(
            currency=converted_price.currency,
            rate=converted_price.currency_rate,
            price_in_pln=converted_price.price_in_pln,
            date=datetime.datetime.strptime(converted_price.currency_rate_fetch_date, DATE_FORMAT)
        )

    def save(self, conversion: ConvertedPricePLN) -> None:
        conversion = self.mapConvertedPriceToConversion(conversion)
        with Session(self.engine) as session:
            session.add(conversion)
            session.commit()
