from sqlalchemy.orm import Session
from model import GeneralTabel, Object, City, Users, ConfirmationTabel
from typing import List, Optional, Dict, Any
from sqlalchemy import func, select
import numpy as np





#CRUD для generalTabel:
def create_generalTabel(db: Session, general_tabel: GeneralTabel) -> GeneralTabel:
    
    """Создает запись в бд таблицы GeneralTabel"""
    db.add(general_tabel)
    db.commit()
    db.refresh(general_tabel)
    return general_tabel


def get_generalTabel(db: Session, tabel_id: int) -> Optional[GeneralTabel]:

    """Возвращает запись по id из таблицы GeneralTabel"""
    return db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()


def update_generalTabel(db: Session, tabel_id: int, updated_data: dict) -> Optional[GeneralTabel]:

    """Обновляет запись по id в таблице generalTabel"""
    tabel = db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()
    if tabel:
        for key, value in updated_data.items():
            setattr(tabel, key, value)
        db.commit()
        db.refresh(tabel)
    return tabel


def delete_generalTabel(db: Session, tabel_id: int) -> bool:

    """Удаляет записи в таблице generalTabel, возвращает True или Flse при выполнении и не выполнении удаления"""
    tabel = db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()
    if tabel:
        db.delete(tabel)
        db.commit()
        return True
    return False


def filter_generalTabel_by_partial_word(db: Session, column_name: str, word: str) -> List[GeneralTabel]:

    """Возвращает таблицу с совпавщими словами (не жестко) из таблицы generalTabel"""
    return db.query(GeneralTabel).filter(func.lower(getattr(GeneralTabel, column_name)).contains(word.lower())).all()


def filter_generalTabel_by_exact_word(db: Session, column_name: str, word: str) -> List[GeneralTabel]:

    """Возвращает таблицу с совпавщими словами (жестко) из таблицы generalTabel"""
    return db.query(GeneralTabel).filter(getattr(GeneralTabel, column_name) == word).all()


def get_generalTabel_columns(db: Session, tabel_id: int, columns: List[str]) -> Optional[Dict[str, Any]]:

    """Вернет значения в указанных колонках таблицы GeneralTabel"""
    query = select(*[getattr(GeneralTabel, col) for col in columns]).where(GeneralTabel.id == tabel_id)
    result = db.execute(query).first()
    return result._asdict() if result else None


#CRUD для object:
def create_object(db: Session, name: str) -> Object:

    """Создает запись в бд таблицы Object"""
    new_object = Object(nameObject=name)
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object


def get_object(db: Session, object_id: int) -> Optional[Object]:

    """Возвращает запись по id из таблицы Object"""
    return db.query(Object).filter(Object.id == object_id).first()


def update_object(db: Session, object_id: int, new_name: str) -> Optional[Object]:

    """Обновляет запись по id в таблице Object"""
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj:
        obj.nameObject = new_name
        db.commit()
        db.refresh(obj)
    return obj


def delete_object(db: Session, object_id: int) -> bool:

    """Удаляет записи в таблице object, возвращает True или Flse при выполнении и не выполнении удаления"""
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False


#CRUD операции city
def create_city(db: Session, name: str) -> City:

    """Создает запись в бд таблице City"""
    new_city = City(nameCity=name)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city


def get_city(db: Session, city_id: int) -> Optional[City]:

    """Возвращает запись по id из таблицы City"""
    return db.query(City).filter(City.id == city_id).first()


def update_city(db: Session, city_id: int, new_name: str) -> Optional[City]:

    """Обновляет запись по id в таблице City"""
    city = db.query(City).filter(City.id == city_id).first()
    if city:
        city.nameCity = new_name
        db.commit()
        db.refresh(city)
    return city


def delete_city(db: Session, city_id: int) -> bool:

    """Удаляет записи в таблице city, возвращает True или Flse при выполнении и не выполнении удаления"""
    city = db.query(City).filter(City.id == city_id).first()
    if city:
        db.delete(city)
        db.commit()
        return True
    return False


#CRUD операции users
def create_user(db: Session, user: Users) -> Users:

    """Создает запись в бд таблице Users"""
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> Optional[Users]:

    """Возвращает запись по id из таблицы Users"""
    return db.query(Users).filter(Users.id == user_id).first()


def update_user(db: Session, user_id: int, updated_data: dict) -> Optional[Users]:

    """Обновляет запись по id в таблице Users"""
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    """Удаляет записи в таблице Users, возвращает True или Flse при выполнении и не выполнении удаления"""
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


#CRUD операции confirmationTabel
def create_confirmationTabel(db: Session, confirmation: ConfirmationTabel) -> ConfirmationTabel:

    """Создает запись в бд таблице confirmationTabel"""
    db.add(confirmation)
    db.commit()
    db.refresh(confirmation)
    return confirmation


def get_confirmationTabel(db: Session, tabel_id: int) -> Optional[ConfirmationTabel]:

    """Возвращает запись по id из таблицы confirmationTabel"""
    return db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()


def update_confirmationTabel(db: Session, tabel_id: int, updated_data: dict) -> Optional[ConfirmationTabel]:

    """Обновляет запись по id в таблице confirmationTabel"""
    tabel = db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()
    if tabel:
        for key, value in updated_data.items():
            setattr(tabel, key, value)
        db.commit()
        db.refresh(tabel)
    return tabel


def delete_confirmationTabel(db: Session, tabel_id: int) -> bool:

    """Удаляет записи в таблице confirmationTabel, возвращает True или Flse при выполнении и не выполнении удаления"""
    tabel = db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()
    if tabel:
        db.delete(tabel)
        db.commit()
        return True
    return False


def get_columns_by_tabel(db: Session, tabel, columns: List[str]) -> Optional[List[Any]]:

    """Возвращает таблицу с колонками перечисленными в параметре columns: <list>"""
    query = select(*[getattr(tabel, col) for col in columns])
    result = db.execute(query).all()
    return result if result else None


def filter_tabel_by_exact_word(db: Session, tabel, columnName: str, word: str) -> List[GeneralTabel]:

    """Возвращает отфильтрованную таблицу из колонки <columnName> по слову <word>"""
    return db.query(tabel).filter(getattr(tabel, columnName) == word).all()


def find_objects_by_name_in_filtered_results(db: Session, column: str, word: str, nameObject: str) -> List[GeneralTabel]:

    """Возвращает объект по названию в отфильтрованном результате"""
    return db.query(GeneralTabel).filter(
        getattr(GeneralTabel, column) == word,
        GeneralTabel.nameObject == nameObject
    ).all()




