from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Base
import pandas as pd
import numpy as np
from engine import fill_generalTabel_from_numpy, query_to_numpy, count_repeat
from CRUD import get_generalTabel, create_generalTabel, get_generalTabel_columns, filter_generalTabel_by_exact_word
from CRUD import get_columns_by_tabel, filter_generalTabel_by_partial_word, filter_tabel_by_exact_word
from CRUD import find_objects_by_name_in_filtered_results
from model import GeneralTabel, Object




if __name__ == "__main__":

    BB_URL = r"sqlite:///C:\WorkSpace\Python\projectGSH\ctrRecBase.db"
    engine = create_engine(BB_URL, echo=False)
    Base.metadata.create_all(engine)

path = r"C:\WorkSpace\Python\projectGSH\19.09.2024-20.09.2024.xlsx"
df = pd.read_excel(path, header = 0, usecols = [0,1,2,3,4,5,6,7,8,9])
#print(df)
dateArr = df.to_numpy()

with Session(engine) as db:
        #filled_records, skipped_rows = fill_generalTabel_from_numpy(db, dateArr)
        #print(f"Добавлено {len(filled_records)} записей в таблицу GeneralTabel")
        #if skipped_rows:
            #print(f"Следующие строки были пропущены из-за ошибок: {skipped_rows}")
            #for row, error in skipped_rows:
                #print(f"Строка {row}: {error}")

    #print(get_generalTabel(db, 10).nameObject)# строку по объекту, так же может достать конктреный столбец из этой строки
    #columns = ['nameObject', 'nameObject']
    #print(get_columns_by_tabel(db, GeneralTabel, columns = ["region", "city"])) #Возвращает список кортежей
    #print(type(get_generalTabel(db, 1).city))
    #print(type(filter_generalTabel_by_partial_word(db, "city", "Москва")))
    #print(filter_generalTabel_by_exact_word(db, "city", "Россия")[0])
    #print(query_to_numpy(filter_tabel_by_exact_word(db, "city", "Россия"), columns = ["city", "nameObject", "region"]))
    #tabel = filter_generalTabel_by_exact_word(db, "city", "Россия")
    #print(filter_tabel_by_exact_word(db, tabel, "nameObject", "-")[:].nameObject)
    #arrFiltr = query_to_numpy(filter_generalTabel_by_exact_word(db, "city", "Россия"), columns = ["nameObject"])
    
    #Получение массива с именами объектов
    #query_result = get_columns_by_tabel(db, Object, columns=["nameObject"])
    tabel = find_objects_by_name_in_filtered_results(db, "city", "Россия", "-")
    arr = query_to_numpy(tabel , ["nameObject", "id"])
    l = count_repeat(arr)
    print(l[1])
    
    #object_names_array = count_repeat(query_to_numpy(query_result, columns=["nameObject"]))
    #print(query_to_numpy(query_result, columns=["nameObject"]))
    #print(count_repeat(query_to_numpy(find_objects_by_name_in_filtered_results(db, "city", "Россия", "-"), columns = ["nameObject", "city", "region"], columns=["nameObject"])))
    ###!!!!! Выше сложный хзапрос, нужно работать!
    #arrName = query_to_numpy(get_columns_by_tabel(db, Object, ["nameObject"]), columns = ["nameObject"])
    
    
    #arr = query_to_numpy(find_objects_by_name_in_filtered_results(db, "city", "Россия", "-"), columns = ["nameObject", "city", "region"])
    #print(arrFiltr)
    #print(count_repeat_all(object_names_array, arrFiltr)) 