import numpy as np
from datetime import datetime, date, time
from sqlalchemy.orm import Session
from model import GeneralTabel, Object, City
from typing import List, Tuple, Dict
from CRUD import create_generalTabel, create_object, create_city, find_objects_by_name_in_filtered_results






def fill_generalTabel_from_numpy(db: Session, data: np.ndarray) -> Tuple[List[GeneralTabel], List[Tuple[int, str]]]:

    """Записывает массив типа <numpy> в бд, возвращает <список записей>, <список пропущенных строк>"""
    created_records = []
    skipped_rows = []
    
    for index, row in enumerate(data, start=1):
        try:
            
            nameSatellite, date_obj, startCine, endCine, countCine, longitude, latitude, city, region, nameObject = row
            nameSatellite = str(nameSatellite)

            if isinstance(date_obj, datetime):
                date_obj = date_obj.date()
            elif isinstance(date_obj, str):
                date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()

            if isinstance(startCine, datetime):
                startCine = startCine.time()
            elif isinstance(startCine, str):
                startCine = datetime.strptime(startCine, '%H:%M:%S').time()
    
            if isinstance(endCine, datetime):
                endCine = endCine.time()
            elif isinstance(endCine, str):
                endCine = datetime.strptime(endCine, '%H:%M:%S').time()
            
            countCine = float(countCine)
            longitude = float(longitude)
            latitude = float(latitude)
            city = str(city)
            region = str(region)
            nameObject = str(nameObject)
            
            city_obj = db.query(City).filter(City.nameCity == city).first() #Проверка существования города, создание их при необходимости
            if not city_obj:
                city_obj = create_city(db, city)
            
            object_obj = db.query(Object).filter(Object.nameObject == nameObject).first() #Проверка существования объекта, создание их при необходимости
            if not object_obj:
                object_obj = create_object(db, nameObject)
            
            
            new_record = GeneralTabel(
                nameSatellite=nameSatellite,
                date=date_obj,
                startCine=startCine,
                endCine=endCine,
                countCine=countCine,
                longitude=longitude,
                latitude=latitude,
                city=city,
                region=region,
                nameObject=nameObject
            ) #Создание записи GeneralTabel
            
            created_record = create_generalTabel(db, new_record)
            created_records.append(created_record)
        
        except Exception as e:
            skipped_rows.append((index, str(e))) #Если возникла ошибка, записываем номер строки и описание ошибки
            continue
    
    return created_records, skipped_rows


#Преобразование запроса в numpy массив (СОЗДАН ДЛЯ ЗАПИСИ В EXEL)
def query_to_numpy(query, columns: List[str] = None) -> np.array:

    """Преобразеует запрос (таблицу которую дастали из бд типа <имя таблицы>)
        в массив numpy, для быстрой работы с ним)"""
    result = [[getattr(item, col) for col in columns] for item in query]
    return np.array(result)


#Подсчет количества повторений в массиве, на входе таблица из сорта сортов (тоесть, массив уже с найденным именем объекта)
def count_repeat(tabelRepeats: np.array) -> Tuple:

    """Вернет количесвто строк из табицы ->
    <значение первой строки первого столбца в массиве> <количсвто строк в массиве>"""
    return (tabelRepeats[0][0], len(tabelRepeats))









