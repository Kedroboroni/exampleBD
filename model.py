from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import Date, Time, Float, String, Integer, Boolean
from sqlalchemy import ForeignKey
from typing import List





class Base(DeclarativeBase):

    pass


class GeneralTabel(Base):

    __tablename__ = "generalTabel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nameSatellite: Mapped[str] = mapped_column(String(15))
    date: Mapped[Date] = mapped_column(Date)
    startCine: Mapped[Time] = mapped_column(Time)
    endCine: Mapped[Time] = mapped_column(Time)
    countCine: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    latitude: Mapped[float] = mapped_column(Float)
    city: Mapped[str] = mapped_column(String(100), ForeignKey("city.nameCity"))
    region: Mapped[str] = mapped_column(String(150))
    nameObject: Mapped[str] = mapped_column(String(200), ForeignKey("object.nameObject"))


    def __repr__(self) -> str:
        return f"""generalTabel(ИмяСпутника = {self.nameSatellite}, Дата = {self.date}, 
                    Начало = {self.startCine}, Конец = {self.endCine}, Длительность = {self.countCine}, 
                    Широта = {self.latitude}, Долгота = {self.longitude}, Страна = {self.city},
                    Регион = {self.region}, Имя объекта = {self.nameObject},
                    )""".replace('\n', ' ').replace('                    ', ' ')
    

class Object(Base):

    __tablename__ = "object"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nameObject: Mapped[str] = mapped_column(String(200), unique=True)
    

class City(Base):

    __tablename__ = "city"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nameCity: Mapped[str] = mapped_column(String(100), unique=True)


    def __repr__(self) -> str:
        return f"""contry(id = {self.id}, nameContry = {self.nameCity}
                    )""".replace('\n', ' ').replace('                    ', ' ')
    

class Users(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    loginUser: Mapped[str] = mapped_column(String(100), unique = True)
    nameUser: Mapped[str] = mapped_column(String(100))
    lastNameUser: Mapped[str] = mapped_column(String(100))
    roleUser: Mapped[str] = mapped_column(String(100)) # Администратор, Аналитик, Пользователь
    paswordHash: Mapped[str] = mapped_column(String(100))
    

    def __repr__(self) -> str:
        return f"""users(id = {self.id}, Логин = {self.loginUser}, 
                    Имя = {self.nameUse}, Фамилия = {self.lastNameUser},
                    Парва доступа = {self.roleUser}, 
                    Пароль = {self.paswordHash},
                    )""".replace('\n', ' ').replace('                    ', ' ')
    

class ConfirmationTabel(Base):

    __tablename__ = "confirmationTabel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nameObject: Mapped[str] = mapped_column(String(200), ForeignKey("object.nameObject"))
    dateLastConfirmation: Mapped[Date] = mapped_column(Date, nullable=True)
    presensAttack: Mapped[bool] = mapped_column(Boolean, default=False)


    def __repr__(self) -> str:
        return f"""confirmationTabel(id = {self.id}, Имя объекта = {self.nameObject}, 
                    Дата последнего подтверждения = {self.dateLastConfirmation}, 
                    Наличие атаки = {self.presensAttack}
                    )""".replace('\n', ' ').replace('                    ', ' ')

    

 



