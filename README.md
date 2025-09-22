# iris-classification

## Описание датасета
Использован классический датасет **Iris** (Фишера), включающий 150 наблюдений ирисов трёх видов (*setosa, versicolor, virginica*).  
Признаки:  
- длина и ширина чашелистика,  
- длина и ширина лепестка.  

## Что сделано
- Проведён разведочный анализ данных (EDA) с визуализациями.  
- Обучена модель классификации.  
- Оценены результаты (accuracy, confusion matrix, classification report).  

## Результаты
- Accuracy: **0.93**  
- Confusion matrix:  
  [[15 0 0]
  [ 0 14 1]
  [ 0 2 13]]
- Classification report:  
            precision    recall  f1-score   support

        0       1.00      1.00      1.00        15
        1       0.88      0.93      0.90        15
        2       0.93      0.87      0.90        15

 accuracy                           0.93        45
macro avg       0.93      0.93      0.93        45
weighted avg 0.93 0.93 0.93 45
## Выводы
- Модель показала высокое качество (**93%**).  
- Ошибки в основном связаны с близкими по признакам классами (*versicolor* и *virginica*).  
- Наиболее информативные признаки: **длина и ширина лепестка**.  

## Как запустить
1. Клонировать репозиторий:
 git clone https://github.com/Kidukwe/iris-classification.git
 cd iris-classification 
2. Установить зависимости (рекомендуется использовать виртуальное окружение):
 pip install -r requirements.txt
3. Запустить Jupyter Notebook.
4. Открыть notebook.ipynb и выполнить все ячейки.

## Ps 
Каждый шаг кода максимально пытался расписать поэтапно в самом коде iris_classification.ipynb

