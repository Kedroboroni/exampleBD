import numpy as np
from datetime import datetime, date, time
from sqlalchemy.orm import Session
from model import GeneralTabel, Object, City
from typing import List, Tuple, Dict
from CRUD import create_generalTabel, create_object, create_city, find_objects_by_name_in_filtered_results






def fill_general_tabel_from_numpy(db: Session, data: np.ndarray) -> Tuple[List[GeneralTabel], List[Tuple[int, str]]]:
    created_records = []
    skipped_rows = []
    
    for index, row in enumerate(data, start=1):
        try:
            # Предполагаем, что порядок столбцов в массиве соответствует порядку полей в GeneralTabel
            nameSatellite, date_obj, startCine, endCine, countCine, longitude, latitude, city, region, nameObject = row
            
            # Преобразование и проверка типов данных
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
                countCine=countCine,
                longitude=longitude,
                latitude=latitude,
                city=city,
                region=region,
                nameObject=nameObject
            )
            
            created_record = create_generalTabel(db, new_record)
            created_records.append(created_record)
        
        except Exception as e:
            # Если возникла ошибка, записываем номер строки и описание ошибки
            skipped_rows.append((index, str(e)))
            continue
    
    return created_records, skipped_rows

# Пример использования:
# numpy_data = np.array([...])  # Ваш массив NumPy
# with Session(engine) as db:
#     filled_records, skipped_rows = fill_general_tabel_from_numpy(db, numpy_data)
#     print(f"Добавлено {len(filled_records)} записей в таблицу GeneralTabel")
#     if skipped_rows:
#         print("Следующие строки были пропущены из-за ошибок:")
#         for row, error in skipped_rows:
#             print(f"Строка {row}: {error}")



#Преобразование запроса в numpy массив (СОЗДАН ДЛЯ ЗАПИСИ В EXEL)
def query_to_numpy(query, columns: List[str] = None) -> np.array:
    result = [[getattr(item, col) for col in columns] for item in query]
    return np.array(result)

#Подсчет количества повторений в массиве, на входе таблица из сорта сортов (тоесть, массив уже с найденным именем объекта)
def count_repeat(tabel: np.array) -> List[str, int]:
    #print(len(tabel))
    return list(zip(tabel[0], len(tabel)))


def count_repeat_all(tabelName: np.array, tabelCount: np.array) -> np.array:
    #!!! СМОТРИ УТ СЛОЖНЫЙ ЗАПРОС С НМИ  НАДО РАБОАТЬ!return [[[key, value] for key, value in count_repeat(find_objects_by_name_in_filtered_results(tabelCount)) if item in tabelName] for item in tabelName]



#Функцияы для перобразования из csv  в бд
#Функция преобразования из бд в geojson
#Функция преобразования из бд  в xlsx
#Функция преобразования из бд в csv
#Функция выбора только по указанной 
#Функция подсчета коэфициента
#
#
#
#



