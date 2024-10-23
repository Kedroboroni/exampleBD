import numpy as np
from datetime import datetime, date, time
from sqlalchemy.orm import Session
from model import GeneralTabel, Object, City
from typing import List
from CRUD import create_generalTabel, create_object, create_city

def fill_general_tabel_from_numpy(db: Session, data: np.ndarray) -> List[GeneralTabel]:
    created_records = []
    
    for row in data:
        # Предполагаем, что порядок столбцов в массиве соответствует порядку полей в GeneralTabel
        nameSatellite, date_str, startCine_str, endCine_str, countCine, longitude, latitude, city, region, nameObject = row
        
        # Преобразование строк в соответствующие типы данных
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        startCine = datetime.strptime(startCine_str, '%H:%M:%S').time()
        endCine = datetime.strptime(endCine_str, '%H:%M:%S').time()
        
        # Проверка существования города и объекта, создание их при необходимости
        city_obj = db.query(City).filter(City.nameCity == city).first()
        if not city_obj:
            city_obj = create_city(db, city)
        
        object_obj = db.query(Object).filter(Object.nameObject == nameObject).first()
        if not object_obj:
            object_obj = create_object(db, nameObject)
        
        # Создание записи GeneralTabel
        new_record = GeneralTabel(
            nameSatellite=nameSatellite,
            date=date_obj,
            startCine=startCine,
            endCine=endCine,
            countCine=float(countCine),
            longitude=float(longitude),
            latitude=float(latitude),
            city=city,
            region=region,
            nameObject=nameObject
        )
        
        created_record = create_generalTabel(db, new_record)
        created_records.append(created_record)
    
    return created_records

# Пример использования:
# numpy_data = np.array([...])  # Ваш массив NumPy
# with Session(engine) as db:
#     filled_records = fill_general_tabel_from_numpy(db, numpy_data)
#     print(f"Добавлено {len(filled_records)} записей в таблицу GeneralTabel")