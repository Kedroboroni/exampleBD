from sqlalchemy.orm import Session
from model import GeneralTabel, Object, City, Users, ConfirmationTabel
from typing import List, Optional

#CRUD для generalTabel:
def create_generalTabel(db: Session, general_tabel: GeneralTabel) -> GeneralTabel:
    db.add(general_tabel)
    db.commit()
    db.refresh(general_tabel)
    return general_tabel


def get_generalTabel(db: Session, tabel_id: int) -> Optional[GeneralTabel]:
    return db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()


def update_generalTabel(db: Session, tabel_id: int, updated_data: dict) -> Optional[GeneralTabel]:
    tabel = db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()
    if tabel:
        for key, value in updated_data.items():
            setattr(tabel, key, value)
        db.commit()
        db.refresh(tabel)
    return tabel


def delete_generalTabel(db: Session, tabel_id: int) -> bool:
    tabel = db.query(GeneralTabel).filter(GeneralTabel.id == tabel_id).first()
    if tabel:
        db.delete(tabel)
        db.commit()
        return True
    return False


#CRUD для object:
def create_object(db: Session, name: str) -> Object:
    new_object = Object(nameObject=name)
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object


def get_object(db: Session, object_id: int) -> Optional[Object]:
    return db.query(Object).filter(Object.id == object_id).first()


def update_object(db: Session, object_id: int, new_name: str) -> Optional[Object]:
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj:
        obj.nameObject = new_name
        db.commit()
        db.refresh(obj)
    return obj


def delete_object(db: Session, object_id: int) -> bool:
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False


#CRUD операции city
def create_city(db: Session, name: str) -> City:
    new_city = City(nameCity=name)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city


def get_city(db: Session, city_id: int) -> Optional[City]:
    return db.query(City).filter(City.id == city_id).first()


def update_city(db: Session, city_id: int, new_name: str) -> Optional[City]:
    city = db.query(City).filter(City.id == city_id).first()
    if city:
        city.nameCity = new_name
        db.commit()
        db.refresh(city)
    return city


def delete_city(db: Session, city_id: int) -> bool:
    city = db.query(City).filter(City.id == city_id).first()
    if city:
        db.delete(city)
        db.commit()
        return True
    return False


#CRUD операции users
def create_user(db: Session, user: Users) -> Users:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> Optional[Users]:
    return db.query(Users).filter(Users.id == user_id).first()


def update_user(db: Session, user_id: int, updated_data: dict) -> Optional[Users]:
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


#CRUD операции confirmationTabel
def create_confirmationTabel(db: Session, confirmation: ConfirmationTabel) -> ConfirmationTabel:
    db.add(confirmation)
    db.commit()
    db.refresh(confirmation)
    return confirmation


def get_confirmationTabel(db: Session, tabel_id: int) -> Optional[ConfirmationTabel]:
    return db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()


def update_confirmationTabel(db: Session, tabel_id: int, updated_data: dict) -> Optional[ConfirmationTabel]:
    tabel = db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()
    if tabel:
        for key, value in updated_data.items():
            setattr(tabel, key, value)
        db.commit()
        db.refresh(tabel)
    return tabel


def delete_confirmationTabel(db: Session, tabel_id: int) -> bool:
    tabel = db.query(ConfirmationTabel).filter(ConfirmationTabel.id == tabel_id).first()
    if tabel:
        db.delete(tabel)
        db.commit()
        return True
    return False